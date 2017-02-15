#coding=utf-8
from module import xlsxEngine
from module import create_case
import sys
import getopt



def main(argv):
    print "a"
    init_para_file = ''
    create_robot_file = ''
    createfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:r:c:", ["init_para_file=", "create_robot_file=","create="])
    except getopt.GetoptError:
        print 'test.py -i <init_para_file> -r <create_robot_file> -c <createfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <init_para_file> -r <create_robot_file> -c <createfile>'
            sys.exit()
        elif opt in ("-i", "--init_para_file"):
            init_para_file = arg
        elif opt in ("-r", "--create_robot_file"):
            create_robot_file = arg
        elif opt in ("-c", "--crfile"):
            createfile = arg

    if createfile:
        op_xlsx = xlsxEngine.xlsxEngine_op(createfile)
        op_xlsx.create()
    #
    if init_para_file:
        op_xlsx = xlsxEngine.xlsxEngine_op(init_para_file)
        op_xlsx.init_para()

    if create_robot_file:
        createCase = create_case.create_case(create_robot_file)
        createCase.create_case()
    #
    # if kind == 4:
    #     judgeValue = judge_value.judge_value()
    #     judgeValue.judge_start(filename)

if __name__=='__main__':
    main(sys.argv[1:])
