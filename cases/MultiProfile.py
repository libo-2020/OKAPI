"""
测试批量获取会员信息
"""
import unittest
import requests,ddt,os
from setting import *


@ddt.ddt
class MultiProfile(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'MultiProfile.yaml'))
    def test_multiprofile(self,**payload):
        self._testMethodDoc=payload.get('detail')
        base_url=payload.get('url') #取url
        args=payload.get('data') #获取需要传递得参数
        if payload.get('method')=='get':
            resp=requests.get(url=base_url,params=args).json()
            result = len(resp.get('data').get('info_list')) #获取长度
        else:
            resp = requests.post(url=base_url, data=args).json()
            result=resp.get('ret')
        check = payload.get('check')
        self.assertEqual(check, result)



if __name__ == '__main__':
    unittest.main()
