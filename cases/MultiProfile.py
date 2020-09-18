"""
测试批量获取会员信息
"""
import unittest
import requests,ddt,os
from setting import *
#uuid数据
uuid1='676003847A6FAF10908B6A6184A84B2C,3FE6E35B5A4DC896CB8034E2F08A1473'
uuid2='3FE6E35B5A4DC896CB8034E2F08A1473'
uuid3='4EC1E8184D8C377B2314EA327AD60354'
s='App.User.MultiProfile'
from lib.tools import str
#请求url
# base_url='http://hn216.api.yesapi.cn'
#请求app_key
# base_key='BE7FE3D8B276951BCBDDDB56C4D58479'
#请求数据
# args={
#     's':s,
#     'app_key':base_key,
#     'uuids':uuid1
# }

@ddt.ddt
class MultiProfile(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'MultiProfile.yaml'))
    def test_multiprofile(self,**payload):
        # self._testMethodDoc=payload.get('detail')
        base_url=payload.get('url') #获取url
        args=payload.get('data') #获取需要传递得参数

        resp=requests.get(url=base_url,params=args).text
        result=str(resp)
        #当用户不存在的时候，下面就是一个空列表
        # check='info_list=[]'
        check=payload.get('check')[0]
        print(check)
        self.assertIn(check,result)


if __name__ == '__main__':
    unittest.main()