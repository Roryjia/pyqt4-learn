# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-10, by rory
# 
# 

__author__ = 'rory'

import sys

from PyQt4 import QtGui, QtCore


class Communicate(QtCore.QObject):

    closeAPP = QtCore.pyqtSignal()


class BasePushButton(QtGui.QPushButton):

    def __init__(self, type, *args):
        # self.type = type
        super(BasePushButton, self).__init__(*args)
        # self.clicked.connect(getattr(self, self.type))
        self.clicked.connect(self.ShowStatusBar)

    def ShowStatusBar(self):
        sender = self.parent().sender()
        self.parent().statusBar().showMessage(sender.text() + u'被电击了！！')


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # b1 = QtGui.QPushButton('Button 1', self)
        b1 = BasePushButton('ShowStatusBar', 'Button 1', self)
        b2 = BasePushButton('ShowStatusBar', 'Button 2', self)
        # b2 = QtGui.QPushButton('Button 2', self)

        b1.move(30, 50)
        b2.move(30, 100)

        self.statusBar()

        # b1.clicked.connect(self.cleckButton)
        # b2.clicked.connect(self.cleckButton)

        # 链接莫个信号
        self.c = Communicate()
        self.c.closeAPP.connect(self.close)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Click Button')
        self.show()

    def cleckButton(self):
        sender = self.sender()

        self.statusBar().showMessage(sender.text() + u'被电击了！！')

    def keyPressEvent(self, QKeyEvent):
        print QKeyEvent.key()
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.c.closeAPP.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
