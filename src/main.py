import configparser
from tesseract_runner import TesseractRunner
# config = configparser.ConfigParser()
# res = config.read('./config.ini')
# etalonsDir = config['DEFAULT']['EtalonsDir']


tesseract_runner = TesseractRunner()
result = tesseract_runner.convert_to_text('etalons/3-19.jpg')
print(result)