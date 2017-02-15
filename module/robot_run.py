# -*- coding:utf-8 -*-
import string
import os

class robot_run(object):

    def __init__(self, file):
        self.file = file

    def print_run(self):
        print self.file

    def robot_run(self):
        file_path = os.path.dirname(self.file)

        content = "--outputdir"+"\n" + file_path +r"\report" +"\n"+ "-C" +"\n"+ "off" +"\n"+ "-W" +"\n"+ "168"
        filename = file_path + r"\argfile.txt"

        fp = open(filename, "w")
        fp.write(content)

        if not os.path.exists(file_path + r"\report"):
            os.makedirs(file_path + r"\report")

        cmd = r"pybot.bat --argumentfile %s\argfile.txt --listener D:\Python27\lib\site-packages\robotide\contrib\testrunner\TestRunnerAgent.py:61683:False %s"%(file_path, file_path)

        os.chdir(file_path + r"\report")
        os.system(cmd)

class all_run(object):

    def __init__(self, fold):
        self.fold = fold

    def all_run(self):
        file_path = self.fold
        content = "--outputdir" + "\n" + file_path + r"\report" + "\n" + "-C" + "\n" + "off" + "\n" + "-W" + "\n" + "168"
        filename = file_path + r"\argfile.txt"

        fp = open(filename, "w")
        fp.write(content)

        if not os.path.exists(file_path + r"\report"):
            os.makedirs(file_path + r"\report")

        cmd = r"pybot.bat --argumentfile %s\argfile.txt --listener D:\Python27\lib\site-packages\robotide\contrib\testrunner\TestRunnerAgent.py:61683:False %s"%(file_path, file_path)

        os.chdir(file_path + r"\report")
        os.system(cmd)