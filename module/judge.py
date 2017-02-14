#coding=utf-8
import requests
import json
import op_request
import antpedia

class judge(object):
    antpediaJson = antpedia.antpedia_json()

    def judge_start(self, request, request_body, judge_value, set_judge):
        opRequest = op_request.op_request(request, request_body)
        dict_response_data = opRequest.http_request_post()

        response_data = dict_response_data["data"]
        response_status = dict_response_data["status_code"]

        self.judge_data(judge_value, response_data, set_judge)
        return response_status

    def judge_data(self, judge_value, response_data, set_judge):
        print response_data
        for x in  set_judge:
            print set_judge[x]
            print set_judge[x][1]
            print "---------------"

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

