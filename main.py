#coding=utf-8
from module import xlsxEngine
from module import create_case
from module import robot_run
import sys
import getopt

def main(argv):
    init_para_file = ''
    create_robot_file = ''
    createfile = ''
    run_robot_file = ''
    all_run_fold = ''
    try:
        opts, args = getopt.getopt(argv, "hi:r:c:u:a:", ["init_para_file=", "create_robot_file=", "create=", "run=", "all_run="])
    except getopt.GetoptError:
        print 'test.py -i <init_para_file> -r <create_robot_file> -c <createfile> -u <robot_file>-a<project fold>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <init_para_file> -r <create_robot_file> -c <createfile> -u <robot_file>-a<project fold>'
            sys.exit()
        elif opt in ("-i", "--init_para_file"):
            init_para_file = arg
        elif opt in ("-r", "--create_robot_file"):
            create_robot_file = arg
        elif opt in ("-c", "--crfile"):
            createfile = arg
        elif opt in ("-u", "--robot_file"):
            run_robot_file = arg
        elif opt in ("-a", "--project fold"):
            all_run_fold = arg

    if createfile:
        op_xlsx = xlsxEngine.xlsxEngine_op(createfile)
        op_xlsx.create()

    if init_para_file:
        op_xlsx = xlsxEngine.xlsxEngine_op(init_para_file)
        op_xlsx.init_para()
        op_xlsx = xlsxEngine.xlsxEngine_op(init_para_file)
        op_xlsx.init_para()

    if create_robot_file:
        createCase = create_case.create_case(create_robot_file)
        createCase.create_case()

    if run_robot_file:
        robotRun = robot_run.robot_run(run_robot_file)
        robotRun.robot_run()

    if all_run_fold:
        allRun = robot_run.all_run(all_run_fold)
        allRun.all_run()

if __name__=='__main__':
    main(sys.argv[1:])
