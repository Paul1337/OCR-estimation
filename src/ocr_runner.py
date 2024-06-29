from abc import ABC, abstractmethod

# абстрактный класс для запуска процесса OCR
class OcrRunner:
  @abstractmethod
  def convert_to_text(self, img):
    
    pass