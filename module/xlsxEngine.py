# -*- coding:utf-8 -*-
import xlrd
import xlsxwriter
import os

class xlsxEngine_rd(object):

    def __init__(self, file):
        self.xlsx_name = file
        self.xlrd_object = None
        self.xlsx_object = None
        self.isopenfailed = True

    def xlrd_open(self):
        try:
            self.xlrd_object = xlrd.open_workbook(self.xlsx_name)
            self.isopenfailed = False
        except Exception,e:
            self.isopenfailed = True
            self.xlrd_object = None
            print e
        finally:
            pass
        return [self.isopenfailed, self.xlrd_object]

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
        if os.path.exists(self.xlsx_name+".xlsx"):
            self.xlrd_object = xlrd.open_workbook(self.xlsx_name+".xlsx")
        else:
            self.xlrd_object = None
        self.xlsx_object = xlsxwriter.Workbook(self.xlsx_name+".xlsx")
        self.isopenfailed = True

    def create(self):
        try:
            # self.xlsx_object = xlsxwriter.Workbook(self.xlsx_name + ".xlsx")
            self.xlsx_sheet = self.xlsx_object.add_worksheet("para")
            self.xlsx_sheet.write(0, 0, "Host")
            self.xlsx_sheet.write(1, 0, "Url")
            self.xlsx_sheet.write(2, 0, "Method")
            self.xlsx_sheet.write(3, 0, "Protocol")
            self.xlsx_sheet.write(4, 0, "Headers")
            self.xlsx_sheet.write(6, 0, "cookie")
            self.xlsx_sheet.write(8, 0, "Request_body")
            self.xlsx_sheet.write(8, 1, "body_key")
            self.xlsx_sheet.write(9, 1, "body_value")
            self.xlsx_object.close()
            self.isopenfailed = False
        except Exception, e:
            print e

    def init_casesheet(self):

        if not self.xlrd_object:
            print "write para in %s"%self.xlsx_name
        else:
            self.init_case()
            self.init_json()

    def init_case(self):
        print "init_case"

    def init_json(self):
        print "init_json"

