import unittest
from setting import *
import time
from BeautifulReport import BeautifulReport

# 生成测试用例函数
# create_case('case_template.txt')

# 查找用例
discover = unittest.defaultTestLoader.discover(CASE_PATH, 'test_*.py')

# 执行并生成报告
time_now = time.strftime('%Y%m%d%H%M%S')

report_name = '小白接口-{}.html'.format(time_now)

runner = BeautifulReport(discover)

runner.report('小白接口测试', report_name, REPORT_PATH)
