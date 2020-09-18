"""
otherprofile接口测试用例
"""
import unittest,requests,ddt,os
from lib.utils_otherprofile import set_res_data
from setting_otherprofile import DATA_PATH

@ddt.ddt
class OtherProfile(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'otherprofile.yaml'))
    def test_otherprofile(self,**payload):
        self._testMethodDoc=payload.get('detail')
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
        # print(results)
        # print(check)
        for c in check:
            # print(c)
            self.assertIn(c,results)

if __name__ == '__main__':
    unittest.main()
