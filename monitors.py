# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import time
from scipy.io import wavfile
import os

class Ui_SignalPlotting(object):
    def setupUi(self, SignalPlotting):
        self.samplerate=47000.6
        self.x=[]
        self.y=[]
        self.cg=[]
        self.xGraph2=[]
        self.yGraph2=[]
        self.xGraph3=[]
        self.yGraph3=[]
        self.xGraph4=[]
        self.yGraph4=[]
        self.xGraph5=[]
        self.yGraph5=[]
        self.lastIndex=0
        self.lastIndex2=0
        self.lastIndex3=0
        self.lastIndex4=0
        self.lastIndex5=0
        self.PlotValue=2
        self.PlotValue2=2
        self.PlotValue3=2
        self.PlotValue4=2
        self.PlotValue5=2
        self.IncreaseValue=10
        self.Pause=True
        self.Pause2=True
        self.Pause3=True
        self.Pause4=True
        self.Pause5=True
        SignalPlotting.setObjectName("SignalPlotting")
        SignalPlotting.resize(1127, 771)
        self.centralwidget = QtWidgets.QWidget(SignalPlotting)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Signal_1 = QtWidgets.QLabel(self.centralwidget)
        self.Signal_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_1.setFont(font)
        self.Signal_1.setObjectName("Signal_1")
        self.gridLayout.addWidget(self.Signal_1, 0, 0, 1, 2)
        self.Signal_2 = QtWidgets.QLabel(self.centralwidget)
        self.Signal_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_2.setFont(font)
        self.Signal_2.setObjectName("Signal_2")
        self.gridLayout.addWidget(self.Signal_2, 0, 5, 1, 3)
        self.Signal_3 = QtWidgets.QLabel(self.centralwidget)
        self.Signal_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_3.setFont(font)
        self.Signal_3.setObjectName("Signal_3")
        self.gridLayout.addWidget(self.Signal_3, 0, 11, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Signal_Plot_1 = PlotWidget(self.centralwidget)
        self.Signal_Plot_1.setEnabled(True)
        self.Signal_Plot_1.setAcceptDrops(False)
        self.Signal_Plot_1.setObjectName("Signal_Plot_1")
        self.verticalLayout.addWidget(self.Signal_Plot_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Signal_Plot_2 = PlotWidget(self.centralwidget)
        self.Signal_Plot_2.setEnabled(True)
        self.Signal_Plot_2.setAcceptDrops(False)
        self.Signal_Plot_2.setObjectName("Signal_Plot_2")
        self.verticalLayout_4.addWidget(self.Signal_Plot_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 5, 1, 6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Signal_Plot_3 = PlotWidget(self.centralwidget)
        self.Signal_Plot_3.setEnabled(True)
        self.Signal_Plot_3.setAcceptDrops(False)
        self.Signal_Plot_3.setObjectName("Signal_Plot_3")
        self.verticalLayout_5.addWidget(self.Signal_Plot_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 11, 1, 5)
        self.Start_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Start_1.setEnabled(True)
        self.Start_1.setObjectName("Start_1")
        self.gridLayout.addWidget(self.Start_1, 2, 0, 1, 1)
        self.Pause_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_1.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Pause_1.setFont(font)
        self.Pause_1.setAcceptDrops(False)
        self.Pause_1.setAutoFillBackground(False)
        self.Pause_1.setAutoDefault(False)
        self.Pause_1.setDefault(False)
        self.Pause_1.setFlat(False)
        self.Pause_1.setObjectName("Pause_1")
        self.gridLayout.addWidget(self.Pause_1, 2, 1, 1, 2)
        self.Resume_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_1.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Resume_1.setFont(font)
        self.Resume_1.setAcceptDrops(False)
        self.Resume_1.setAutoFillBackground(False)
        self.Resume_1.setAutoDefault(False)
        self.Resume_1.setDefault(False)
        self.Resume_1.setFlat(False)
        self.Resume_1.setObjectName("Resume_1")
        self.gridLayout.addWidget(self.Resume_1, 2, 3, 1, 2)
        self.Start_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Start_2.setEnabled(True)
        self.Start_2.setObjectName("Start_2")
        self.gridLayout.addWidget(self.Start_2, 2, 5, 1, 2)
        self.Pause_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_2.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Pause_2.setFont(font)
        self.Pause_2.setAcceptDrops(False)
        self.Pause_2.setAutoFillBackground(False)
        self.Pause_2.setAutoDefault(False)
        self.Pause_2.setDefault(False)
        self.Pause_2.setFlat(False)
        self.Pause_2.setObjectName("Pause_2")
        self.gridLayout.addWidget(self.Pause_2, 2, 7, 1, 2)
        self.Resume_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_2.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Resume_2.setFont(font)
        self.Resume_2.setAcceptDrops(False)
        self.Resume_2.setAutoFillBackground(False)
        self.Resume_2.setAutoDefault(False)
        self.Resume_2.setDefault(False)
        self.Resume_2.setFlat(False)
        self.Resume_2.setObjectName("Resume_2")
        self.gridLayout.addWidget(self.Resume_2, 2, 9, 1, 2)
        self.Start_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Start_3.setEnabled(True)
        self.Start_3.setObjectName("Start_3")
        self.gridLayout.addWidget(self.Start_3, 2, 11, 1, 2)
        self.Pause_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_3.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Pause_3.setFont(font)
        self.Pause_3.setAcceptDrops(False)
        self.Pause_3.setAutoFillBackground(False)
        self.Pause_3.setAutoDefault(False)
        self.Pause_3.setDefault(False)
        self.Pause_3.setFlat(False)
        self.Pause_3.setObjectName("Pause_3")
        self.gridLayout.addWidget(self.Pause_3, 2, 13, 1, 2)
        self.Resume_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_3.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Resume_3.setFont(font)
        self.Resume_3.setAcceptDrops(False)
        self.Resume_3.setAutoFillBackground(False)
        self.Resume_3.setAutoDefault(False)
        self.Resume_3.setDefault(False)
        self.Resume_3.setFlat(False)
        self.Resume_3.setObjectName("Resume_3")
        self.gridLayout.addWidget(self.Resume_3, 2, 15, 1, 1)
        self.Signal_4 = QtWidgets.QLabel(self.centralwidget)
        self.Signal_4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_4.setFont(font)
        self.Signal_4.setObjectName("Signal_4")
        self.gridLayout.addWidget(self.Signal_4, 3, 2, 1, 3)
        self.Signal_5 = QtWidgets.QLabel(self.centralwidget)
        self.Signal_5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_5.setFont(font)
        self.Signal_5.setObjectName("Signal_5")
        self.gridLayout.addWidget(self.Signal_5, 3, 8, 1, 3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Signal_Plot_4 = PlotWidget(self.centralwidget)
        self.Signal_Plot_4.setEnabled(True)
        self.Signal_Plot_4.setAcceptDrops(False)
        self.Signal_Plot_4.setObjectName("Signal_Plot_4")
        self.verticalLayout_6.addWidget(self.Signal_Plot_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 2, 1, 6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Signal_Plot_5 = PlotWidget(self.centralwidget)
        self.Signal_Plot_5.setEnabled(True)
        self.Signal_Plot_5.setAcceptDrops(False)
        self.Signal_Plot_5.setObjectName("Signal_Plot_5")
        self.verticalLayout_7.addWidget(self.Signal_Plot_5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout_10, 4, 8, 1, 6)
        self.Start_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Start_4.setEnabled(True)
        self.Start_4.setObjectName("Start_4")
        self.gridLayout.addWidget(self.Start_4, 5, 2, 1, 2)
        self.Pause_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_4.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Pause_4.setFont(font)
        self.Pause_4.setAcceptDrops(False)
        self.Pause_4.setAutoFillBackground(False)
        self.Pause_4.setAutoDefault(False)
        self.Pause_4.setDefault(False)
        self.Pause_4.setFlat(False)
        self.Pause_4.setObjectName("Pause_4")
        self.gridLayout.addWidget(self.Pause_4, 5, 4, 1, 2)
        self.Resume_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_4.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Resume_4.setFont(font)
        self.Resume_4.setAcceptDrops(False)
        self.Resume_4.setAutoFillBackground(False)
        self.Resume_4.setAutoDefault(False)
        self.Resume_4.setDefault(False)
        self.Resume_4.setFlat(False)
        self.Resume_4.setObjectName("Resume_4")
        self.gridLayout.addWidget(self.Resume_4, 5, 6, 1, 2)
        self.Start_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Start_5.setEnabled(True)
        self.Start_5.setObjectName("Start_5")
        self.gridLayout.addWidget(self.Start_5, 5, 8, 1, 2)
        self.Pause_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_5.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Pause_5.setFont(font)
        self.Pause_5.setAcceptDrops(False)
        self.Pause_5.setAutoFillBackground(False)
        self.Pause_5.setAutoDefault(False)
        self.Pause_5.setDefault(False)
        self.Pause_5.setFlat(False)
        self.Pause_5.setObjectName("Pause_5")
        self.gridLayout.addWidget(self.Pause_5, 5, 10, 1, 2)
        self.Resume_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Resume_5.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Resume_5.setFont(font)
        self.Resume_5.setAcceptDrops(False)
        self.Resume_5.setAutoFillBackground(False)
        self.Resume_5.setAutoDefault(False)
        self.Resume_5.setDefault(False)
        self.Resume_5.setFlat(False)
        self.Resume_5.setObjectName("Resume_5")
        self.gridLayout.addWidget(self.Resume_5, 5, 12, 1, 2)
        self.Browse_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_4.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Browse_4.setFont(font)
        self.Browse_4.setAcceptDrops(False)
        self.Browse_4.setAutoFillBackground(False)
        self.Browse_4.setAutoDefault(False)
        self.Browse_4.setDefault(False)
        self.Browse_4.setFlat(False)
        self.Browse_4.setObjectName("Browse_4")
        self.gridLayout.addWidget(self.Browse_4, 3, 6, 1, 2)
        self.Browse_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_5.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Browse_5.setFont(font)
        self.Browse_5.setAcceptDrops(False)
        self.Browse_5.setAutoFillBackground(False)
        self.Browse_5.setAutoDefault(False)
        self.Browse_5.setDefault(False)
        self.Browse_5.setFlat(False)
        self.Browse_5.setObjectName("Browse_5")
        self.gridLayout.addWidget(self.Browse_5, 3, 12, 1, 2)
        self.Browse_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_3.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Browse_3.setFont(font)
        self.Browse_3.setAcceptDrops(False)
        self.Browse_3.setAutoFillBackground(False)
        self.Browse_3.setAutoDefault(False)
        self.Browse_3.setDefault(False)
        self.Browse_3.setFlat(False)
        self.Browse_3.setObjectName("Browse_3")
        self.gridLayout.addWidget(self.Browse_3, 0, 15, 1, 1)
        self.Browse_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_2.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Browse_2.setFont(font)
        self.Browse_2.setAcceptDrops(False)
        self.Browse_2.setAutoFillBackground(False)
        self.Browse_2.setAutoDefault(False)
        self.Browse_2.setDefault(False)
        self.Browse_2.setFlat(False)
        self.Browse_2.setObjectName("Browse_2")
        self.gridLayout.addWidget(self.Browse_2, 0, 9, 1, 2)
        self.Browse_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_1.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.Browse_1.setFont(font)
        self.Browse_1.setAcceptDrops(False)
        self.Browse_1.setAutoFillBackground(False)
        self.Browse_1.setAutoDefault(False)
        self.Browse_1.setDefault(False)
        self.Browse_1.setFlat(False)
        self.Browse_1.setObjectName("Browse_1")
        self.gridLayout.addWidget(self.Browse_1, 0, 3, 1, 2)
        SignalPlotting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignalPlotting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        SignalPlotting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignalPlotting)
        self.statusbar.setObjectName("statusbar")
        SignalPlotting.setStatusBar(self.statusbar)

        self.retranslateUi(SignalPlotting)
        self.Signal_Plot_1.windowIconChanged['QIcon'].connect(self.Start_1.repaint)
        self.Signal_Plot_1.windowIconChanged['QIcon'].connect(self.Pause_1.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(SignalPlotting)


    
        self.Start_1.clicked.connect(lambda:self.B1())
        self.Pause_1.clicked.connect(lambda:self.Pause_Draw1())
        self.Resume_1.clicked.connect(lambda :self.Resume_Draw())

    
        self.Start_2.clicked.connect(lambda :self.B2())
        self.Pause_2.clicked.connect(lambda:self.Pause_Draw2())
        self.Resume_2.clicked.connect(lambda :self.Resume_Draw2())

        self.Start_3.clicked.connect(lambda:self.B3())
        self.Pause_3.clicked.connect(lambda:self.Pause_Draw3())
        self.Resume_3.clicked.connect(lambda :self.Resume_Draw3())

        self.Start_4.clicked.connect(lambda :self.B4())
        self.Pause_4.clicked.connect(lambda:self.Pause_Draw4())
        self.Resume_4.clicked.connect(lambda :self.Resume_Draw4())

        self.Start_5.clicked.connect(lambda:self.B5())
        self.Pause_5.clicked.connect(lambda:self.Pause_Draw5())
        self.Resume_5.clicked.connect(lambda :self.Resume_Draw5())

    def retranslateUi(self, SignalPlotting):
        _translate = QtCore.QCoreApplication.translate
        SignalPlotting.setWindowTitle(_translate("SignalPlotting", "MainWindow"))
        self.Signal_1.setText(_translate("SignalPlotting", "Signal#1"))
        self.Signal_2.setText(_translate("SignalPlotting", "Signal#2"))
        self.Signal_3.setText(_translate("SignalPlotting", "Signal#3"))
        self.Start_1.setText(_translate("SignalPlotting", "Start"))
        self.Pause_1.setText(_translate("SignalPlotting", "pause"))
        self.Resume_1.setText(_translate("SignalPlotting", "Resume"))
        self.Start_2.setText(_translate("SignalPlotting", "Start"))
        self.Pause_2.setText(_translate("SignalPlotting", "pause"))
        self.Resume_2.setText(_translate("SignalPlotting", "Resume"))
        self.Start_3.setText(_translate("SignalPlotting", "Start"))
        self.Pause_3.setText(_translate("SignalPlotting", "pause"))
        self.Resume_3.setText(_translate("SignalPlotting", "Resume"))
        self.Signal_4.setText(_translate("SignalPlotting", "Signal#4"))
        self.Signal_5.setText(_translate("SignalPlotting", "Signal#5"))
        self.Start_4.setText(_translate("SignalPlotting", "Start"))
        self.Pause_4.setText(_translate("SignalPlotting", "pause"))
        self.Resume_4.setText(_translate("SignalPlotting", "Resume"))
        self.Start_5.setText(_translate("SignalPlotting", "Start"))
        self.Pause_5.setText(_translate("SignalPlotting", "pause"))
        self.Resume_5.setText(_translate("SignalPlotting", "Resume"))
        self.Browse_4.setText(_translate("SignalPlotting", "Browse"))
        self.Browse_5.setText(_translate("SignalPlotting", "Browse"))
        self.Browse_3.setText(_translate("SignalPlotting", "Browse"))
        self.Browse_2.setText(_translate("SignalPlotting", "Browse"))
        self.Browse_1.setText(_translate("SignalPlotting", "Browse"))
        self.Browse_1.clicked.connect(self.Browse_Handler)
        self.Browse_2.clicked.connect(self.Browse_Handler2)
        self.Browse_3.clicked.connect(self.Browse_Handler3)
        self.Browse_4.clicked.connect(self.Browse_Handler4)
        self.Browse_5.clicked.connect(self.Browse_Handler5)


    ####
    def Browse_Handler(self):
        filePath = QtWidgets.QFileDialog.getOpenFileNames()
        self.Signal_Plot_1.clear()
        temp=filePath
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                     
                      with open (pinky[0],'r') as f:
                         
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.x.append(l)
                                self.y.append(k)
                                                    
            elif self.ext==".csv" or self.ext==".xsl":
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         for data1 in f:
                             data = data1.split(",")
                             l = float(data[0])
                             k = float(data[1])
                             self.x.append(l)
                             self.y.append(k)
            elif self.ext==".wav":
                pinky=filePath[0]
                samplerate, self.y=wavfile.read(pinky[0])
                self.x=np.arange(len(self.y))/float(samplerate)

            else:
                return                      

     
    def Browse_Handler2(self):
        filePath = QtWidgets.QFileDialog.getOpenFileNames()
        self.Signal_Plot_2.clear()
        temp=filePath
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                          
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.xGraph2.append(l)
                                self.yGraph2.append(k)
                                                    
            elif self.ext==".csv" or self.ext==".xsl":
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         for data1 in f:
                             data = data1.split(",")
                             l = float(data[0])
                             k = float(data[1])
                             self.xGraph2.append(l)
                             self.yGraph2.append(k)
            elif self.ext==".wav":
                pinky=filePath[0]
                samplerate, self.yGraph2=wavfile.read(pinky[0])
                self.xGraph2=np.arange(len(self.yGraph2))/float(samplerate)

            else:
                return                         
                 

    def Browse_Handler3(self):
        filePath = QtWidgets.QFileDialog.getOpenFileNames()
        self.Signal_Plot_3.clear()
        temp=filePath
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                          
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.xGraph3.append(l)
                                self.yGraph3.append(k)
                                                    
            elif self.ext==".csv" or self.ext==".xsl":
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         for data1 in f:
                             data = data1.split(",")
                             l = float(data[0])
                             k = float(data[1])
                             self.xGraph3.append(l)
                             self.yGraph3.append(k)
            elif self.ext==".wav":
                pinky=filePath[0]
                samplerate, self.yGraph3=wavfile.read(pinky[0])
                self.xGraph3=np.arange(len(self.yGraph3))/float(samplerate)

            else:
                return                      

    def Browse_Handler4(self):
        filePath = QtWidgets.QFileDialog.getOpenFileNames()
        self.Signal_Plot_4.clear()
        temp=filePath
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.xGraph4.append(l)
                                self.yGraph4.append(k)
                                                    
            elif self.ext==".csv" or self.ext==".xsl":
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         for data1 in f:
                             data = data1.split(",")
                             l = float(data[0])
                             k = float(data[1])
                             self.xGraph4.append(l)
                             self.yGraph4.append(k)
            elif self.ext==".wav":
                pinky=filePath[0]
                samplerate, self.yGraph4=wavfile.read(pinky[0])
                self.xGraph4=np.arange(len(self.yGraph4))/float(samplerate)

            else:
                return                      
    def Browse_Handler5(self):
        filePath = QtWidgets.QFileDialog.getOpenFileNames()
        self.Signal_Plot_5.clear()
        temp=filePath
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                    
                      with open (pinky[0],'r') as f:
                         
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.xGraph5.append(l)
                                self.yGraph5.append(k)
                                                    
            elif self.ext==".csv" or self.ext==".xsl":
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                         for data1 in f:
                             data = data1.split(",")
                             l = float(data[0])
                             k = float(data[1])
                             self.xGraph5.append(l)
                             self.yGraph5.append(k)
            elif self.ext==".wav":
                pinky=filePath[0]
                samplerate, self.yGraph5=wavfile.read(pinky[0])
                self.xGraph5=np.arange(len(self.yGraph5))/float(samplerate)

            else:
                return                           
    ###   
    def Start_Draw(self):
        while True:
            if 1 in self.cg :
                if self.Pause==True:
                

                 self.Signal_Plot_1.plot(self.x[0:self.PlotValue],self.y[0:self.PlotValue],pen=(50))
                 self.PlotValue+=self.IncreaseValue
                 self.lastIndex+=self.IncreaseValue
                 QtCore.QCoreApplication.processEvents()
                 
            if 2 in self.cg  :
                if self.Pause2==True:
                  self.Signal_Plot_2.plot(self.xGraph2[0:self.PlotValue2],self.yGraph2[0:self.PlotValue2],pen=(70))
                  self.PlotValue2+=self.IncreaseValue
                  self.lastIndex2+=self.IncreaseValue
                  QtCore.QCoreApplication.processEvents()
               
            if 3 in self.cg :
                if self.Pause3==True:
                    
                  self.Signal_Plot_3.plot(self.xGraph3[0:self.PlotValue3],self.yGraph3[0:self.PlotValue3],pen=(75))
                  self.PlotValue3+=self.IncreaseValue
                  self.lastIndex3+=self.IncreaseValue
                  QtCore.QCoreApplication.processEvents()
                  
            if 4 in self.cg :
                if self.Pause4==True:
                 self.Signal_Plot_4.plot(self.xGraph4[0:self.PlotValue4],self.yGraph4[0:self.PlotValue4],pen=(66))
                 self.PlotValue4+=self.IncreaseValue
                 self.lastIndex4+=self.IncreaseValue
                 QtCore.QCoreApplication.processEvents()
                 
            if 5 in self.cg :
                if self.Pause5==True:
                 self.Signal_Plot_5.plot(self.xGraph5[0:self.PlotValue5],self.yGraph5[0:self.PlotValue5],pen=(40))
                 self.PlotValue5+=self.IncreaseValue
                 self.lastIndex5+=self.IncreaseValue
                 QtCore.QCoreApplication.processEvents()
                              
            QtCore.QCoreApplication.processEvents()     

   
    def Pause_Draw1(self):
        if self.Pause==True:
            self.Pause=False

    def Pause_Draw2(self):

       if self.Pause2==True:
            self.Pause2=False 
    def Pause_Draw3(self):
       
       if self.Pause3==True:
            self.Pause3=False
    def Pause_Draw4(self):
       
       if self.Pause4==True:
            self.Pause4=False
    def Pause_Draw5(self):
      
       if self.Pause5==True:
            self.Pause5=False

    def Resume_Draw(self):
        if self.Pause==False:
          self.Pause=True
          self.Start_Draw()


    def Resume_Draw2(self):
        self.Pause2=True
        self.Start_Draw()
    def Resume_Draw3(self):
        self.Pause3=True
        self.Start_Draw()
    def Resume_Draw4(self):
        self.Pause4=True
        self.Start_Draw()
    def Resume_Draw5(self):
        self.Pause5=True
        self.Start_Draw()

    def B1(self):
        self.cg.append(1)
        self.Start_Draw()

    def B2(self):
        self.cg.append(2) 
        self.Start_Draw() 

    def B3(self):
        self.cg.append(3)  
        self.Start_Draw()
    def B4(self):
        self.cg.append(4)  
        self.Start_Draw()
    def B5(self):
        self.cg.append(5) 
        self.Start_Draw()              
from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignalPlotting = QtWidgets.QMainWindow()
    ui = Ui_SignalPlotting()
    ui.setupUi(SignalPlotting)
    SignalPlotting.show()
    sys.exit(app.exec_())

