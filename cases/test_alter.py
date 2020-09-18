import os
import unittest
import ddt
import requests

from lib.utils import *
from setting import *

@ddt.ddt
class Alter(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'AlterPassword.yaml'))
    def test_alter(self,**case):
        print(case)
        url=case.get('url')
        print(url)
        method=case.get('method')
        data=case.get('data')
        print(data)
        check=case.get('check')
        print(check)
        if 'old_password' in data:
            data['old_password']=hash_code(data['old_password'])
            print(data['old_password'])
        if 'new_password' in data:
            data['new_password'] = hash_code(data['new_password'])
            print(data['new_password'])

        if method.lower() == 'post':
            res=requests.post(url,data=data)
            resp=res.text
            print(resp)
        else:
            res=requests.get(url,params=data)
            resp=res.text
            print(resp)

        result=set_res_data(resp)
        print(result)
        for i in check:
            print(i)
            self.assertIn(i,result)

if __name__ == '__main__':
    unittest.main()