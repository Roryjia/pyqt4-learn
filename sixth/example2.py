# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-11, by rory
# 
# 

__author__ = 'rory'

import sys

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.p1 = QtGui.QProgressBar(self)
        self.p1.move(10, 20)
        self.resize(30, 100)

        self.b1 = QtGui.QPushButton(u'Start', self)
        self.b1.move(10, 40)
        self.b1.clicked.connect(self.do_action)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        c1 = QtGui.QCalendarWidget(self)
        c1.showToday()
        c1.setGridVisible(False)
        c1.move(80, 40)

        self.setGeometry(300, 300, 400, 320)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()

    def timerEvent(self, QTimerEvent):
        if self.step >= 100:
            self.timer.stop()
            self.b1.setText('Finish')

        self.step += 1
        self.p1.setValue(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.b1.setText('Start')

        else:
            self.timer.start(100, self)
            self.b1.setText('Stop')


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
