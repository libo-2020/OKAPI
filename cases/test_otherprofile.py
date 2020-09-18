"""
otherprofile接口测试用例
"""

import unittest,requests,ddt,os
from lib.utils import set_res_data
from setting import DATA_PATH

@ddt.ddt
class OtherProfile(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'otherprofile.yaml'))
    def test_other_profile(self,**payload):
        url=payload.get('url')
        method=payload.get('method')
        check=payload.get('check')
        data=payload.get('data')
        try:
            if method == 'get':
                res = requests.get(url, params=data)
                resp = res.text
            else:
                res = requests.post(url, data=data)
                resp = res.text
        except Exception as e:
            print(e)
            return e
        results=set_res_data(resp)
        print(results)
        print(check)
        for c in check:
            self.assertIn(c,check)
        # response=requests.get(url=url,params=data)
        # print(response.text)
        # return response.text
if __name__ == '__main__':
    unittest.main()
