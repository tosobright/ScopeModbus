# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_product.ui'
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

class Ui_DialogPro(object):
    def setupUi(self, DialogPro):
        DialogPro.setObjectName(_fromUtf8("DialogPro"))
        DialogPro.resize(368, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogPro.setWindowIcon(icon)
        DialogPro.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(DialogPro)
        self.buttonBox.setGeometry(QtCore.QRect(50, 160, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(DialogPro)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 291, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(50, 30, 187, 76))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Lbl_DevAddr = QtGui.QLabel(self.widget)
        self.Lbl_DevAddr.setObjectName(_fromUtf8("Lbl_DevAddr"))
        self.verticalLayout_2.addWidget(self.Lbl_DevAddr)
        self.Lbl_Product = QtGui.QLabel(self.widget)
        self.Lbl_Product.setObjectName(_fromUtf8("Lbl_Product"))
        self.verticalLayout_2.addWidget(self.Lbl_Product)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Edt_DevAddr = QtGui.QLineEdit(self.widget)
        self.Edt_DevAddr.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Edt_DevAddr.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Edt_DevAddr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Edt_DevAddr.setObjectName(_fromUtf8("Edt_DevAddr"))
        self.verticalLayout.addWidget(self.Edt_DevAddr)
        self.comb_Product = QtGui.QComboBox(self.widget)
        self.comb_Product.setObjectName(_fromUtf8("comb_Product"))
        self.verticalLayout.addWidget(self.comb_Product)
        self.Edt_AcqCyc = QtGui.QLineEdit(self.widget)
        self.Edt_AcqCyc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Edt_AcqCyc.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Edt_AcqCyc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Edt_AcqCyc.setObjectName(_fromUtf8("Edt_AcqCyc"))
        self.verticalLayout.addWidget(self.Edt_AcqCyc)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DialogPro)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogPro.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogPro.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogPro)

    def retranslateUi(self, DialogPro):
        DialogPro.setWindowTitle(_translate("DialogPro", "LoadProduct", None))
        self.groupBox.setTitle(_translate("DialogPro", "Select", None))
        self.Lbl_DevAddr.setText(_translate("DialogPro", "DevAddr", None))
        self.Lbl_Product.setText(_translate("DialogPro", "Product", None))
        self.label.setText(_translate("DialogPro", "AcqCyc", None))

import pyimg_rc
