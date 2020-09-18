##/cases/test_UserProfile.py
import unittest
import requests
from setting import *
import os
import ddt
from lib.utils_userprofile import set_res_data


@ddt.ddt
class UserProfile(unittest.TestCase):
    # 使用ddt加载yaml文件
    @ddt.file_data(os.path.join(DATA_PATH, 'userprofile.yaml'))
    def test_userprofile(self, **case):  # 星号用于接收解包后的用例内容
        url = case.get('url')
        method = case.get('method')
        data = case.get('data')
        check = case.get('check')

        # 根据方法去构造请求
        try:
            if method.lower() == 'post':
                res = requests.post(url, data=data)
                resp = res.text
            else:
                res = requests.get(url, params=data)
                resp = res.text
        except Exception as e:
            print("接口请求出错！")
            resp = e

        # 处理结果数据，方便比较
        results = set_res_data(resp)

        # 根据构造结果，进行断言
        for c in check:
            self.assertIn(c, results)


if __name__ == '__main__':
    unittest.main()
