# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#

from PyQt4 import QtCore, QtGui, Qt
from layout.ui_layout_main import Ui_MainWindow
from layout.ui_layout_product import Ui_DialogPro
from layout.ui_layout_comm import Ui_DialogComm
from layout.ui_layout_option import Ui_DialogOption
from layout.ui_layout_upgrade import Ui_DialogUpgrade
from layout.ui_layout_about import Ui_DialogAbout
import numpy as np
import time
import datetime
import os
from layout import pyimg_rc
from MBRTU.modbus import MB
import glob
import json
from configobj import ConfigObj
import MBRTU.MBFormat as mbf
from log import XStream
import sys
import mypath


#时间线程
class TimeThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)

    def run(self):
        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            time.sleep(1)
            self.txt_time.setText(t)

    def getTimeObj(self,obj):
        self.txt_time = obj

# 采集线程


class AcqThread(QtCore.QThread):
    signal_acqdata = QtCore.pyqtSignal(str, list)  # 信号

    def __init__(self, parent=None):
        super(AcqThread, self).__init__(parent)
        self.bol_working = True
        self.bol_emit = False
        self.int_cyc = 1  # 单位为s
        self.num = 0

    def run(self):
        while self.bol_working:
            # print "Working", self.thread()
            if self.bol_emit:
              try:
                self.cmdtxt.setUpdatesEnabled(False)
                v=[]
                for item in self.productpar:
                    func = item['func']
                    startaddr = item['startaddr']
                    length = item['length']
                    d = self.mb.read(func, startaddr, length)
                    #print func,startaddr,length,d
                    if item['type'] == 'int':
                        dv = mbf.ReadInt(d)
                    elif item['type'] == 'float':
                        dv = mbf.ReadFloat(d)
                    elif item['type'] == 'list':
                        dv = mbf.ReadInt(d)
                    elif item['type'] == 'bool':
                        if mbf.ReadInt(d) == 1:
                          dv = True
                        else:
                          dv = False
                    v.append(dv)  
                #print v   
                self.cmdtxt.setUpdatesEnabled(True)
                self.num += 1 
                self.signal_acqdata.emit("Running:"+str(self.num), v)  # 发送信号              
              except Exception as e:
                self.cmdtxt.setUpdatesEnabled(True)
                pass
            self.sleep(self.int_cyc)

    def startAcq(self, AcqCyc):
        self.num = 0
        self.int_cyc = AcqCyc
        self.bol_emit = True

    def stopAcq(self):
        self.bol_emit = False

    def ExitThread(self):
        self.bol_working = False

    def UpdateMB(self,mb):
        self.mb = mb

    def UpdateAutoPar(self,pars):
        self.productpar = pars

    def TreeRead(self,tree,treepars):
        for group in treepars:
          basic = group['name']
          for item in group['children']:
              child = item['name']
              try:
                func = item['func']
                startaddr = item['startaddr']
                length = item['length']
                d = self.mb.read(func, startaddr, length)
                #print func,startaddr,length,d
                if item['type'] == 'int':
                    dv = mbf.ReadInt(d)
                elif item['type'] == 'float':
                    dv = mbf.ReadFloat(d)
                    # print dv
                elif item['type'] == 'list':
                        dv = mbf.ReadInt(d)
                elif item['type'] == 'bool':
                    if mbf.ReadInt(d) == 1:
                      dv = True
                    else:
                      dv = False
                tree.setVal(basic,child,dv)
              except Exception as e:
                raise e

    def TreeWrite(self,tree,childName,par):
        func = par['func1']
        start = par['startaddr']
        try:
          if par['type'] == 'int':
                val = mbf.WriteInt(int(par['value']))
          elif par['type'] == 'float':
              val = mbf.WriteFloat(float(par['value']))
          elif par['type'] == 'list':
              val = mbf.WriteInt(par['values'].index(par['value']))
          elif par['type'] == 'bool':
              val = mbf.WriteInt(int(par['value']))

          self.mb.write(func, start, val)
          #bc = childName.split('.')
          #tree.setVal(bc[0],bc[1],val)
        except Exception as e:
          pass
    
    def CommandTxt(self,cmd):
        self.cmdtxt = cmd

# 升级加载对话框


class dialogUpgrade(QtGui.QDialog):
    def __init__(self):
        super(dialogUpgrade, self).__init__()
        self.ui = Ui_DialogUpgrade()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)
        self.ui.toolButton.clicked.connect(self.LoadDialogPath)
        self.ui.Btn_Upgrade.clicked.connect(self.Upgrade)
        self.ui.progressBar.setValue(0)
        self.ui.lineEdit.setText('')
        self.ui.plainTextEdit.setPlainText('')

    def LoadDialogPath(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,self.tr(u'select UpgradeFile'),'',u'file(*.upf)')
        self.ui.lineEdit.setText(filename)

    def Upgrade(self):
        pass

# 选项加载对话框


class dialogOption(QtGui.QDialog):
    def __init__(self):
        super(dialogOption, self).__init__()
        self.ui = Ui_DialogOption()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)


# 通信配置加载对话框


class dialogComm(QtGui.QDialog):
    def __init__(self, ports):
        super(dialogComm, self).__init__()
        self.ui = Ui_DialogComm()
        self.ui.setupUi(self)
        self.ui.comb_Comm.addItems(ports)
        self.ui.comb_BaudR.addItems(['9600', '19200', '115200'])
        self.ui.comb_DPaity.addItems(['None', 'Odd', 'Even'])
        self.ui.comb_DataBit.addItems(['5', '6', '7', '8'])
        self.ui.comb_StopBit.addItems(['1', '1.5', '2'])
        self.ui.Edt_Timeout.setValidator(QtGui.QIntValidator(10, 10000))
        self.ui.Edt_Timeout.setText('1000')
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)

# 关于对话框


class dialogAbout(QtGui.QDialog):
    def __init__(self):
        super(dialogAbout, self).__init__()
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)
        self.ui.plainTextEdit.setPlainText(self.tr('Version:1.0'))
        self.ui.plainTextEdit.appendPlainText(self.tr('Author:Toso'))

# 产品加载对话框


class dialogProduct(QtGui.QDialog):
    def __init__(self):
        super(dialogProduct, self).__init__()
        self.ui = Ui_DialogPro()
        self.ui.setupUi(self)
        # 加载翻译配置
        configPath = mypath.FilePath('Config', 'Sys.ini')
        config = ConfigObj(configPath, encoding='UTF8')
        # print config['CommPar']['Comm']
        try:
            Lang = config['System']['Lang']
        except:
            Lang = "ENGLISH"
        p = mypath.FilePath('Product',Lang)
        pro = glob.glob(p + '//*')
        #print os.path, p
        self.ProductPath = pro
        for item in pro:
            filename, extension = os.path.splitext(os.path.basename(item))
            if extension == '.json':
                self.ui.comb_Product.addItem(filename)
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint)
        self.ui.Edt_DevAddr.setValidator(QtGui.QIntValidator(0, 250))
        self.ui.Edt_DevAddr.setText('1')
        self.ui.Edt_AcqCyc.setValidator(QtGui.QIntValidator(1,1000))
        self.ui.Edt_AcqCyc.setText('1')

    def updatePar(self):
        pass

# 主窗体


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # 这里需要注意self.ui已经将Ui_MainWindow类实例
        # 化，因此继承了该类的所有属性，后面更改设置属性都用self.ui“冠名”
        # 主UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #log信号连接create connections
        xstream = XStream()
        xstream.stdout().messageWritten.connect( self.LogHistory)
        xstream.stderr().messageWritten.connect( self.LogHistory)

        self.UiInit()


        # modbus通信class
        self.mb = MB()
        self.ports = self.mb.ComAutoFind()
        #self.mb.Log(self.ui.txt_CMD)
        self.mb.MBrecord.connect(self.LogRecord)

        self.ui.txt_CMD.maximumBlockCount = 100
        self.ui.txt_CMD.setReadOnly(True)
        self.ui.txt_CMD.setPlainText(self.tr(u'CommandLog'))
        self.ui.txt_CMD.appendPlainText('-----------------')

        # 通信配置加载对话框
        self.dialogcomm = dialogComm(self.ports)
        self.dialogcomm.ui.buttonBox.accepted.connect(self.SaveCommPar)
        self.dialogcomm.ui.Btn_refresh.clicked.connect(self.ComRefresh)
        self.LoadCommPar()
        # 产品加载dialog
        self.dialogproduct = dialogProduct()
        self.dialogproduct.ui.buttonBox.accepted.connect(
            self.LoadProductPar)
        #选项配置加载对话框
        self.dialogoption = dialogOption()
        self.dialogoption.ui.buttonBox.accepted.connect(self.SaveOption)
        #升级加载对话框
        self.dialogupgrade = dialogUpgrade()
        self.dialogupgrade.ui.Btn_Upgrade.clicked.connect(self.Upgrade)     
        #关于对话框
        self.dialogabout = dialogAbout()   

        # Load thread
        # 创建新线程
        self.threadAcq = AcqThread()
        # thread2 = myThread(2, "Thread-2", 2)
        # 连接信号
        self.threadAcq.signal_acqdata.connect(self.Graph_Update)
        # 开启线程
        self.threadAcq.start()
        self.threadAcq.CommandTxt(self.ui.txt_CMD)

        self.threadTime = TimeThread()
        self.threadTime.getTimeObj(self.Txt_time)
        self.threadTime.start()

        self.Btn_DevConn.setEnabled(True)
        self.Btn_AcqStart.setEnabled(False)
        self.Btn_AcqStop.setEnabled(False)
        self.Btn_AcqSave.setEnabled(False)
        self.Btn_CommSet.setEnabled(True)
        self.Btn_Option.setEnabled(True)
        self.Btn_Upgrade.setEnabled(False)
        self.ui.widget_parTree.setEnabled(False)

        self.ui.action_DeviceConnect.setEnabled(True)
        self.ui.action_DeviceClose.setEnabled(False)
        self.ui.action_DeviceInfo.setEnabled(False)
        self.ui.action_Exit.setEnabled(True)
        self.ui.action_Start.setEnabled(False)
        self.ui.action_Stop.setEnabled(False)
        self.ui.action_SaveData.setEnabled(False)
        self.ui.action_Communication.setEnabled(True)
        self.ui.action_Option.setEnabled(True)
        self.ui.action_Upgrade.setEnabled(False)
        self.ui.action_HelpFile.setEnabled(True)
        self.ui.action_Update.setEnabled(True)
        self.ui.action_About.setEnabled(True)


    def threadexit(self):
        self.threadAcq.ExitThread()

    def UiInit(self):
        #允许嵌套dock
        self.setDockNestingEnabled(True)
        self.setCentralWidget(self.ui.dockW_Scope)
        #合并窗体dock
        self.tabifyDockWidget(self.ui.dockW_Command,self.ui.dockW_History)
        #将制定dock放置在最前
        self.ui.dockW_Command.raise_()
        self.ToolBarInit()
        self.StatusBarInit()
        self.ButtonConnect()

    def ToolBarInit(self):
        # pass
        # ----------添加工具栏----------------------
        # 设备连接按钮
        self.Btn_DevConn = QtGui.QAction(QtGui.QIcon(
            ":/source/img/connect.png"), self.tr(u'Conn'), self)
        self.Btn_DevConn.setStatusTip(self.tr(u'Device Connect'))
        self.Btn_DevConn.triggered.connect(self.DevConn)
        self.ui.toolBar.addAction(self.Btn_DevConn)
        self.ui.toolBar.addSeparator()

        # 采集开始按钮
        self.Btn_AcqStart = QtGui.QAction(QtGui.QIcon(
            ":/source/img/start.png"), self.tr(u'Start'), self)
        self.Btn_AcqStart.setStatusTip(self.tr(u'Acquire Start'))
        self.Btn_AcqStart.triggered.connect(self.AcqStart)
        #self.Btn_AcqStart.setCheckable(True)
        #self.Btn_AcqStart.setChecked(False)
        self.ui.toolBar.addAction(self.Btn_AcqStart)
        # 采集停止按钮
        self.Btn_AcqStop = QtGui.QAction(QtGui.QIcon(
            ":/source/img/stop.png"), self.tr(u'Stop'), self)
        self.Btn_AcqStop.setStatusTip(self.tr(u'Acquire Stop'))
        self.Btn_AcqStop.triggered.connect(self.AcqStop)
        self.ui.toolBar.addAction(self.Btn_AcqStop)
        # 采集保存按钮
        self.Btn_AcqSave = QtGui.QAction(QtGui.QIcon(
            ":/source/img/save.png"), self.tr(u'Save'), self)
        self.Btn_AcqSave.setStatusTip(self.tr(u'Acquire Save'))
        self.ui.toolBar.addAction(self.Btn_AcqSave)

        self.ui.toolBar.addSeparator()

        # 通信设置按钮
        self.Btn_CommSet = QtGui.QAction(QtGui.QIcon(
            ":/source/img/comm.png"), self.tr(u'CommSet'), self)
        self.Btn_CommSet.setStatusTip(self.tr(u'Communication Set'))
        self.Btn_CommSet.triggered.connect(self.CommSet)
        self.ui.toolBar.addAction(self.Btn_CommSet)
        # 选项设置按钮
        self.Btn_Option = QtGui.QAction(QtGui.QIcon(
            ":/source/img/option.png"), self.tr(u'Option'), self)
        self.Btn_Option.setStatusTip(self.tr(u'OptionSet'))
        self.Btn_Option.triggered.connect(self.OptionSet)
        self.ui.toolBar.addAction(self.Btn_Option)

        self.ui.toolBar.addSeparator()

        # 升级
        self.Btn_Upgrade = QtGui.QAction(QtGui.QIcon(
            ":/source/img/upgrade.png"), self.tr(u'Upgrade'), self)
        self.Btn_Upgrade.setStatusTip(self.tr(u'Upgrade'))
        self.Btn_Upgrade.triggered.connect(self.UpgradeShow)
        self.ui.toolBar.addAction(self.Btn_Upgrade)

        self.ui.toolBar.addSeparator()

        # 帮助
        self.Btn_HelpFile = QtGui.QAction(QtGui.QIcon(
            ":/source/img/help.png"), self.tr(u'HelpFile'), self)
        self.Btn_HelpFile.setStatusTip(self.tr(u'HelpFile'))
        self.ui.toolBar.addAction(self.Btn_HelpFile)

    def StatusBarInit(self):
        #self.Txt_Sep = QtGui.QLabel()
        #self.ui.statusBar.addPermanentWidget(self.Txt_Sep)
        self.ui.statusBar.setMaximumHeight(20)

        self.Txt_Msg = QtGui.QLabel()
        self.Txt_Msg.width = 200
        self.Txt_Msg.setText(self.tr('Please Connect the Device...'))        
        self.ui.statusBar.addPermanentWidget(self.Txt_Msg)

        self.Txt_Com = QtGui.QLabel()
        self.Txt_Com.setMinimumSize(QtCore.QSize(90,0))
        self.Txt_Com.setAlignment(QtCore.Qt.AlignCenter)
        self.Txt_Com.setText(self.tr('NoPort'))
        self.ui.statusBar.addPermanentWidget(self.Txt_Com)

        self.Txt_Pro = QtGui.QLabel()
        self.Txt_Pro.setMinimumSize(QtCore.QSize(120,0))
        self.Txt_Pro.setAlignment(QtCore.Qt.AlignCenter)
        self.Txt_Pro.setText(self.tr('ProductInfo'))
        self.ui.statusBar.addPermanentWidget(self.Txt_Pro)

        self.Txt_Addr = QtGui.QLabel()
        self.Txt_Addr.setMinimumSize(QtCore.QSize(70,0))
        self.Txt_Addr.setAlignment(QtCore.Qt.AlignCenter)
        self.Txt_Addr.setText(self.tr('None'))
        self.ui.statusBar.addPermanentWidget(self.Txt_Addr)

        self.Txt_time = QtGui.QLabel()
        self.Txt_time.setMinimumSize(QtCore.QSize(130,0))
        self.Txt_time.setAlignment(QtCore.Qt.AlignCenter)
        self.Txt_time.setText('0000-00-00 00:00:00')
        self.ui.statusBar.addPermanentWidget(self.Txt_time)

    def ButtonConnect(self):
            # 按钮链接
        pass

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            self.tr(u"Exit"),
                                            self.tr(u"Are you Sure?"),
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            # self.releasePlot()  # release thread's resouce
            self.threadexit()
            event.accept()

    def helpfile(self):
        #print '12345'
        tempdir = QtGui.QApplication.applicationDirPath()
        # print tempdir
        filepath = QtCore.QString.fromUtf8(
            os.path.join(str(tempdir), 'readme.txt'))
        #print filepath
        if QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(filepath)) == False:
            QtGui.QMessageBox.information(self, self.tr(u"ScopeModbus"), self.tr(u"can't find helpfile！"))

    def DevConn(self):
        print unicode(self.tr(u"ScopeModbus"))
        self.dialogproduct.show()

    def LoadProductPar(self):
        # 获取参数
        self.DevAddr = int(self.dialogproduct.ui.Edt_DevAddr.text())
        self.ProductName = self.dialogproduct.ui.comb_Product.currentText()
        self.AcqCyc = int(self.dialogproduct.ui.Edt_AcqCyc.text())
        #print str(self.ProductName)
        path = self.dialogproduct.ProductPath[self.dialogproduct.ui.comb_Product.currentIndex()]
        with open(path, 'r') as f:
            data = f.read()
        self.ProductPar = json.loads(data)
        self.ui.widget_qtGraph.LoadInit(self.ProductPar)
        self.ui.widget_parTree.LoadPar(self.ProductPar)
        self.ui.widget_parTree.partree.sigTreeStateChanged.connect(self.treeChange)

        # print self.mb.ComAutoFind()
        self.mb.close()
        try:
          self.mb.Open(self.DevAddr, self.Comm,self.BaudR,self.DPaity,self.DataBit,self.StopBit,self.Timeout)
        except Exception as e:
          QtGui.QMessageBox.information(self,self.tr(u'ErrInfo'),self.tr("can't open port!"))
        #self.ui.widget_parTree.mb_read(self.mb, 03, 0, 1)
        #读取初始状态
        #print self.ProductPar
        self.threadAcq.UpdateMB(self.mb)
        self.threadAcq.UpdateAutoPar(self.ProductPar[0]['children'])
        self.threadAcq.TreeRead(self.ui.widget_parTree,self.ProductPar)

        self.Txt_Pro.setText(self.ProductName)
        self.Txt_Addr.setText('Addr:' + str(self.DevAddr))

        #界面控件使能       
        self.Btn_DevConn.setEnabled(True)
        self.Btn_AcqStart.setEnabled(True)
        self.Btn_AcqStop.setEnabled(False)
        self.Btn_AcqSave.setEnabled(True)
        self.Btn_CommSet.setEnabled(True)
        self.Btn_Option.setEnabled(True)
        self.Btn_Upgrade.setEnabled(True)
        self.ui.widget_parTree.setEnabled(True)

        self.ui.action_DeviceConnect.setEnabled(True)
        self.ui.action_DeviceClose.setEnabled(True)
        self.ui.action_DeviceInfo.setEnabled(True)
        self.ui.action_Exit.setEnabled(True)
        self.ui.action_Start.setEnabled(True)
        self.ui.action_Stop.setEnabled(False)
        self.ui.action_SaveData.setEnabled(True)
        self.ui.action_Communication.setEnabled(True)
        self.ui.action_Option.setEnabled(True)
        self.ui.action_Upgrade.setEnabled(True)
        self.ui.action_HelpFile.setEnabled(True)
        self.ui.action_Update.setEnabled(True)
        self.ui.action_About.setEnabled(True)
        

    def AcqStart(self):
        self.Btn_DevConn.setEnabled(False)
        self.Btn_AcqStart.setEnabled(False)
        self.Btn_AcqStop.setEnabled(True)
        self.Btn_AcqSave.setEnabled(False)
        self.Btn_CommSet.setEnabled(False)
        self.Btn_Option.setEnabled(False)
        self.Btn_Upgrade.setEnabled(False)
        self.ui.widget_parTree.setEnabled(False)

        self.ui.action_DeviceConnect.setEnabled(False)
        self.ui.action_DeviceClose.setEnabled(False)
        self.ui.action_DeviceInfo.setEnabled(False)
        self.ui.action_Exit.setEnabled(True)
        self.ui.action_Start.setEnabled(False)
        self.ui.action_Stop.setEnabled(True)
        self.ui.action_SaveData.setEnabled(False)
        self.ui.action_Communication.setEnabled(False)
        self.ui.action_Option.setEnabled(False)
        self.ui.action_Upgrade.setEnabled(False)
        self.ui.action_HelpFile.setEnabled(True)
        self.ui.action_Update.setEnabled(True)
        self.ui.action_About.setEnabled(True)

        # self.ui.widget_parTree.
        self.threadAcq.startAcq(self.AcqCyc)

    def AcqStop(self):
        self.Btn_DevConn.setEnabled(True)
        self.Btn_AcqStart.setEnabled(True)
        self.Btn_AcqStop.setEnabled(False)
        self.Btn_AcqSave.setEnabled(True)
        self.Btn_CommSet.setEnabled(True)
        self.Btn_Option.setEnabled(True)
        self.Btn_Upgrade.setEnabled(True)
        self.ui.widget_parTree.setEnabled(True)

        self.ui.action_DeviceConnect.setEnabled(True)
        self.ui.action_DeviceClose.setEnabled(True)
        self.ui.action_DeviceInfo.setEnabled(True)
        self.ui.action_Exit.setEnabled(True)
        self.ui.action_Start.setEnabled(True)
        self.ui.action_Stop.setEnabled(False)
        self.ui.action_SaveData.setEnabled(True)
        self.ui.action_Communication.setEnabled(True)
        self.ui.action_Option.setEnabled(True)
        self.ui.action_Upgrade.setEnabled(True)
        self.ui.action_HelpFile.setEnabled(True)
        self.ui.action_Update.setEnabled(True)
        self.ui.action_About.setEnabled(True)

        self.threadAcq.stopAcq()

    def Graph_Update(self, str, list):
        #print str
        self.ui.widget_qtGraph.Update(1, list)
        basicname = self.ProductPar[0]['name']
        for index,item in enumerate(self.ProductPar[0]['children']):
            self.ui.widget_parTree.setVal(basicname,item['name'],list[index])

    def CommSet(self):
        self.LoadCommPar()
        self.dialogcomm.show()

    def SaveCommPar(self):
        configPath = mypath.FilePath('Config','Comm.ini')
        config=ConfigObj(configPath, encoding='UTF8')
        config['CommPar']={}
        config['CommPar']['Comm']=self.dialogcomm.ui.comb_Comm.currentText()
        config['CommPar']['BaudR']=self.dialogcomm.ui.comb_BaudR.currentText()
        config['CommPar']['DPaity']=self.dialogcomm.ui.comb_DPaity.currentText()
        config['CommPar']['DataBit']=self.dialogcomm.ui.comb_DataBit.currentText()
        config['CommPar']['StopBit']=self.dialogcomm.ui.comb_StopBit.currentText()
        config['CommPar']['Timeout']=self.dialogcomm.ui.Edt_Timeout.text()
        config.write()
        self.LoadCommPar()
        print self.tr('Save Communication parameter')

    def LoadCommPar(self):
        configPath = mypath.FilePath('Config','Comm.ini')
        config=ConfigObj(configPath, encoding='UTF8')
        # print config['CommPar']['Comm']
        try:
          self.Comm=config['CommPar']['Comm']
          self.dialogcomm.ui.comb_Comm.setCurrentIndex(
            self.dialogcomm.ui.comb_Comm.findText(self.Comm))
        except:
          pass
        # print config['CommPar']['BaudR']
        try:
          BaudR=config['CommPar']['BaudR']
          self.dialogcomm.ui.comb_BaudR.setCurrentIndex(
              self.dialogcomm.ui.comb_BaudR.findText(BaudR))
          self.BaudR=int(BaudR)
        except:
          pass
        # print config['CommPar']['DPaity']
        try:
          DPaity=config['CommPar']['DPaity']
          self.dialogcomm.ui.comb_DPaity.setCurrentIndex(
              self.dialogcomm.ui.comb_DPaity.findText(DPaity))
          if DPaity == 'None':
              self.DPaity= 'N'
          elif DPaity == 'Odd':
              self.DPaity= 'O'
          elif DPaity == 'Even':
              self.DPaity= 'E'
        except:
          pass
        # print config['CommPar']['DataBit']
        try:
          DataBit=config['CommPar']['DataBit']
          self.dialogcomm.ui.comb_DataBit.setCurrentIndex(
              self.dialogcomm.ui.comb_DataBit.findText(DataBit))
          self.DataBit=int(DataBit)
        except:
          pass
        # print config['CommPar']['StopBit']
        try:
          StopBit=config['CommPar']['StopBit']
          self.dialogcomm.ui.comb_StopBit.setCurrentIndex(
              self.dialogcomm.ui.comb_StopBit.findText(StopBit))
          if StopBit == '1':
              self.StopBit=1
          elif StopBit == '1.5':
              self.StopBit=1.5
          elif StopBit == '2':
              self.StopBit=2
        except:
          pass
        # print config['CommPar']['Timeout']
        try:
          Timeout=config['CommPar']['Timeout']
          self.dialogcomm.ui.Edt_Timeout.setText(Timeout)
          self.Timeout = int(Timeout)
        except:
          pass

        self.Txt_Com.setText(self.Comm + '-'+ BaudR)
        #print self.tr('Load Communication parameter')

    def ComRefresh(self):
        for i in range(self.dialogcomm.ui.comb_Comm.count()):
            self.dialogcomm.ui.comb_Comm.removeItem(0)
        p=self.mb.ComAutoFind()
        self.dialogcomm.ui.comb_Comm.addItems(p)
        print 'ComRefresh'

    def treeChange(self,param, changes):
        #print("treeChange:")
        for param, change, data in changes:
            path = self.ui.widget_parTree.partree.childPath(param)
            if path is not None:
                childName = '.'.join(path)
            else:
                childName = param.name()
            #print('  parameter: %s' % childName)
            #print('  change:    %s' % change)
            #print('  data:      %s' % str(data))
            #print('  ----------')
            self.threadAcq.TreeWrite(self.ui.widget_parTree,childName,param.opts)

 
    #@QtCore.pyqtSlot(str)
    def LogRecord(self,msg):
        configPath = mypath.FilePath('commLog','record.log')
        self.ui.txt_CMD.appendPlainText(msg)
        f = open(configPath, 'a+')
        f.write(msg + '\n')
        f.close()

    def LogHistory(self,msg):
        #print '11111' 此处禁止使用print
        self.Txt_Msg.setText(msg)
        self.ui.txt_CMD_2.appendPlainText(msg)

    def LoadOptionPar(self):
        configPath = mypath.FilePath('Config','Sys.ini')
        config=ConfigObj(configPath, encoding='UTF8')
        # print config['CommPar']['Comm']
        try:
          self.Lang=config['System']['Lang']
          self.dialogoption.ui.comb_Lang.setCurrentIndex(
            self.dialogoption.ui.comb_Lang.findText(self.Lang))
        except:
          pass

    def OptionSet(self):
        self.LoadOptionPar()
        self.dialogoption.show()

    def SaveOption(self):
        print self.tr('Save Option')
        configPath = mypath.FilePath('Config','Sys.ini')
        config=ConfigObj(configPath, encoding='UTF8')
        config['System']={}
        config['System']['Lang']=self.dialogoption.ui.comb_Lang.currentText()
        config.write()
        print self.tr('Saved!')

    def UpgradeShow(self):
        self.dialogupgrade.show()

    def Upgrade(self):
        pass

    def AboutShow(self):
        self.dialogabout.show()

