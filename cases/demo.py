# 请求url地址
import requests

url='http://hn216.api.yesapi.cn/'

# 传入请求数据
data={

    's':'App.User.Check',
    'app_key':'5CBB0F0AC8CCFC7032F5023CD7BE9F79',
    'uuid':'ACAA725AF687A45CB6769EDF6EBF647B',
    'token':'A47F9757FDB97FBDF18557994BA93103D2222092C2A96C6EA8F20BAF9202EF2C'
}
# 发送请求
re = requests.post(url=url,params=data)
# 响应结果
result = re.text
print(result)

#url
import requests
base_url = 'http://hn216.api.yesapi.cn/'
#数据
data = {
    's':'App.User.LogoutAll',
    'app_key':'4F476813EC222132D61351A3AA1D159B',
    'uuid':'FB4AD526480098811795BF3D0F2E97AF'
}
#发送请求
re=requests.get(url=base_url,params=data)
#re=requests.post(url=base_url,data=data)

#返回响应信息
result=re.text
print(result)
