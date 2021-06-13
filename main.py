from mainWindow import Ui_MainWindow
import ntpath
import os
import sys

from PyQt5 import QtGui, QtWidgets ,QtCore , QtSerialPort
from PyQt5.QtCore import Qt

from scipy.io import loadmat
import matplotlib.pyplot as plt
import scipy.io
# import ecg_plot
import collections
import random
import time
import math
import numpy as np
import time
from scipy.io import wavfile 
import serial as sr
import statistics as stats




class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.yGraph=np.array([])
        self.xGraph=np.arange(0,len(self.yGraph))
        self.xGraph2=[]
        self.yGraph2=[]
        self.xGraph3=[]
        self.yGraph3=[]
        self.xGraph4=[]
        self.yGraph4=[]
        self.PlotValue=2
        self.PlotValue2=2
        self.PlotValue3=2
        self.PlotValue4=2
        self.PlotValue5=2
        self.lastIndex=0
        self.lastIndex2=0
        self.lastIndex3=0
        self.lastIndex4=0
        self.IncreaseValue=10
        self.cg1=0
        self.cg2=0
        self.cg3=0
        self.cg4=0
        self.graph1=self.ui.Graph1
        self.graph2=self.ui.Graph2
        self.graph3=self.ui.Graph2_2
        self.label=self.ui.label
        self.label2=self.ui.label_2
        self.label3=self.ui.label_3
        # self.graph4=self.ui.Graph4
        self.Start_1=self.ui.pushButton
        self.Start_1.clicked.connect(self.B1)
        data=np.array([])
        self.s=QtSerialPort.QSerialPort("COM4")
        self.s.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
        self.s.errorOccurred.connect(self.handle_error)
        self.s.readyRead.connect(self.handle_ready_read)
        self.s.open(QtCore.QIODevice.ReadWrite)
        self.newValue=0
        self.i=0
        self.lcd1=self.ui.lcdNumber
        self.lcd2=self.ui.lcdNumber_2
        self.lcd3=self.ui.lcdNumber_3
        self.temperature=[]
        # self.UCL=0
        # self.LCL=0
        # self.CL=0
        # self.bcl=0
        # self.blcl=0
        # self.bucl=0

    def handle_ready_read(self):
        while self.s.canReadLine():
            codec = QtCore.QTextCodec.codecForName("UTF-8")
            line = codec.toUnicode(self.s.readLine()).strip().strip('\x00')
            try:
                # print(line)
                value = float(line)
            except ValueError as e:
                print("error", e)
            else:
                self.newValue=value
                self.temperature.append(value)
                print(self.newValue)

    def handle_error(self, error):
        if error == QtSerialPort.QSerialPort.NoError:
            return
        # print(error, self.s.errorString())

       



    def B1(self):
        self.Browse_Handler2()
        self.Browse_Handler3()
        self.cg3=1
        self.cg1=1
        self.cg2=1
        self.Start_Draw()


    def chart(self,Xarray,Yarray):
        samplerate=100
        samples=[]
        samplesize=4
        means=[]
        ranges=[]
        #print(len(self.yGraph2))
        for w in range(0,len(Xarray),samplerate):
                samples.append(random.sample(Yarray, samplesize))

                #print("inside loop",samples)
        for sample in samples:
            x_bar=stats.mean(sample)
            R=max(sample)-min(sample)
            means.append(x_bar)
            ranges.append(R)
    
        Rdbar=stats.mean(ranges)
        xdbar=stats.mean(means)
        self.UCL=xdbar+0.73*Rdbar
        print("ucl is:",self.UCL)
        self.CL=xdbar
        self.LCL=xdbar-0.73*Rdbar
        print("lcl is:",self.LCL)
        print("cl is:",self.CL)
        self.bucl=2.28*Rdbar
        self.blcl=0*Rdbar
        self.bcl=Rdbar


    def Start_Draw(self):
        while True:
                # if self.cg1==1 :
                #     self.yGraph=np.append(self.yGraph,self.newValue)

                #     self.xGraph=np.arange(0,len(self.yGraph))

                #     self.chart(self.xGraph,self.temperature)

                #     self.graph1.clear()
                #     self.s.errorOccurred.connect(self.handle_error)
                #     self.s.readyRead.connect(self.handle_ready_read)
                #     self.s.open(QtCore.QIODevice.ReadWrite)
                    
                #     new_info1="Temperature Acquired Sensor Signal with UCL = "+str(self.UCL) + " , CL = " +str(self.CL) + " , and  LCL = " +str(self.LCL)
                #     self.label.setText(new_info1) 
                #     UCL=len(self.xGraph)*[self.UCL]
                #     LCL=len(self.xGraph)*[self.LCL]
                #     CL = len(self.xGraph)*[self.CL]
                    
                #     print("ucl =",UCL)
                #     self.graph1.plot(self.xGraph[0:self.PlotValue],UCL[0:self.PlotValue])
                #     self.graph1.plot(self.xGraph[0:self.PlotValue],LCL[0:self.PlotValue])
                #     self.graph1.plot(self.xGraph[0:self.PlotValue],CL[0:self.PlotValue])
                   
                #     self.graph1.plot(self.xGraph[0:self.PlotValue],self.yGraph[0:self.PlotValue],pen=(65))
                #     self.lcd1.display(self.newValue)
                #     self.PlotValue+=self.IncreaseValue
                #     self.lastIndex+=self.PlotValue

                #     check1=self.newValue
                    
                #     if check1>self.UCL or check1<self.LCL :
                #             self.lcd1.setStyleSheet("""QLCDNumber { 
                #                                     background-color: red; 
                #                                     color: white; }""")
                #     else:
                #             self.lcd1.setStyleSheet("""QLCDNumber { 
                #                                     background-color: white; 
                #                                     color: black; }""")
                #     # self.graph1.setXRange(-20+self.i, self.lastIndex, padding=0)
                #     self.i+=20
                    
                #     # self.lcd1.display()
                #     QtCore.QCoreApplication.processEvents()
                    

                if self.cg2==1 :
                    self.chart(self.xGraph2,self.yGraph2)

                    UCL=len(self.xGraph2)*[self.UCL]
                    LCL=len(self.xGraph2)*[self.LCL]
                    CL = len(self.xGraph2)*[self.CL]
                    new_info2="ECG Signal X-chart with UCL = "+str(self.UCL) + " , CL = " +str(self.CL) + " , and  LCL = " +str(self.LCL)
                    self.label2.setText(new_info2) 
                    self.graph2.clear()

                    self.graph2.plot(self.xGraph2[0:self.PlotValue2],UCL[0:self.PlotValue2])
                    self.graph2.plot(self.xGraph2[0:self.PlotValue2],LCL[0:self.PlotValue2])
                    self.graph2.plot(self.xGraph2[0:self.PlotValue2],CL[0:self.PlotValue2])
                    self.graph2.plot(self.xGraph2[0:self.PlotValue2],self.yGraph2[0:self.PlotValue2],pen=(70))
                    self.lcd2.display(self.yGraph2[self.PlotValue2])

                    check=self.yGraph2[0:self.PlotValue2]
                    for checks in check:
                        if checks>self.UCL or checks<self.LCL :
                            self.lcd2.setStyleSheet("""QLCDNumber { 
                                                    background-color: red; 
                                                    color: white; }""")
                        else:
                            self.lcd2.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")
                    
                    self.PlotValue2+=self.IncreaseValue
                    self.lastIndex2+=self.IncreaseValue
                    QtCore.QCoreApplication.processEvents()

                if self.cg3==1 :
                    self.chart(self.xGraph3,self.yGraph3)

                    bucl=len(self.xGraph3)*[self.bucl]
                    blcl=len(self.xGraph3)*[self.blcl]
                    bcl = len(self.xGraph3)*[self.bcl]
                    new_info3="EMG Signal R-chart with UCL = "+str(self.bucl) + " , CL = " +str(self.bcl) + " , and  LCL = " +str(self.blcl)
                    self.label3.setText(new_info3) 
                    self.graph3.clear()

                    self.graph3.plot(self.xGraph3[0:self.PlotValue3],bucl[0:self.PlotValue3])
                    self.graph3.plot(self.xGraph3[0:self.PlotValue3],blcl[0:self.PlotValue3])
                    self.graph3.plot(self.xGraph3[0:self.PlotValue3],bcl[0:self.PlotValue3])
                    self.graph3.plot(self.xGraph3[0:self.PlotValue3],self.yGraph3[0:self.PlotValue3],pen=(75))
                    self.lcd3.display(self.yGraph3[self.PlotValue3])

                    check3=self.yGraph3[0:self.PlotValue3]
                    for checks3 in check3:
                        if checks3>self.bucl or checks3<self.blcl :
                            self.lcd3.setStyleSheet("""QLCDNumber { 
                                                    background-color: red; 
                                                    color: white; }""")
                        else:
                            self.lcd3.setStyleSheet("""QLCDNumber { 
                                                    background-color: white; 
                                                    color: black; }""")

                    self.PlotValue3+=self.IncreaseValue
                    self.lastIndex3+=self.IncreaseValue
                    QtCore.QCoreApplication.processEvents()


                
                QtCore.QCoreApplication.processEvents()
                time.sleep(0.01)    
        self.s.close() 

                              
    def Browse_Handler2(self):
        filePath = (['C:/Users/modyf/Desktop/New folder (8)/output.txt'], 'All Files (*)')
        self.graph2.clear()
        temp=(['C:/Users/modyf/Desktop/New folder (8)/output.txt'], 'All Files (*)')
        print(temp)
        for vs in temp[0]:
            
            self.ext = os.path.splitext(vs)[-1].lower()
            if self.ext==".txt":
                      
                      
                      pinky=filePath[0]
                      
                      with open (pinky[0],'r') as f:
                          print('d5l')
                          for data1 in f:
                               
                                data= data1.split(" ")
                                l = float(data[0])
                                k = float(data[1])
                                self.xGraph2.append(l)
                                self.yGraph2.append(k)
                                                               
                 

    def Browse_Handler3(self):
        filePath = (['C:/Users/modyf/Desktop/New folder (8)/emg_neuropathy.txt'], 'All Files (*)')
        self.graph3.clear()
        temp=(['C:/Users/modyf/Desktop/New folder (8)/emg_neuropathy.txt'], 'All Files (*)')
        print(temp)

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

           






def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
