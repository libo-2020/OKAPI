import os

API_URL = 'http://hn216.api.yesapi.cn/'
APP_KEY = '503ED17D034EFD2CF9337AED9F12AE1A'


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH,'data')
CASE_PATH = os.path.join(BASE_PATH,'cases')
REPORT_PATH = os.path.join(BASE_PATH,'report')
print(DATA_PATH)
print(CASE_PATH)
print(REPORT_PATH)
