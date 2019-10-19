# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#


import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.Point import Point


class QtGraphWrapper(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.graph = pg.PlotWidget()
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.graph)
        self.layout.setMargin(0)
        self.setLayout(self.layout)

        self.legend = self.graph.addLegend()
        self.color = ['r', 'g', 'b', 'y', 'c',
                      'm', (195, 46, 212), (250, 194, 5), (19, 234, 201), (54, 55, 55), (237, 177, 32), (119, 172, 48)]
        self.pen = []
        self.ArrLen = 0

        # cross hair
        self.vLine = pg.InfiniteLine(
            angle=90, movable=False, pen=(255, 255, 255))
        self.hLine = pg.InfiniteLine(
            angle=0, movable=False, pen=(255, 255, 255))
        self.graph.addItem(self.vLine, ignoreBounds=True)
        self.graph.addItem(self.hLine, ignoreBounds=True)
        # reg mouse
        self.graph.scene().sigMouseMoved.connect(self.mouseMoved)
        # self.graph.scene().sigMouseHover.connect(self.mouseHover)

        self.text = pg.TextItem("", anchor=(0.5, -1.0))
        self.text.setParentItem(self.legend)
        self.text.setPos(100, -41)

    def LoadInit(self, pars):
        # self.data1 = 100 + 150 * \
        #    pg.gaussianFilter(np.random.random(size=100), 10) + \
        #    30 * np.random.random(size=100)
        # self.data2 = 150 + 150 * \
        #    pg.gaussianFilter(np.random.random(size=100), 10) + \
        #    30 * np.random.random(size=100)
        #self.p1 = self.graph.plot(self.data1, pen="r")
        #self.p2 = self.graph.plot(self.data2, pen="g")
        try:
            self.InitData()
        except Exception as e:
            raise e

        self.pen = []
        self.dataY = []
        self.ArrLen = len(pars[0]['children'])
        for index, item in enumerate(pars[0]['children']):
            #print item['name']
            self.dataY.append(np.array([]))
            self.pen.append(self.graph.plot(
                np.array([]), pen=self.color[index], symbolBrush=self.color[index], symbolSize=1, name=item['name']))
        #print self.pen

    def InitData(self):
        for i in range(self.ArrLen):
            self.pen[i].setData([], [])
        for i in range(len(self.pen)):
            self.pen.pop(0)
            self.legend.items.pop(0)

    def Update(self, dt_x, arrval_y):
        # self.data1, self.data2 = np.append(
        #    self.data1, arrval_y), np.append(self.data2, arrval_y+3)
        # self.p1.setData(self.data1)
        # self.p2.setData(self.data2)
        for i in range(self.ArrLen):
            self.dataY[i] = np.append(self.dataY[i], arrval_y[i])
            self.pen[i].setData(self.dataY[i])

    def mouseMoved(self, evt):

        if self.graph.sceneRect().contains(evt):
            mousePoint = self.graph.mapToView(evt)
            index = int(mousePoint.x())
            if index > 0 and index < len(self.dataY[0]):
                s = '\n\n'.join(str(self.dataY[i][index])
                                for i in range(self.ArrLen))
                self.text.setText(s)
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())
