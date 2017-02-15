# -*- coding:utf-8 -*-
import xlrd
import xlsxwriter
import recursive
import os
import op_request

class xlsxEngine_rd(object):

    def __init__(self, file):
        self.xlsx_name = file
        self.xlrd_object = None
        self.xlsx_object = None
        self.isopenfailed = True

    def xlrd_open(self):
        try:
            self.xlrd_object = xlrd.open_workbook(self.xlsx_name)
            self.para_sheet = self.xlrd_object.sheet_by_name("para")
            self.case_sheet = self.xlrd_object.sheet_by_name("case")
            self.isopenfailed = False
        except Exception,e:
            self.isopenfailed = True
            self.xlrd_object = None
            print e
        finally:
            pass
        return [self.isopenfailed, self.xlrd_object, self.para_sheet, self.case_sheet]

    def cell_pos(self,sheet, target):
        try:
            re_dict = {}
            flag = True
            for row in range(0, sheet.nrows):
                if flag:
                    for col in range(0, sheet.ncols):
                        if sheet.cell(row, col).value == target:
                            re_dict["row"] = row
                            re_dict["col"] = col
                            flag == False
                            break
                else:
                    break
        except Exception,e:
            print "error at xlsxEngine_op -> cell_post"

        return re_dict



class xlsxEngine_wt(object):

    def __init__(self, file):
        self.xlsx_name = file
        self.xlsx_object = None
        self.xlsx_sheet = None
        self.isopenfailed = True

    def open(self):
        try:
            self.xlsx_object = xlsxwriter.Workbook(self.xlsx_name+".xlsx")
            self.isopenfailed = False
        except Exception, e:
            print e

class xlsxEngine_op(object):

    def __init__(self, file):
        self.xlsx_name = file
        if os.path.exists(self.xlsx_name+".xls"):
            self.xlrd_object = xlrd.open_workbook(self.xlsx_name+".xls")
        else:
            self.xlrd_object = None
        self.xlsx_object = xlsxwriter.Workbook(self.xlsx_name+".xls")
        self.isopenfailed = True

    def create(self):
        try:
            self.xlsx_object = xlsxwriter.Workbook(self.xlsx_name + ".xls")
            self.xlsx_sheet = self.xlsx_object.add_worksheet("para")
            self.xlsx_sheet.write(0, 0, "host")
            self.xlsx_sheet.write(1, 0, "url")
            self.xlsx_sheet.write(2, 0, "method")
            self.xlsx_sheet.write(3, 0, "protocol")
            self.xlsx_sheet.write(4, 0, "headers")
            self.xlsx_sheet.write(6, 0, "cookie")
            self.xlsx_sheet.write(8, 0, "request_body")
            self.xlsx_sheet.write(8, 1, "body_key")
            self.xlsx_sheet.write(9, 1, "body_value")
            self.xlsx_object.close()
            self.isopenfailed = False
        except Exception, e:
            print "error at xlsxEngine_op ->create"

    def init_para(self):
        try:
            xlrd_sheet = self.xlrd_object.sheet_by_name("para")
            xlsx_para_sheet = self.xlsx_object.add_worksheet("para")
            self.copy_execl_sheet(xlrd_sheet, xlsx_para_sheet)
            xlsx_case_sheet = self.xlsx_object.add_worksheet("case")

        except Exception, e:
            print "error at xlsxEngine_op -> init_para_try1"

        para_list = self.para_list(xlrd_sheet)
        values = [[] for i in range(len(para_list))]

        xlsx_case_sheet.write(0, 0, "judge_logic")
        xlsx_case_sheet.write(1, 0, "judge_env")
        xlsx_case_sheet.write(2, 0, "key_kind")
        xlsx_case_sheet.write(3, 0, "case_Id")


        for i in range(0, len(para_list), 1):
            pos = self.cell_post(xlrd_sheet, para_list[i])
            row = pos["row"]
            col = pos["col"]
            for x in range(row + 1, xlrd_sheet.nrows, 1):
                if xlrd_sheet.cell(x, col).value:
                    add_para = self.charge_to_str(xlrd_sheet.cell(x, col).value)
                    values[i].append(add_para)

        for i in range(1, len(para_list)+1, 1):
            xlsx_case_sheet.write(3, i, para_list[i-1])

        xlsx_case_sheet.write(3, len(para_list)+1, "Judgement")

        templist = []
        all_List = recursive.createTestCase(values, templist, len(values))

        index = 0
        for case_para in all_List:
            xlsx_case_sheet.write(index+4, 0, index+1)
            list.reverse(case_para)
            y = 0
            for x in case_para:
                xlsx_case_sheet.write(index+4, y+1, x)
                y += 1
            index += 1

        request = {}
        request_body = {}

        request["host"] = xlrd_sheet.cell(0, 1).value
        request["url"] = xlrd_sheet.cell(1, 1).value
        request["method"] = xlrd_sheet.cell(2, 1).value
        request["protocol"] = xlrd_sheet.cell(3, 1).value
        request["headers"] = xlrd_sheet.cell(4, 1).value

        try:
            for i in range(0, len(para_list), 1):
                request_body[para_list[i]] = all_List[0][i]
        except Exception, e:
            print "no para"

        opRequest = op_request.op_request(request, request_body)
        re_dict = opRequest.send_request()

        url1 = "1"
        json_key_list = recursive.json_key(re_dict["data"], url1)
        json_key_col = len(para_list) + 2
        for json_key in json_key_list:
            xlsx_case_sheet.write(3, json_key_col, json_key)
            json_key_col += 1

        self.xlsx_object.close()

    def copy_execl_sheet(self, source_sheet, target_sheet):
        try:
            for row in range(0, source_sheet.nrows):
                for col in range(0, source_sheet.ncols):
                    target_sheet.write(row, col, source_sheet.cell(row, col).value)
        except Exception, e:
            print "error at xlsxEngine_op -> copy execl sheet"

    def para_list(self, sheet):
        para_list = []
        try:
            request_body_pos = self.cell_post(sheet, "request_body")
            for x in range(request_body_pos["col"] + 1, sheet.ncols):
                para_list.append(sheet.cell(request_body_pos["row"], x).value)
        except Exception,e:
            print "error at xlsxEngine_op -> para_list"

        return para_list

    def cell_post(self, sheet, target):
        try:
            re_dict = {}
            flag = True
            for row in range(0, sheet.nrows):
                if flag:
                    for col in range(0, sheet.ncols):
                        if sheet.cell(row, col).value == target:
                            re_dict["row"] = row
                            re_dict["col"] = col
                            flag == False
                            break
                else:
                    break
        except Exception,e:
            print "error at xlsxEngine_op -> cell_post"

        return re_dict

    def charge_to_str(self, value):
        re_data =value
        if isinstance(value, (float)):
            re_data = str(int(value))
        return re_data





