import requests

# 请求url地址
from setting import API_URL, API_KEY

base_url = API_URL

# 请求数据
data = {
    "s": "App.User.Profile",
    "app_key": API_KEY,
    "uuid": "631610AFD6B9C1F76A7E6D8BE7352FD2",
    "token": "EA8A16F633A4DBE3172BC8F96009112A85E172C8C62D64BB16F0A01C9013CEF7"
}

# 发送请求
re = requests.post(url=base_url, data=data)

# 响应结果
result = re.text
print(result)

