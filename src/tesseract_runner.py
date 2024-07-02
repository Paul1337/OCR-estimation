from ocr_runner import OcrRunner
from config import config
import pytesseract as tess
tess.pytesseract.tesseract_cmd = config['DEFAULTS']['TesseractPath']
from PIL import Image

class TesseractRunner(OcrRunner):
    def convert_to_text(self, img_path):
        return self.perform_ocr(img_path)

    def perform_ocr(self, img_path):
        img = Image.open(img_path)
        text = tess.image_to_string(img, lang='rus')
        return text
