import hashlib
def hash_code(password):
    md5 = hashlib.md5()#获取MD5对象
    md5.update(password.encode('utf-8'))#将传入的密码编码后，更新MD5的状态
    return md5.hexdigest()#返回十六进制的MD5码
def set_res_data(res):
    if res:
        return res.lower().replace('":"','=').replace('":','=')