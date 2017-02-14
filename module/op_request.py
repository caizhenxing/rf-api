#coding=utf-8
import requests
import json

class op_request(object):

    def __init__(self, request, request_body):
        self.request_url = request["host"] + request["url"]
        self.method = request["method"]
        self.protocol = request["protocol"]
        self.headers = request["headers"]
        self.request_body = request_body

    def print_self(self):
        print self.request_url
        print self.method
        print self.headers
        print self.protocol

    def send_request(self):
        if self.method == "post" and self.protocol == "http":
            re_dict = self.http_request_post()
        return re_dict

    def http_request_post(self):
        url = self.request_url
        request_body = self.request_body
        headers = self.headers

        session = requests.session()
        session.headers.update(headers)
        response = session.post(url, request_body)
        data = json.loads(response.content)
        re_dict ={}
        re_dict["data"] = data
        re_dict["status_code"] = response.status_code

        return re_dict


