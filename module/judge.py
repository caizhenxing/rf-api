#coding=utf-8
import requests
import json
import op_request
import antpedia

class judge(object):
    antpediaJson = antpedia.antpedia_json()

    def judge_start(self, request, request_body, judge_value):
        opRequest = op_request.op_request(request, request_body)
        dict_response_data = opRequest.http_request_post()

        response_data = dict_response_data["data"]
        response_status = dict_response_data["status_code"]

        self.judge_data(judge_value, response_data)
        return "re_data"

    def judge_data(self, judge_value, response_data):
        print response_data

        for json_key in judge_value:
            jdata = self.antpediaJson.antpedia_json(response_data,json_key)
            judge_data = judge_value[json_key]
            print judge_data
            print type(judge_data)
            print jdata
            print type(jdata)
            print "----------------"
            print cmp (judge_data, jdata)
            print "---------------"



# request = {u'host': u'http://yqq.emoney.cn', u'url': u'/myhome/saveinfo', u'method': u'post', u'protocol': u'http', u'header': '',}
# request_body = {u'UserId': u'26035', u'NickName': u'\u7075\u513f\u7684\u5b88\u62a4', u'sex': u'\u5973', u'select_year': u'1921', u'select_month': u'2', u'select_day': u'1', u'prov': u'\u5317\u4eac', u'city': u'\u4e1c\u57ce\u533a', u'qq': u'1234567'}
# judge_value = {u'ErrMessage': u'\u4fdd\u5b58\u6210\u529f', u'HasError': u'FALSE', u'HRESULT': '', u'ObjectValue': u'1'}
#
# a = judge()
# a.judge_start(request, request_body ,judge_value)