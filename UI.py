# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.downloadBtn = QtWidgets.QPushButton(Form)
        self.downloadBtn.setGeometry(QtCore.QRect(150, 250, 100, 30))
        self.downloadBtn.setObjectName("downloadBtn")
        self.link = QtWidgets.QLineEdit(Form)
        self.link.setGeometry(QtCore.QRect(75, 50, 250, 25))
        self.link.setObjectName("link")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(175, 30, 50, 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(Form)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(0, 150, 400, 15))
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(70, 100, 300, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.downloadBtn.setText(_translate("Form", "下載"))
        self.label.setText(_translate("Form", "網址"))
        self.title.setText(_translate("Form", "標題"))

