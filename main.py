from src.estimation_service import EstimationService
from src.tesseract_runner import TesseractRunner
from src.text_comparator import TextComparator
from src.config import config

etalons_dir = config['DEFAULT']['EtalonsDir']

estimation_service = EstimationService(etalons_dir=etalons_dir, ocr_runner=TesseractRunner(), text_comparator=TextComparator())

text_comp = TextComparator()

if config['DEFAULT']['Mode'] == 'etalon':
  while True:
    print('Enter etalon name:')
    etalon_name = input()
    print('Processing...')
    test_estimation_result = estimation_service.get_estimation(etalon_name)
    print(f'Estimation for etalon: difference = {test_estimation_result}')
elif config['DEFAULT']['Mode'] == 'preproc':
  while True:
    print('Enter preproc directory path:')
    preproc_dir_path = input()
    print('Enter textfile name in that directory:')
    text_file_name = input()
    print('Processing...')
    estimation_service.print_preprocessing_estimation(preproc_dir_path, text_file_name)
    
else:
  print('Mode is unknown, should be etalon or preproc')