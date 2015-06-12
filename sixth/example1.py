# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
#
#

__author__ = 'rory'

import sys

from PyQt4 import QtGui, QtCore


class Example1(QtGui.QWidget):

    def __init__(self):
        super(Example1, self).__init__()

        self.initUI()

    def initUI(self):
        cb = QtGui.QCheckBox(u'请选择', self)
        cb.move(50, 20)
        cb.stateChanged.connect(self.cb_state_change)

        b1 = QtGui.QPushButton(u'Red', self)
        b1.setCheckable(True)
        b1.move(50, 50)
        b1.clicked[bool].connect(self.set_color)

        b2 = QtGui.QPushButton(u'Green', self)
        b2.setCheckable(True)
        b2.move(50, 100)
        b2.clicked[bool].connect(self.set_color)

        b3 = QtGui.QPushButton(u'Blue', self)
        b3.setCheckable(True)
        b3.move(50, 150)
        b3.clicked[bool].connect(self.set_color)

        self.col = QtGui.QColor(0, 0, 0)
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(50, 200, 100, 30)
        sld.valueChanged[int].connect(self.change_image)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('../first/dog.jpg'))
        self.label.setGeometry(160, 130, 180, 150)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle(u'Widget 组件')
        self.show()

    def cb_state_change(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle(u'已选中')
            self.sender().setText(u'已选中')
        else:
            self.setWindowTitle(u'请选择')
            self.sender().setText(u'请选择')

    def set_color(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

    def change_image(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('../first/dog.jpg'))
            self.col.setRed(value)
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('../first/L1.jpg'))
            self.col.setGreen(value)
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('../first/L2.jpg'))
            self.col.setBlue(value)
        else:
            self.col.setRed(value)
            self.label.setPixmap(QtGui.QPixmap('../first/dog.jpg'))

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()