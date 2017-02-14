# -*- coding:utf-8 -*-
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def create_case():
    xlrd_object = xlrd.open_workbook("testcase.xlsx")
    xlrd_sheet = xlrd_object.sheet_by_name("work")
    case_id = xlrd_sheet.cell(6, 0).value
    host =  xlrd_sheet.cell(0, 0).value
    host_data = xlrd_sheet.cell(0, 1).value

    url = xlrd_sheet.cell(1, 0).value
    url_data = xlrd_sheet.cell(1, 1).value

    method = xlrd_sheet.cell(2, 0).value
    method_data = xlrd_sheet.cell(2, 1).value

    header = xlrd_sheet.cell(3, 0).value
    header_data = xlrd_sheet.cell(3, 1).value
    if not header_data:
        header_data = "\\"

    protocol = xlrd_sheet.cell(4, 0).value
    protocol_data = xlrd_sheet.cell(4, 1).value

    add = "case%s"%int(case_id) + "\n"
    add = add + r"    "
    add = add +r"${request}"
    add = add + r"    "
    add = add + r"create dictionary"
    add = add + r"    "
    add = add + "%s"%host
    add = add + r"    "
    add = add + "%s" % host_data
    add = add + r"    "
    add = add + "%s" % url
    add = add + r"    "
    add = add + "%s" % url_data
    add = add + r"    "
    add = add + "%s" % method
    add = add + r"    "
    add = add + "%s" % method_data
    add = add + r"    "
    add = add + "%s" % header
    add = add + r"    "
    add = add + "%s" % header_data
    add = add + r"    "
    add = add + "%s" % protocol
    add = add + r"    "
    add = add + "%s" % protocol_data
    add = add  + "\n"

    add = add + r"    "
    add = add + r"${request_body}"
    add = add + r"    "
    add = add + r"create dictionary"
    add = add + r"    "

    for i in range(1, 11):
        para = xlrd_sheet.cell(5, i).value
        value = xlrd_sheet.cell(6, i).value

        print type(value)

        add = add + "%s" %para
        add = add + r"    "
        add = add + "%s" %value
        add = add + r"    "
    add = add  + "\n"

    add = add + r"    "
    add = add + r"${judge_value}"
    add = add + r"    "
    add = add + r"create dictionary"
    add = add + r"    "

    for i in range(12, 16):
        para = xlrd_sheet.cell(5, i).value
        value = xlrd_sheet.cell(6, i).value
        if not value:
            value = "\\"

        add = add + "%s" % para
        add = add + r"    "
        add = add + "%s" % value
        add = add + r"    "
    add = add + "\n"

    add = add + r"    "
    add = add + r"log"
    add = add + r"    "
    add = add + r"${request}"
    add = add + "\n"

    add = add + r"    "
    add = add + r"log"
    add = add + r"    "
    add = add + r"${request_body}"
    add = add + "\n"

    add = add + r"    "
    add = add + r"log"
    add = add + r"    "
    add = add + r"${judge_value}"
    add = add + "\n"

    add = add + r"    "
    add = add + r"${re_data}"
    add = add + r"    "
    add = add + r"judge_start"
    add = add + r"    "
    add = add + r"${request}"
    add = add + r"    "
    add = add + r"${request_body}"
    add = add + r"    "
    add = add + r"${judge_value}"
    add = add + "\n"

    add = add + r"    "
    add = add + r"log"
    add = add + r"    "
    add = add + r"${re_data}"
    add = add + "\n"



    print add

    return add
