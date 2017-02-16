# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import QSettings
from module.gui import Ui_MainWindow
import sys
setting = QSettings("./QtPad.ini", QSettings.IniFormat)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MyDialog(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = MyDialog()
    Dialog.show()
    sys.exit(app.exec_())