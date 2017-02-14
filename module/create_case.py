# -*- coding:utf-8 -*-
import xlsxEngine
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class create_case(object):

    def __init__(self, file):
        self.xlsx_rd = xlsxEngine.xlsxEngine_rd(file+".xlsx")
        self.xlrd_open = self.xlsx_rd.xlrd_open()
        self.para_sheet = self.xlrd_open[2]
        self.case_sheet = self.xlrd_open[3]

    def print_value(self):
        print self.para_sheet.cell(0, 0).value
        print self.case_sheet.cell(0, 0).value

    def create_case(self):
        fp = open(r"D:\rf-api\caseManage\yqq\text.txt", "w")
        content = "*** Settings ***"+ "\n"
        content = content + "Library           Collections"+ "\n"
        content = content + "Library           ../../module/judge.py" + "\n"
        content = content + "\n"
        content = content + "*** Test Cases ***" + "\n"

        case_Id_pos = self.xlsx_rd.cell_pos(self.case_sheet, "case_Id")
        Judgement_pos = self.xlsx_rd.cell_pos(self.case_sheet, "Judgement")



        for x in range(case_Id_pos["row"]+1, self.case_sheet.nrows, 1):
            content = content + "case%s" % int(self.case_sheet.cell(x, 0).value) + "\n"
            content = content + r"    "
            content = content + r"${request}"
            content = content + r"    "
            content = content + r"set_request"+ "\n"

            content = content + r"    "
            content = content + r"${set_judge}"
            content = content + r"    "
            content = content + r"set_judge"+ "\n"



            content = content + r"    "
            content = content + r"${request_body}"
            content = content + r"    "
            content = content + r"create dictionary"
            content = content + r"    "
            for y in range(case_Id_pos["col"]+1, Judgement_pos["col"], 1):
                para = self.case_sheet.cell(3, y).value
                value = self.case_sheet.cell(x, y).value
                if not value:
                    value = "\\"
                content = content + "%s" % para
                content = content + r"    "
                content = content + "%s" % value
                content = content + r"    "
            content = content + "\n"

            content = content + r"    "
            content = content + r"${judge_value}"
            content = content + r"    "
            content = content + r"create dictionary"
            content = content + r"    "

            for y in range(Judgement_pos["col"]+1, self.case_sheet.ncols, 1):
                para = self.case_sheet.cell(3, y).value
                value = self.case_sheet.cell(x, y).value
                if not value:
                    value = "\\"
                content = content + "%s" % para
                content = content + r"    "
                content = content + "%s" % value
                content = content + r"    "
            content = content + "\n"

            content = content + r"    "
            content = content + r"log"
            content = content + r"    "
            content = content + r"${request}"
            content = content + "\n"

            content = content + r"    "
            content = content + r"log"
            content = content + r"    "
            content = content + r"${request_body}"
            content = content + "\n"

            content = content + r"    "
            content = content + r"log"
            content = content + r"    "
            content = content + r"${judge_value}"
            content = content + "\n"

            content = content + r"    "
            content = content + r"${re_data}"
            content = content + r"    "
            content = content + r"judge_start"
            content = content + r"    "
            content = content + r"${request}"
            content = content + r"    "
            content = content + r"${request_body}"
            content = content + r"    "
            content = content + r"${judge_value}"
            content = content + r"    "
            content = content + r"${set_judge}"
            content = content + "\n"

            content = content + r"    "
            content = content + r"log"
            content = content + r"    "
            content = content + r"${re_data}"
            content = content + "\n"

        content = content + "*** Keywords ***"+ "\n"
        content = content + "set_request" + "\n"
        content = content + r"    "
        content = content + r"${request}"
        content = content + r"    "
        content = content + r"create dictionary"
        content = content + r"    "

        for i in range(0, 5, 1):
            para = self.para_sheet.cell(i, 0).value
            value = self.para_sheet.cell(i, 1).value
            if not value:
                value = "\\"
            content = content + "%s" % para
            content = content + r"    "
            content = content + "%s" % value
            content = content + r"    "
        content = content + "\n"
        content = content + r"    "
        content = content + r"[Return]"
        content = content + r"    "
        content = content + r"${request}"+ "\n"

        content = content + "set_judge" + "\n"


        for y in range(Judgement_pos["col"] + 1, self.case_sheet.ncols, 1):
            judge_logic = self.case_sheet.cell(0, y).value
            judge_env = self.case_sheet.cell(1, y).value
            key_kind = self.case_sheet.cell(2, y).value
            json_key = self.case_sheet.cell(3, y).value
            if not judge_logic:
                judge_logic = "\\"
            if not judge_env:
                judge_env = "\\"
            if not key_kind:
                key_kind = "\\"
            if not json_key:
                json_key = "\\"

            content = content + r"    "
            content = content + "@{%s}" % json_key
            content = content + r"    "
            content = content + r"create list"
            content = content + r"    "
            content = content + "%s" % judge_logic
            content = content + r"    "
            content = content + "%s" % judge_env
            content = content + r"    "
            content = content + "%s" % key_kind+ "\n"

        content = content + r"    "
        content = content + r"&{judge}"
        content = content + r"    "
        content = content + r"create dictionary"
        content = content + r"    "

        for y in range(Judgement_pos["col"] + 1, self.case_sheet.ncols, 1):
            json_key = self.case_sheet.cell(3, y).value
            if not json_key:
                json_key = "\\"
            content = content + "%s=@{%s}" % (json_key,json_key)
            content = content + r"    "


        content = content + "\n"
        content = content + r"    "
        content = content + r"[Return]"
        content = content + r"    "
        content = content + r"&{judge}"+ "\n"


        fp.write(content)