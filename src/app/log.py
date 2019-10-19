# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#
import sys
from PyQt4 import QtCore
import time
import mypath


class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None

    messageWritten = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(XStream, self).__init__(parent)
        self.filepath = ''

    def flush(self):
        pass

    def fileno(self):
        return -1

    def write(self, msg):
        if (not self.signalsBlocked()):
            if (msg != '\n'):
                t = time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
                self.messageWritten.emit(unicode(t + msg))
                fp = mypath.FilePath('Log', 'log.log')
                f = open(fp, 'a+')
                f.write(t + msg.encode('utf-8') + '\n')
                f.close()

    @staticmethod
    def stdout():
        if (not XStream._stdout):
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if (not XStream._stderr):
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr
