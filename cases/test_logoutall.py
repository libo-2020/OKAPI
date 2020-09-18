import os
import unittest

import ddt
import requests

from lib.utils import *

from setting import  BASE_PATH, DATA_PATH



@ddt.ddt
class LogoutAll(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'aogoutall.yaml'))
    def test_logouAll(self,**case):
        self._testMethodDoc = case.get("detail")
        #构建参数
        # print(case)
        url=case.get('url')
        method=case.get('method')
        data=case.get('data')
        check=case.get('check')
        # print(check)

        if method.lower()=='get':
            res=requests.get(url,params=data)
            resp=res.text
            print(resp)
            print(type(resp))
        else:
            res = requests.post(url, data=data)
            resp = res.text


        #构建的结果，匹配结果
        # check=['ret=200','err_code=0','"err_msg="']
        result = set_res_data(resp)
        for c in check:
            self.assertIn(c,result)
        # def test_%(method_name)s(self,**case)

if __name__ == '__main__':
    unittest.main()