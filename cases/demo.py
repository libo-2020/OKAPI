

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
