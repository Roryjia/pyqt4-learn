# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
#

__author__ = 'rory'

import os
import sys

from PyQt4 import QtGui

class Example1(QtGui.QMainWindow):

    def __init__(self):
        super(Example1, self).__init__()

        self.initUI()

    def initUI(self):
        # 调用状态栏显示消息
        self.statusBar().showMessage('Ready....')

        # 调用菜单栏
        self.initMenu()

        self.setGeometry(300, 300, 600, 450)
        self.setWindowTitle(u'主窗体')

        self.show()

    def initMenu(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        # 用于退出
        fileMenu.addAction(self.actionExist())
        # 用于打开文件对话框
        fileMenu.addAction(self.actionOpen())

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.actionExist())

    def actionExist(self):
        exitAction = QtGui.QAction(QtGui.QIcon('../first/L1.jpg'), '&Exist', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setToolTip('Exit application')
        exitAction.triggered.connect(QtGui.QApplication.quit)
        return exitAction

    def actionOpen(self):
        exitAction = QtGui.QAction(QtGui.QIcon('../first/L2.jpg'), '&Open', self)
        exitAction.setShortcut('Ctrl+N')
        exitAction.setToolTip('Open File')
        exitAction.triggered.connect(self.openFile)
        return exitAction

    def openFile(self):
        qf = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '~')
        self.textEdit.clear()
        # 会得到当前选择的文件全路径
        print qf, type(qf)

        with open(qf) as f:
            self.textEdit.append(f.read())

        self.statusBar().showMessage(u'打开了一个文件 {}'.format(os.path.basename(str(qf))))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()