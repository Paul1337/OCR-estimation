import configparser
config = configparser.ConfigParser()
res = config.read('./config.ini')
etalonsDir = config['DEFAULT']['EtalonsDir']
