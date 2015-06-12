# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'

import sys
from PyQt4 import QtGui

class Example2(QtGui.QWidget):

    def __init__(self):
        super(QtGui.QWidget, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('LYF')
        self.setWindowIcon(QtGui.QIcon('L1.jpg'))

        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()