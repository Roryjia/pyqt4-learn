# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'

import sys

from PyQt4 import QtGui


class Example4(QtGui.QWidget):

    def __init__(self):
        super(Example4 , self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u'消息盒子')

        # 屏幕剧中
        self.show()

    def closeEvent(self, event):
        replay = QtGui.QMessageBox.question(self, 'Message', 'Area sure to quit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if replay == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget.availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example4()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()