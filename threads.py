# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from module import xlsxEngine
from module import create_case
from module import robot_run
from PyQt4.QtCore import QSettings
import time
import os
import sys
import gc


reload(sys)
sys.setdefaultencoding('utf-8')
setting = QSettings("./QtPad.ini", QSettings.IniFormat)

class create_execl_Thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(create_execl_Thread, self).__init__(parent)

    def run(self):
        filename = str(setting.value("create_execl_file_name").toPyObject())
        work_path = str(setting.value("work_path").toPyObject())
        full_filename = work_path+"\\"+filename
        self.trigger.emit(u"文件%s正在创建中" % full_filename + "\n")
        op_xlsx1 = xlsxEngine.xlsxEngine_op(full_filename)
        op_xlsx1.create()
        self.trigger.emit(u"文件%s创建完成"%full_filename)

class init_para_Thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(init_para_Thread, self).__init__(parent)

    def run(self):
        filename = str(setting.value("create_execl_file_name").toPyObject())
        work_path = str(setting.value("work_path").toPyObject())
        full_filename = work_path+"\\"+filename
        self.trigger.emit(u"文件%s正在初始化参数中" % full_filename + "\n")
        try:
            op_xlsx = xlsxEngine.xlsxEngine_op(full_filename)
            op_xlsx.init_para()
        finally:
        # print sys.getrefcount(op_xlsx)
            del op_xlsx
            gc.collect()
        # cmd = r"python d:\rf-api\main.py -i d:\yqq\sample\sample.xlsx"
        # os.system(cmd)

        self.trigger.emit(u"文件%s初始化参数完成"%full_filename)

class create_robot_Thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(create_robot_Thread, self).__init__(parent)

    def run(self):
        filename = str(setting.value("create_execl_file_name").toPyObject())
        work_path = str(setting.value("work_path").toPyObject())
        full_filename = work_path+"\\"+filename
        self.trigger.emit(u"robot文件正在生成中" + "\n")
        createCase = create_case.create_case(full_filename)
        createCase.create_case()
        self.trigger.emit(u"robot文件生成完成")

class run_robot_Thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(run_robot_Thread, self).__init__(parent)

    def run(self):
        filename = str(setting.value("run_robot_file_name").toPyObject())
        work_path = str(setting.value("work_path").toPyObject())


        full_filename = work_path+"\\"+filename
        self.trigger.emit(u"正在执行用例，请稍等"+ "\n")
        robotRun = robot_run.robot_run(full_filename)
        robotRun.robot_run()
        self.trigger.emit(u"用例全部执行完成，可以查看报告了")
