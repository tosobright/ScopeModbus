# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_upgrade.ui'
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

class Ui_DialogUpgrade(object):
    def setupUi(self, DialogUpgrade):
        DialogUpgrade.setObjectName(_fromUtf8("DialogUpgrade"))
        DialogUpgrade.resize(381, 302)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/upgrade.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogUpgrade.setWindowIcon(icon)
        DialogUpgrade.setModal(True)
        self.widget = QtGui.QWidget(DialogUpgrade)
        self.widget.setGeometry(QtCore.QRect(10, 10, 361, 283))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Btn_Upgrade = QtGui.QPushButton(self.widget)
        self.Btn_Upgrade.setMinimumSize(QtCore.QSize(100, 50))
        self.Btn_Upgrade.setIcon(icon)
        self.Btn_Upgrade.setObjectName(_fromUtf8("Btn_Upgrade"))
        self.horizontalLayout_2.addWidget(self.Btn_Upgrade)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogUpgrade)
        QtCore.QMetaObject.connectSlotsByName(DialogUpgrade)

    def retranslateUi(self, DialogUpgrade):
        DialogUpgrade.setWindowTitle(_translate("DialogUpgrade", "Upgrade", None))
        self.toolButton.setText(_translate("DialogUpgrade", "...", None))
        self.Btn_Upgrade.setText(_translate("DialogUpgrade", "Upgrade", None))

import pyimg_rc
