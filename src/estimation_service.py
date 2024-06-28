from ocr_runner import OcrRunner
from text_comparator import TextComparator
from typing import List

# класс для оценки качества работы OCR 
class EstimationService:

  def __init__(self, ocr_runner: OcrRunner):
    self.ocr_runner = ocr_runner
    self.text_comparator = TextComparator()
    pass

  def get_estimation(self, etalon_path: str):
    # прочитать картинку в etalon_path (например etalon_path = '2-2', картинка 2-2.png)
    # прочитать текст в etalon_path (2-2.txt)
    ocrText = self.ocr_runner.convert_to_text(img) # получить текст полученный в результате ocr
    difference = self.text_comparator.compare(ocrText) # сравнить
    return difference
  
  def get_preprocessing_estimation(self, img_path: List[str], text_path: str):
    # здесь нужно взять список картинок (предполагается разная предобработка одной картики) 
    # и для каждой выполнить OCR, сравнить с text_path, вернуть массив оценок по каждой картинке
    pass
