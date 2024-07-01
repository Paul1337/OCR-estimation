from src.ocr_runner import OcrRunner
from src.text_comparator import TextComparator
from typing import List
from pathlib import Path

# класс для оценки качества работы OCR 
class EstimationService:

  def __init__(self, etalons_dir: str, ocr_runner: OcrRunner, text_comparator: TextComparator):
    self.etalons_dir = Path(etalons_dir)
    self.ocr_runner = ocr_runner
    self.text_comparator = text_comparator
    pass

  def get_estimation(self, etalon_name: str) -> int:
    text_file_path = self.etalons_dir.joinpath(f"{etalon_name}.txt")
    img_path = self.etalons_dir.joinpath(f"{etalon_name}.png")

    if not text_file_path.exists():
      raise FileNotFoundError(f"File {text_file_path} not found.")

    if not img_path.exists():
      raise FileNotFoundError(f"Image {img_path} not found.")

    with open(text_file_path, 'r') as text_file:
      original_text = text_file.read()

    ocr_text = self.ocr_runner.convert_to_text(img_path) 

    difference = self.text_comparator.compare(original_text, ocr_text)
    return difference
  
  def get_preprocessing_estimation(self, img_path: List[str], text_path: str) -> int:
    # здесь нужно взять список картинок (предполагается разная предобработка одной картики) 
    # и для каждой выполнить OCR, сравнить с text_path, вернуть массив оценок по каждой картинке
    pass
