# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_comm.ui'
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

class Ui_DialogComm(object):
    def setupUi(self, DialogComm):
        DialogComm.setObjectName(_fromUtf8("DialogComm"))
        DialogComm.resize(292, 247)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/comm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogComm.setWindowIcon(icon)
        DialogComm.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(DialogComm)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 210, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(DialogComm)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 251, 191))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 19, 237, 156))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Lbl_1 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_1.setObjectName(_fromUtf8("Lbl_1"))
        self.verticalLayout.addWidget(self.Lbl_1)
        self.Lbl_2 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_2.setObjectName(_fromUtf8("Lbl_2"))
        self.verticalLayout.addWidget(self.Lbl_2)
        self.Lbl_3 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_3.setObjectName(_fromUtf8("Lbl_3"))
        self.verticalLayout.addWidget(self.Lbl_3)
        self.Lbl_4 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_4.setObjectName(_fromUtf8("Lbl_4"))
        self.verticalLayout.addWidget(self.Lbl_4)
        self.Lbl_5 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_5.setObjectName(_fromUtf8("Lbl_5"))
        self.verticalLayout.addWidget(self.Lbl_5)
        self.Lbl_6 = QtGui.QLabel(self.layoutWidget)
        self.Lbl_6.setObjectName(_fromUtf8("Lbl_6"))
        self.verticalLayout.addWidget(self.Lbl_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comb_Comm = QtGui.QComboBox(self.layoutWidget)
        self.comb_Comm.setMinimumSize(QtCore.QSize(100, 0))
        self.comb_Comm.setObjectName(_fromUtf8("comb_Comm"))
        self.verticalLayout_2.addWidget(self.comb_Comm)
        self.comb_BaudR = QtGui.QComboBox(self.layoutWidget)
        self.comb_BaudR.setObjectName(_fromUtf8("comb_BaudR"))
        self.verticalLayout_2.addWidget(self.comb_BaudR)
        self.comb_DPaity = QtGui.QComboBox(self.layoutWidget)
        self.comb_DPaity.setObjectName(_fromUtf8("comb_DPaity"))
        self.verticalLayout_2.addWidget(self.comb_DPaity)
        self.comb_DataBit = QtGui.QComboBox(self.layoutWidget)
        self.comb_DataBit.setObjectName(_fromUtf8("comb_DataBit"))
        self.verticalLayout_2.addWidget(self.comb_DataBit)
        self.comb_StopBit = QtGui.QComboBox(self.layoutWidget)
        self.comb_StopBit.setObjectName(_fromUtf8("comb_StopBit"))
        self.verticalLayout_2.addWidget(self.comb_StopBit)
        self.Edt_Timeout = QtGui.QLineEdit(self.layoutWidget)
        self.Edt_Timeout.setObjectName(_fromUtf8("Edt_Timeout"))
        self.verticalLayout_2.addWidget(self.Edt_Timeout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Btn_refresh = QtGui.QPushButton(self.layoutWidget)
        self.Btn_refresh.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_refresh.setIcon(icon1)
        self.Btn_refresh.setObjectName(_fromUtf8("Btn_refresh"))
        self.verticalLayout_3.addWidget(self.Btn_refresh)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(DialogComm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogComm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogComm.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogComm)

    def retranslateUi(self, DialogComm):
        DialogComm.setWindowTitle(_translate("DialogComm", "CommSet", None))
        self.groupBox.setTitle(_translate("DialogComm", "Comm", None))
        self.Lbl_1.setText(_translate("DialogComm", "ComPort", None))
        self.Lbl_2.setText(_translate("DialogComm", "BaudRate", None))
        self.Lbl_3.setText(_translate("DialogComm", "DataPaity", None))
        self.Lbl_4.setText(_translate("DialogComm", "DataBit", None))
        self.Lbl_5.setText(_translate("DialogComm", "StopBit", None))
        self.Lbl_6.setText(_translate("DialogComm", "Timeout", None))

import pyimg_rc
