import base64
import requests
import re
API_KEY = "1aRCaG2POWpVFOZvpmzzxNzF"
SECRET_KEY = "7ZpEbZrxMeluMaOAqAtZtjOExoO23lgj"


def getocrvalue(imgbase64):
    imagbase = re.search('base64,(.*)', imgbase64)
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()
    # 这里要修该为解析或者网址，反正是由函数获得
    img = imagbase.group(1)
    params = {"image": img}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    # 这里返回的数据类型不是str或者json,尝试过转换利用正则或分割自符串后失败
    response = requests.request("POST", url, headers=headers, data=params).json()
    words = response["words_result"][0]["words"]
    # 这里是对words进行去除等于号和计算结果
    words = words[0:len(words) - 1]
    res = eval(words)
    return str(res)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# 转换为二进制文件
#def get_file_as_base64(path):
    #f = open(path, 'rb')
    #image = base64.b64encode(f.read())
    #return image


