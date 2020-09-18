import unittest
from setting import DATA_PATH
import ddt
import requests
import os
@ddt.ddt
class OtherProfile(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'otherprofile.yaml'))
    def test_other_profile(self,**payload):
        url=payload.get('url')
        data=payload.get('data')

        response=requests.get(url=url,params=data)
        print(response.text)
        return response.text

# url='http://hn216.api.yesapi.cn/'
# data={
#     's':'App.User.OtherProfile',
#     'app_key':'C934E82FEE5E64FC9035E3315BA667AC',
#     # 'uuid':'pass',
#     # 'token':'pass',
#     'other_uuid':'321286992C1DE8FBC1493BE1715D6ADE'
# }
# response=requests.get(url=url,params=data)
# response.json()
# re=response.text





if __name__ == '__main__':
    unittest.main()


