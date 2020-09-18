import hashlib


def hash_code(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 返回的报文是json格式的，利用字符替换让数据变成"a=1,b=2"的格式
def set_res_data(res):
    if res:
        return res.lower().replace('":"', '=').replace('":', '=')
