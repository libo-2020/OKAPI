import unittest
import requests
import os
import ddt

from lib.utils import set_res_data
from setting import DATA_PATH


@ddt.ddt
class UpdateExtInfo(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'login.yaml'))
    def test_UpdateExtInfo(self,**case):
        url= case.get('url')
        method= case.get('method')
        data= case.get('data')
        check= case.get('check')
        if method== 'get':
            respones= requests.get(url=url, params=data)
        else:
            respones= requests.post(url=url, data=data)
            respones= respones.text
        respones= set_res_data(respones)
        print(respones)
        for c in check:
            self.assertIn(c, respones)

if __name__ == '__main__':
    unittest.main()
