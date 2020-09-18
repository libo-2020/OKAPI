"""测试工具函数"""
def str(resp):
    if resp:
        return resp.lower().replace('":"','=').replace('":','=')