
def set_res_data(resp):
    if resp:
        return resp.replace('":"','=').replace('":','=')
