###setting.py
import os

# 服务相关配置
API_URL = 'http://hn216.api.yesapi.cn/'
API_KEY = 'C934E82FEE5E64FC9035E3315BA667AC'

# 设置目录的绝对路径

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# yaml测试用例存放位置
DATA_PATH = os.path.join(BASE_PATH, 'data')

# unittest测试类文件存放位置
CASE_PATH = os.path.join(BASE_PATH, 'cases')

# 测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')

