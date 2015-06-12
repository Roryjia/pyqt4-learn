# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-10, by rory
#
#

__author__ = 'rory'

import sys

from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        b1 = QtGui.QPushButton('Input Dialog', self)
        b1.clicked.connect(self.show_input_dialog)
        self.l1 = QtGui.QLineEdit(self)

        self.l2 = QtGui.QLabel(u'Show 魔法：', self)

        b1.move(50, 50)
        self.l1.move(120, 100)
        self.l2.move(50, 100)

        b2 = QtGui.QPushButton('Color Dialog', self)
        b2.clicked.connect(self.show_color_dialog)
        b2.setStyleSheet("QWidget { background-color: %s }" % '#666')
        b2.resize(85, 20)
        b2.move(50, 250)

        col = QtGui.QColor(0, 0, 0)
        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
            % col.name())
        self.frm.move(50, 200)

        b3 = QtGui.QPushButton('Font Dialog', self)
        b3.clicked.connect(self.show_font_dialog)
        b3.move(250, 100)

        self.setGeometry(300, 300, 400, 350)
        self.setWindowTitle('More Dialog')
        self.show()

    def show_input_dialog(self):
        d, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Please Input You Name:')
        if ok:
            self.l1.setText(d)

    def show_color_dialog(self):
        c = QtGui.QColorDialog.getColor()
        if c.isValid():
            self.l1.setText(c.name())

            self.frm.setStyleSheet("QWidget { background-color: %s }" % c.name())

            self.sender().setStyleSheet("QWidget { background-color: %s }" % c.name())

    def show_font_dialog(self):
        f, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.l2.setFont(f)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.close()

        print QKeyEvent.key()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()