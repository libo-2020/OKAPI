import time
import unittest
from setting import *
from BeautifulReport import BeautifulReport
#查找用例
discover=unittest.defaultTestLoader.discover(CASE_PATH,pattern='test_logoutall.py')
#执行生成报告
title='接口测试'
time_now=time.strftime('%Y%m%d%H%M%S')
BeautifulReport(discover).report('小白接口清空会员登录会话接口','清除会话接口{}'.format(time_now),REPORT_PATH)