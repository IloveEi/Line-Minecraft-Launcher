# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Line(object):
    def setupUi(self, Line):
        Line.setObjectName("Line")
        Line.resize(766, 411)
        self.stackedWidget = QtWidgets.QStackedWidget(Line)
        self.stackedWidget.setGeometry(QtCore.QRect(140, 50, 681, 351))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.headpic = QtWidgets.QLabel(Line)
        self.headpic.setGeometry(QtCore.QRect(40, 80, 61, 61))
        self.headpic.setText("")
        self.headpic.setObjectName("headpic")
        self.lineEdit = LineEdit(Line)
        self.lineEdit.setGeometry(QtCore.QRect(10, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.startg = PushButton(Line)
        self.startg.setGeometry(QtCore.QRect(10, 250, 121, 41))
        self.startg.setObjectName("startg")
        self.pickuser = ComboBox(Line)
        self.pickuser.setGeometry(QtCore.QRect(10, 190, 121, 31))
        self.pickuser.setObjectName("pickuser")
        self.pickver = ComboBox(Line)
        self.pickver.setGeometry(QtCore.QRect(10, 350, 121, 31))
        self.pickver.setObjectName("pickver")
        self.cpa = PushButton(Line)
        self.cpa.setGeometry(QtCore.QRect(222, 11, 81, 31))
        self.cpa.setObjectName("cpa")
        self.cpl_4 = PushButton(Line)
        self.cpl_4.setGeometry(QtCore.QRect(141, 11, 81, 31))
        self.cpl_4.setObjectName("cpl_4")
        self.cpt = PushButton(Line)
        self.cpt.setGeometry(QtCore.QRect(303, 11, 81, 31))
        self.cpt.setObjectName("cpt")
        self.cpd = PushButton(Line)
        self.cpd.setGeometry(QtCore.QRect(384, 11, 81, 31))
        self.cpd.setObjectName("cpd")
        self.cps = PushButton(Line)
        self.cps.setGeometry(QtCore.QRect(465, 11, 81, 31))
        self.cps.setObjectName("cps")
        self.ver = QtWidgets.QLabel(Line)
        self.ver.setGeometry(QtCore.QRect(10, 330, 54, 12))
        self.ver.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.ver.setObjectName("ver")

        self.retranslateUi(Line)
        QtCore.QMetaObject.connectSlotsByName(Line)

    def retranslateUi(self, Line):
        _translate = QtCore.QCoreApplication.translate
        Line.setWindowTitle(_translate("Line", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Line", "用户名"))
        self.startg.setText(_translate("Line", "启动"))
        self.pickuser.setPlaceholderText(_translate("Line", "已保存的用户"))
        self.pickver.setPlaceholderText(_translate("Line", "版本"))
        self.cpa.setText(_translate("Line", "账户"))
        self.cpl_4.setText(_translate("Line", "启动"))
        self.cpt.setText(_translate("Line", "终端"))
        self.cpd.setText(_translate("Line", "下载"))
        self.cps.setText(_translate("Line", "设置"))
        self.ver.setText(_translate("Line", "启动版本"))
from qfluentwidgets import ComboBox, LineEdit, PushButton