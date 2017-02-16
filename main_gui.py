# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from threads import create_execl_Thread
from threads import init_para_Thread
from threads import create_robot_Thread
from threads import run_robot_Thread
from gui import Ui_MainWindow
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MyDialog(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

        self.create_execl_run_botton.clicked.connect(self.create_execl_run)
        self.init_para_run_botton.clicked.connect(self.init_para_run)
        self.create_robot_run_botton.clicked.connect(self.create_robot_run)
        self.run_robot_run_botton.clicked.connect(self.run_robot)

    def create_execl_run(self):
        self.textBrowser.clear()
        self.create_execl_thread = create_execl_Thread()
        self.create_execl_thread.trigger.connect(self.update_text)
        self.create_execl_thread.start()

    def init_para_run(self):
        self.textBrowser.clear()
        self.init_para_thread = init_para_Thread()
        self.init_para_thread.trigger.connect(self.update_text)
        self.init_para_thread.start()

    def create_robot_run(self):
        self.textBrowser.clear()
        self.create_robot_thread = create_robot_Thread()
        self.create_robot_thread.trigger.connect(self.update_text)
        self.create_robot_thread.start()

    def run_robot(self):
        self.textBrowser.clear()
        self.run_robot_thread = run_robot_Thread()
        self.run_robot_thread.trigger.connect(self.update_text)
        self.run_robot_thread.start()

    def update_text(self, message):
        self.textBrowser.insertPlainText(message)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = MyDialog()
    Dialog.show()
    sys.exit(app.exec_())