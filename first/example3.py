# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-09, by rory
# 
# 

__author__ = 'rory'


import sys
from PyQt4 import QtGui, QtCore


class Example3(QtGui.QWidget):

    def __init__(self):
        super(Example3, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('Monon', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 对于btn 设置点击事件链接 -- 关闭整个应用程序
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        # 设置按钮大小为建议大小
        btn.resize(btn.sizeHint())
        # 移动按钮的位置
        btn.move(80, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()