# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName(_fromUtf8("DialogAbout"))
        DialogAbout.resize(368, 232)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAbout.setWindowIcon(icon)
        DialogAbout.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        DialogAbout.setModal(True)
        self.label = QtGui.QLabel(DialogAbout)
        self.label.setGeometry(QtCore.QRect(20, 10, 194, 52))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(DialogAbout)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 90, 241, 91))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(_fromUtf8(""))
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Raised)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.retranslateUi(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(_translate("DialogAbout", "About", None))
        self.label.setText(_translate("DialogAbout", "<html><head/><body><p><img src=\":/source/img/ico.png\" width=\"40\" height=\"40\"/><span style=\" font-size:16pt; font-weight:600;color:rgb(0, 0, 150)\">ScopeModbus</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(_translate("DialogAbout", "Version:", None))

import pyimg_rc
