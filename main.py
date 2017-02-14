#coding=utf-8
from module import xlsxEngine
from module import create_case
class main(object):


    def main(self, filename, kind):

        if kind == 1:
            op_xlsx = xlsxEngine.xlsxEngine_op("test")
            op_xlsx.create()

        if kind == 2:
            op_xlsx = xlsxEngine.xlsxEngine_op("test")
            op_xlsx.init_para()

        if kind == 3:
            createCase = create_case.create_case("test")
            createCase.create_case()

        if kind == 4:
            judgeValue = judge_value.judge_value()
            judgeValue.judge_start(filename)

if __name__=='__main__':
    test = main()
    test.main("follow_test",3)