import unittest

import requests

from lib.utils import *
import os
import ddt

from setting import DATA_PATH

# url = 'http://hn216.api.yesapi.cn/'
@ddt.ddt
class Check(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'check.yaml'))
    def test_check(self,**case):
        url = case.get('url')
        method = case.get('method')
        data = case.get('data')
        check = case.get('check')
        # data = set_res_data(data)

        if method.lower() == 'post':
            res = requests.post(url=url,data=data)
            resp = res.text
            print(resp)
            print(type(resp))
        else:
            res = requests.get(url=url,params=data)
            resp = res.text


        results = set_res_data(resp)
        for c in check:
            self.assertIn(c,results)



if __name__ == '__main__':
    unittest.main()



