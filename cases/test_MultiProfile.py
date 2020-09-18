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
        base_url=payload.get('url') #url
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


# #uuid数据
# UUid1='676003847A6FAF10908B6A6184A84B2C'
# Uuid2='3FE6E35B5A4DC896CB8034E2F08A1473'
# UUid3='4EC1E8184D8C377B2314EA327AD60354'
# s='App. User.MultiProfile'#请求ur
# base_url='http://hn216.api.yesapi.cn'#请求app_key
# base_key='BE7FE3D8B276951BCBDDDB56C4D58479'#请求数据
# args={
#     's':'App. User.MultiProfile',
#     'app_key':base_key,
#     'uuids':'676003847A6FAF10908B6A6184A84B2C' }
# re=requests.get(url='http://hn216.api.yesapi.cn',params=args)
# print(re.text)