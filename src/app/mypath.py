# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#
from PyQt4 import QtGui
import os

#APP_Path = 'E:\\git\\ScopeModbus\\src'
APP_Path = ''


def AppDir():
    if APP_Path != '':
        tempdir = APP_Path
    else:
        tempdir = str(QtGui.QApplication.applicationDirPath())
    return tempdir


def FilePath(folder, filename):
    appdir = AppDir()
    if folder != '':
        folderPath = os.path.join(appdir, folder)
    else:
        folderPath = appdir
    if filename != '':
        filePath = os.path.join(folderPath, filename)
    else:
        filePath = folderPath
    return filePath
