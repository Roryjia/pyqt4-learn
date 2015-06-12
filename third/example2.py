# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'

import sys

from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        vbox = QtGui.QVBoxLayout()

        lineEdit = QtGui.QLineEdit()
        vbox.addWidget(lineEdit)

        grid = QtGui.QGridLayout()
        names = [
            'Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        print positions

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

        vbox.addLayout(grid)
        self.setLayout(vbox)
        # self.setGeometry(300, 150, 400, 320)
        self.setWindowTitle('Calculator')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()