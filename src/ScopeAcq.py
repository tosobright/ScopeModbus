# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#


import sys
from PyQt4 import QtCore, QtGui
from app.windows_main import MyWindow
import os
from configobj import ConfigObj
from app import mypath


if __name__ == "__main__":
    QtApp = QtGui.QApplication(sys.argv)

    # 加载翻译配置
    configPath = mypath.FilePath('Config', 'Sys.ini')
    config = ConfigObj(configPath, encoding='UTF8')
    # print config['CommPar']['Comm']
    try:
        Lang = config['System']['Lang']
    except:
        Lang = "ENGLISH"

    # 加载翻译
    try:
        transPath = mypath.FilePath('Lang', Lang + '.qm')
        print transPath
        trans = QtCore.QTranslator()
        print trans.load(transPath)
        QtApp.installTranslator(trans)
    except:
        pass

    myW = MyWindow()

    # 菜单链接
    myW.ui.action_DeviceConnect.triggered.connect(myW.DevConn)
    # myW.ui.action_DeviceClose.triggered.connect()
    # myW.ui.action_DeviceInfo.triggered.connect()
    myW.ui.action_Exit.triggered.connect(myW.close)
    myW.ui.action_Start.triggered.connect(myW.AcqStart)
    myW.ui.action_Stop.triggered.connect(myW.AcqStop)
    # myW.ui.action_SaveData.triggered.connect()
    myW.ui.action_Communication.triggered.connect(myW.CommSet)
    myW.ui.action_Option.triggered.connect(myW.OptionSet)
    myW.ui.action_Upgrade.triggered.connect(myW.UpgradeShow)
    # myW.ui.action_HelpFile.triggered.connect()
    # myW.ui.action_Update.triggered.connect()
    myW.ui.action_About.triggered.connect(myW.AboutShow)

    myW.show()
    sys.exit(QtApp.exec_())
