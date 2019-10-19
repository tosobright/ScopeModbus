# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_option.ui'
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

class Ui_DialogOption(object):
    def setupUi(self, DialogOption):
        DialogOption.setObjectName(_fromUtf8("DialogOption"))
        DialogOption.resize(489, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/source/img/option.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogOption.setWindowIcon(icon)
        DialogOption.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(DialogOption)
        self.buttonBox.setGeometry(QtCore.QRect(170, 340, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(DialogOption)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 471, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comb_Lang = QtGui.QComboBox(self.groupBox)
        self.comb_Lang.setGeometry(QtCore.QRect(20, 40, 121, 22))
        self.comb_Lang.setObjectName(_fromUtf8("comb_Lang"))
        self.comb_Lang.addItem(_fromUtf8(""))
        self.comb_Lang.addItem(_fromUtf8(""))
        self.comb_Lang.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(DialogOption)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogOption.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogOption.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogOption)

    def retranslateUi(self, DialogOption):
        DialogOption.setWindowTitle(_translate("DialogOption", "Option", None))
        self.groupBox.setTitle(_translate("DialogOption", "SelectLanguage", None))
        self.comb_Lang.setItemText(0, _translate("DialogOption", "ENGLISH", None))
        self.comb_Lang.setItemText(1, _translate("DialogOption", "zh_CN", None))
        self.comb_Lang.setItemText(2, _translate("DialogOption", "zh_TW", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DialogOption", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DialogOption", "Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DialogOption", "Tab 3", None))

import pyimg_rc
