from BeautifulReport import BeautifulReport
from setting import CASE_PATH,REPORT_PATH,DATA_PATH
import time
import unittest


discover=unittest.defaultTestLoader.discover(start_dir=CASE_PATH,pattern='test_otherprofile.py')
time_now=time.strftime('%Y%m%d%H%M%S')
report_name="小白接口-获取其他会员个人资料接口.{}".format(time_now)
runner = BeautifulReport(discover)
runner.report("接口自动化项目",filename=report_name,report_dir=REPORT_PATH)
