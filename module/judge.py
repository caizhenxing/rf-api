#coding=utf-8
import requests
import json
import string
import op_request
import antpedia
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class judge(object):
    antpediaJson = antpedia.antpedia_json()

    def judge_start(self, request, request_body, judge_value, set_judge):
        opRequest = op_request.op_request(request, request_body)
        dict_response_data = opRequest.http_request_post()

        response_data = dict_response_data["data"]
        response_status = dict_response_data["status_code"]

        data = self.judge_data(judge_value, response_data, set_judge)
        data["response_status"] = response_status
        return data

    def judge_data(self, judge_value, response_data, set_judge):
        re_dict ={}
        judge_flag = True
        error_list =[]
        for json_key in judge_value:
            kind = set_judge[json_key][2]
            re_data = self.antpediaJson.antpedia_json(response_data,json_key)
            judge_data = judge_value[json_key]


            if kind == "str":
                re_data = str(re_data)
                judge_data = str(judge_data)

            if kind == "int":
                temp = string.splitfields(judge_data,".")
                print temp
                re_data = int(re_data)
                judge_data = int(temp[0])

            if kind == "bool":
                re_data = bool(re_data)
                judge_data = bool(judge_data)

            if kind == "none":
                if not judge_data:
                    re_data = True
                    judge_data =True

            if cmp(re_data, judge_data) != 0:
                judge_flag = False
                judge_log = u"error message:json_para is %r,expected value is %r,return value is %r"%(json_key,judge_data,re_data)
                error_list.append(judge_log)
        re_dict["judge_flag"] = judge_flag
        re_dict["error_list"] = error_list
        return re_dict



            # print judge_data
            # print type(judge_data)
            # print jdata
            # print type(jdata)
            # print "----------------"
            # print cmp (judge_data, jdata)
            # print "---------------"

