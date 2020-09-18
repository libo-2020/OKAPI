
import unittest
import  requests
from lib.utils import *


url = 'http://hn216.api.yesapi.cn/'
class Check(unittest.TestCase):
    def test_check(self):

        data ={
            's':'App.User.Check',
            'app_key':'5CBB0F0AC8CCFC7032F5023CD7BE9F79',
            'uuid':'ACAA725AF687A45CB6769EDF6EBF647B',
            'token':'A47F9757FDB97FBDF18557994BA93103D2222092C2A96C6EA8F20BAF9202EF2C'
        }

        res = requests.post(url=url,data=data)
        print(res)
        resp = res.text
        print(res.text)
        results = set_res_data(resp)
        print(results)
        check = ['ret=200','err_code=0','"err_msg="']
        for c in check:
            self.assertIn(c,results)


    def test_check1(self):

        data ={
            's':'App.User.Check',
            'app_key':'5CBB0F0AC8CCFC7032F5023CD7BE9F',
            'uuid':'ACAA725AF687A45CB6769EDF6EBF647B',
            'token':'A47F9757FDB97FBDF18557994BA93103D2222092C2A96C6EA8F20BAF9202EF2C'
        }

        res = requests.post(url=url,data=data)
        print(res)
        resp = res.text
        print(res.text)
        results = set_res_data(resp)
        print(results)
        check = ['ret=400']
        for c in check:
            self.assertIn(c,results)


if __name__ == '__main__':
    unittest.main()
