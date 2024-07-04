from src.ocr_runner import OcrRunner
from src.text_comparator import TextComparator
from typing import List
from pathlib import Path
import os

# класс для оценки качества работы OCR 
class EstimationService:

  def __init__(self, etalons_dir: str, ocr_runner: OcrRunner, text_comparator: TextComparator):
    self.etalons_dir = Path(etalons_dir)
    self.ocr_runner = ocr_runner
    self.text_comparator = text_comparator

    self.img_extensions = ['png', 'jpg', 'jpeg']
    pass

  def get_img_path(self, img_name):
    img_path = self.etalons_dir.joinpath(f"{img_name}.{self.img_extensions[0]}")

    extInd = 1
    while not img_path.exists() and extInd < len(self.img_extensions):
      img_path = self.etalons_dir.joinpath(f"{img_name}.{self.img_extensions[extInd]}")
      extInd += 1

    if not img_path.exists():
      raise FileNotFoundError(f"Image {img_path} not found ({' '.join(self.img_extensions)} tried)")
    
    return img_path


  def get_estimation(self, etalon_name: str) -> int:
    img_path = self.get_img_path(etalon_name)
    text_file_path = self.etalons_dir.joinpath(f"{etalon_name}.txt")

    if not text_file_path.exists():
      raise FileNotFoundError(f"File {text_file_path} not found.")

    with open(text_file_path, 'r') as text_file:
      original_text = text_file.read()

    ocr_text = self.ocr_runner.convert_to_text(img_path) 

    difference = self.text_comparator.compare(original_text, ocr_text)
    return difference
  
  def print_preprocessing_estimation(self, preproc_dir_path: List[str], text_file_name: str) -> int:
    text_file_path = Path(preproc_dir_path).joinpath(text_file_name)
    if not text_file_path.exists():
      raise FileNotFoundError(f"File {text_file_path} not found.")

    with open(text_file_path, 'r') as text_file:
      original_text = text_file.read()

    img_paths = []
    for filename in os.listdir(preproc_dir_path):
      file_path = Path(preproc_dir_path).joinpath(filename)
        
      if os.path.isfile(file_path):
        _, extension = os.path.splitext(filename)
        if extension.lower()[1:] in self.img_extensions:
          img_paths.append(file_path)
      
    for img_path in img_paths:
      ocr_text = self.ocr_runner.convert_to_text(img_path) 
      difference = self.text_comparator.compare(original_text, ocr_text)
      # print(ocr_text)
      print(f'Image {img_path}, diff = {difference}')

