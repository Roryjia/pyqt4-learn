# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'

import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle(u'例子')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
