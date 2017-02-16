# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QFileDialog


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

setting = QSettings("./QtPad.ini", QSettings.IniFormat)
execl_suffix = ".xlsx"
txt_suffix = ".txt"

class Ui_MainWindow(object):

    # def __init__(self):
    #     self.setting = QSettings("./QtPad.ini", QSettings.IniFormat)
    #     self.execl_suffix = ".xls"

    def setupUi(self, MainWindow):
        """
        主窗口的layout
        """
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # """
        # 切换界面按钮
        # """

        self.create_execl_botton = QtGui.QPushButton(MainWindow)
        self.create_execl_botton.setGeometry(QtCore.QRect(40, 40, 120, 40))
        self.create_execl_botton.setObjectName(_fromUtf8("pushButton"))

        self.init_para_botton = QtGui.QPushButton(MainWindow)
        self.init_para_botton.setGeometry(QtCore.QRect(200, 40, 120, 40))
        self.init_para_botton.setObjectName(_fromUtf8("pushButton"))

        self.create_robot_file_botton = QtGui.QPushButton(MainWindow)
        self.create_robot_file_botton.setGeometry(QtCore.QRect(360, 40, 120, 40))
        self.create_robot_file_botton.setObjectName(_fromUtf8("pushButton"))

        self.run_robot_file_botton = QtGui.QPushButton(MainWindow)
        self.run_robot_file_botton.setGeometry(QtCore.QRect(520, 40, 120, 40))
        self.run_robot_file_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 工作路径
        # """

        self.work_path_label = QtGui.QLabel(MainWindow)
        self.work_path_label.setGeometry(QtCore.QRect(40, 100, 60, 30))
        self.work_path_label.setObjectName(_fromUtf8("label"))

        self.path_label = QtGui.QLabel(MainWindow)
        self.path_label.setGeometry(QtCore.QRect(120, 100, 200, 30))
        self.path_label.setObjectName(_fromUtf8("label"))

        self.work_path_set_botton = QtGui.QPushButton(MainWindow)
        self.work_path_set_botton.setGeometry(QtCore.QRect(400, 100, 30, 30))
        self.work_path_set_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 第一个界面，创建execl文档
        # """

        self.create_execl_widget = QtGui.QFrame(MainWindow)
        self.create_execl_widget.setGeometry(QtCore.QRect(40, 140, 740, 200))
        self.create_execl_widget.setObjectName(_fromUtf8("frame"))
        self.create_execl_widget.setStyleSheet("QFrame{  border: 1px solid black;   }")

        self.create_execl_label = QtGui.QLabel(self.create_execl_widget)
        self.create_execl_label.setGeometry(QtCore.QRect(30, 20, 150, 30))
        self.create_execl_label.setObjectName(_fromUtf8("label"))

        self.create_execl_filename_label = QtGui.QLabel(self.create_execl_widget)
        self.create_execl_filename_label.setGeometry(QtCore.QRect(200, 20, 150, 30))
        self.create_execl_filename_label.setObjectName(_fromUtf8("label"))


        self.create_execl_edit_botton = QtGui.QPushButton(self.create_execl_widget)
        self.create_execl_edit_botton.setGeometry(QtCore.QRect(500, 20, 30, 30))
        self.create_execl_edit_botton.setObjectName(_fromUtf8("pushButton"))

        self.create_execl_run_botton = QtGui.QPushButton(self.create_execl_widget)
        self.create_execl_run_botton.setGeometry(QtCore.QRect(550, 20, 30, 30))
        self.create_execl_run_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 第二个界面，初始化para参数
        # """

        self.init_para_widget = QtGui.QFrame(MainWindow)
        self.init_para_widget.setGeometry(QtCore.QRect(40, 140, 740, 200))
        self.init_para_widget.setObjectName(_fromUtf8("frame"))
        self.init_para_widget.setStyleSheet("QFrame{  border: 1px solid black;   }")
        self.init_para_widget.hide()

        self.init_para_label = QtGui.QLabel(self.init_para_widget)
        self.init_para_label.setGeometry(QtCore.QRect(30, 20, 150, 30))
        self.init_para_label.setObjectName(_fromUtf8("label"))

        self.init_para_filename_label = QtGui.QLabel(self.init_para_widget)
        self.init_para_filename_label.setGeometry(QtCore.QRect(200, 20, 150, 30))
        self.init_para_filename_label.setObjectName(_fromUtf8("label"))


        self.init_para_edit_botton = QtGui.QPushButton(self.init_para_widget)
        self.init_para_edit_botton.setGeometry(QtCore.QRect(500, 20, 30, 30))
        self.init_para_edit_botton.setObjectName(_fromUtf8("pushButton"))

        self.init_para_run_botton = QtGui.QPushButton(self.init_para_widget)
        self.init_para_run_botton.setGeometry(QtCore.QRect(550, 20, 30, 30))
        self.init_para_run_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 第三个界面，制作robot文件
        # """

        self.create_robot_file_widget = QtGui.QFrame(MainWindow)
        self.create_robot_file_widget.setGeometry(QtCore.QRect(40, 140, 740, 200))
        self.create_robot_file_widget.setObjectName(_fromUtf8("frame"))
        self.create_robot_file_widget.setStyleSheet("QFrame{  border: 1px solid black;   }")
        self.create_robot_file_widget.hide()

        self.create_robot_label = QtGui.QLabel(self.create_robot_file_widget)
        self.create_robot_label.setGeometry(QtCore.QRect(30, 20, 150, 30))
        self.create_robot_label.setObjectName(_fromUtf8("label"))

        self.create_robot_filename_label = QtGui.QLabel(self.create_robot_file_widget)
        self.create_robot_filename_label.setGeometry(QtCore.QRect(200, 20, 150, 30))
        self.create_robot_filename_label.setObjectName(_fromUtf8("label"))


        self.create_robot_edit_botton = QtGui.QPushButton(self.create_robot_file_widget)
        self.create_robot_edit_botton.setGeometry(QtCore.QRect(500, 20, 30, 30))
        self.create_robot_edit_botton.setObjectName(_fromUtf8("pushButton"))

        self.create_robot_run_botton = QtGui.QPushButton(self.create_robot_file_widget)
        self.create_robot_run_botton.setGeometry(QtCore.QRect(550, 20, 30, 30))
        self.create_robot_run_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 第四个界面，执行robot文件
        # """

        self.run_robot_file_widget = QtGui.QFrame(MainWindow)
        self.run_robot_file_widget.setGeometry(QtCore.QRect(40, 140, 740, 200))
        self.run_robot_file_widget.setObjectName(_fromUtf8("frame"))
        self.run_robot_file_widget.setStyleSheet("QFrame{  border: 1px solid black;   }")
        self.run_robot_file_widget.hide()

        self.run_robot_label = QtGui.QLabel(self.run_robot_file_widget)
        self.run_robot_label.setGeometry(QtCore.QRect(30, 20, 150, 30))
        self.run_robot_label.setObjectName(_fromUtf8("label"))

        self.run_robot_filename_label = QtGui.QLabel(self.run_robot_file_widget)
        self.run_robot_filename_label.setGeometry(QtCore.QRect(200, 20, 150, 30))
        self.run_robot_filename_label.setObjectName(_fromUtf8("label"))


        self.run_robot_edit_botton = QtGui.QPushButton(self.run_robot_file_widget)
        self.run_robot_edit_botton.setGeometry(QtCore.QRect(500, 20, 30, 30))
        self.run_robot_edit_botton.setObjectName(_fromUtf8("pushButton"))

        self.run_robot_run_botton = QtGui.QPushButton(self.run_robot_file_widget)
        self.run_robot_run_botton.setGeometry(QtCore.QRect(550, 20, 30, 30))
        self.run_robot_run_botton.setObjectName(_fromUtf8("pushButton"))

        # """
        # 文本输出框
        # """
        self.textBrowser = QtGui.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(40, 350, 740, 130))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        # """"
        # 各种动作关联
        # """
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.work_path_set_botton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.work_path_setting)
        QtCore.QObject.connect(self.create_execl_botton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_create_execl_botton)
        QtCore.QObject.connect(self.init_para_botton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_init_para_botton)
        QtCore.QObject.connect(self.create_robot_file_botton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_create_robot_botton)
        QtCore.QObject.connect(self.run_robot_file_botton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_run_robot_botton)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "接口自动化测试", None))
        self.create_execl_botton.setText(u"创建execl界面")
        self.init_para_botton.setText(u"初始化参数界面")
        self.create_robot_file_botton.setText(u"生产robot文件界面")
        self.run_robot_file_botton.setText(u"运行robot文件界面")
        self.work_path_label.setText(u"工作路径：")
        path_label_text = setting.value("work_path").toPyObject()
        self.path_label.setText(path_label_text)
        self.work_path_set_botton.setText(u"...")


        self.create_execl_label.setText(u"需要创建的execl的文件名")
        create_execl_file_name = self.create_exexl_name()
        self.create_execl_filename_label.setText(create_execl_file_name)
        self.create_execl_edit_botton.setText(u"编辑")
        self.create_execl_run_botton.setText(u"创建")

        self.init_para_label.setText(u"初始化参数execl的文件名")
        init_para_execl_file_name = self.create_exexl_name()
        self.init_para_filename_label.setText(init_para_execl_file_name)
        self.init_para_edit_botton.setText(u"编辑")
        self.init_para_run_botton.setText(u"运行")

        self.create_robot_label.setText(u"生成脚本的execl文件名")
        create_robot_execl_file_name = self.create_exexl_name()
        self.create_robot_filename_label.setText(create_robot_execl_file_name)
        self.create_robot_edit_botton.setText(u"编辑")
        self.create_robot_run_botton.setText(u"运行")

        self.run_robot_label.setText(u"运行robot脚本名")
        run_robot_file_name = self.create_txt_name()
        self.run_robot_filename_label.setText(run_robot_file_name)
        self.run_robot_edit_botton.setText(u"编辑")
        self.run_robot_run_botton.setText(u"运行")


    def work_path_setting(self):
        absolute_path = QFileDialog.getExistingDirectory(directory=setting.value("work_path").toPyObject())
        if absolute_path:
            self.path_label.setText(absolute_path)
            setting.setValue("work_path", absolute_path)
            setting.sync()
        else:
            self.path_label.setText(setting.value("work_path").toPyObject())
        create_execl_file_name = self.create_exexl_name()
        run_robot_file_name = self.create_txt_name()
        self.create_execl_filename_label.setText(create_execl_file_name)
        self.init_para_filename_label.setText(create_execl_file_name)
        self.create_robot_filename_label.setText(create_execl_file_name)
        self.run_robot_filename_label.setText(run_robot_file_name)
        setting.setValue("create_execl_file_name", create_execl_file_name)
        setting.setValue("run_robot_file_name", run_robot_file_name)
        setting.sync

    def create_exexl_name(self):
        work_path = setting.value("work_path").toPyObject()
        work_path_list = os.path.split(str(work_path))
        re_data = work_path_list[-1] + execl_suffix
        return re_data

    def create_txt_name(self):
        work_path = setting.value("work_path").toPyObject()
        work_path_list = os.path.split(str(work_path))
        re_data = work_path_list[-1] + txt_suffix
        return re_data

    def click_create_execl_botton(self):
        self.create_execl_widget.show()
        self.init_para_widget.hide()
        self.create_robot_file_widget.hide()
        self.run_robot_file_widget.hide()

    def click_init_para_botton(self):
        self.create_execl_widget.hide()
        self.init_para_widget.show()
        self.create_robot_file_widget.hide()
        self.run_robot_file_widget.hide()

    def click_create_robot_botton(self):
        self.create_execl_widget.hide()
        self.init_para_widget.hide()
        self.create_robot_file_widget.show()
        self.run_robot_file_widget.hide()

    def click_run_robot_botton(self):
        self.create_execl_widget.hide()
        self.init_para_widget.hide()
        self.create_robot_file_widget.hide()
        self.run_robot_file_widget.show()






if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
