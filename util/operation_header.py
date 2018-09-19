# coding:utf-8
import requests
import json
from .operation_json import OperetionJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_url(self):
        '''
        获取登录返回的token的url
        '''
        url = self.response['data']['token']
        return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        print(cookie)
        op_json = OperetionJson()
        op_json.write_data(cookie)

    def write_header(self):
        header = self.get_response_url()
        headers = {
            "token": header
        }
        op_json = OperetionJson('../dataconfig/cookie.json')
        op_json.write_data(headers)


if __name__ == '__main__':
    url = "http://oa.jc-saas.com.cn/auth/login"
    data = {
        "work_number": "jc0001",
        "password": "123456"
    }
    res = json.dumps(requests.post(url, data).json())
    op_header = OperationHeader(res)
    op_header.write_header()
