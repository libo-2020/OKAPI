import time
import unittest

from BeautifulReport import BeautifulReport

from setting import CASE_PATH, REPORT_PATH

discover=unittest.defaultTestLoader.discover(CASE_PATH,'test_check.py')
time_now = time.strftime('%Y%m%d%H%M%S')
report_name ='登录状态-{}'.format(time_now)

runner = BeautifulReport(discover)
runner.report('小白接口测试',report_name, REPORT_PATH)