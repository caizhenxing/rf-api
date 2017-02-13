#coding=utf-8
from module import xlsxEngine
import test
class main(object):


    def main(self, filename, kind):



        # f = open(r"D:\rf-api\caseManage\yqq\saveinfo.txt", "a+")
        #
        #
        # add = "case3\n    ${request}    create dictionary    host    http://yqq.emoney.cn    url    /myhome/saveinfo    method    post    header    \\    protocol    http\n    ${request_body}    create dictionary    UserId    26035    NickName    \xe7\x81\xb5\xe5\x84\xbf\xe7\x9a\x84\xe5\xae\x88\xe6\x8a\xa4    sex    \xe5\xa5\xb3    select_year    1921    select_month    2    select_day    1    prov    \xe5\x8c\x97\xe4\xba\xac    city    \xe4\xb8\x9c\xe5\x9f\x8e\xe5\x8c\xba    qq    1234567\n    ${judge_value}    create dictionary    ErrMessage    \xe4\xbf\x9d\xe5\xad\x98\xe6\x88\x90\xe5\x8a\x9f    HasError    FALSE    HRESULT    \\    ObjectValue    1\n    log    ${request}\n    log    ${request_body}\n    log    ${judge_value}\n    ${re_data}    judge_start    ${request}    ${request_body}    ${judge_value}\n    log    ${re_data}\n"
        # f.write(add)

        add = test.create_case()

        f = open(r"D:\rf-api\caseManage\yqq\saveinfo.txt", "a+")
        f.write(add)

        if kind == 1:
            op_xlsx = xlsxEngine.xlsxEngine_op("test2")
            op_xlsx.init_casesheet()

        if kind == 2:
            initPara = init_para.init_para()
            initPara.init_para(filename)

        if kind == 3:
            initJsonKey = init_json_key.get_json_key()
            initJsonKey.init_json_key(filename)

        if kind == 4:
            judgeValue = judge_value.judge_value()
            judgeValue.judge_start(filename)

if __name__=='__main__':
    test1 = main()
    test1.main("follow_test",0)