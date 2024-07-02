import configparser
from src.estimation_service import EstimationService
from src.tesseract_runner import TesseractRunner
from src.text_comparator import TextComparator

config = configparser.ConfigParser()
res = config.read('./config.ini')
etalons_dir = config['DEFAULT']['EtalonsDir']

estimation_service = EstimationService(etalons_dir=etalons_dir, ocr_runner=TesseractRunner(), text_comparator=TextComparator)

# test
print('Enter etalon name:')
etalon_name = input()
test_estimation_result = estimation_service.get_estimation(etalon_name)
print(f'estimation for etalon: difference = {test_estimation_result}')