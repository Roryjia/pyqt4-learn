# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'

import sys

from PyQt4 import QtGui


class Example1(QtGui.QWidget):

    def __init__(self):
        super(Example1, self).__init__()

        self.initUI()

    def initUI(self):
        okButton = QtGui.QPushButton('OK')
        cancelButton = QtGui.QPushButton('CANCEL')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle(u'LayLout')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()