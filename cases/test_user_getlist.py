import os
import unittest

import ddt
import requests

from lib.utils_otherprofile import set_res_data
from setting import DATA_PATH

@ddt.ddt
class UserGetListTestCase(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'user_getlist.yaml'))
    def test_user_getlist(self,**data):
        #注明url，request.method
        base_url=data['url']
        method=data['method']
        check=data['check']
        print(check)
        payload=data['data']
        if method=='post':
            res=requests.post(base_url,data=payload)
        else:
            res=requests.get(base_url,params=data)
        result=res.text
        print(result)
        # self.assertEqual(True, False)
        # check=['ret=200','err_code=0','"err_msg="']
        results=set_res_data(result)
        print(results)
        for c in check:
            self.assertIn(c,results)


if __name__ == '__main__':
    unittest.main()
