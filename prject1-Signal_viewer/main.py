from PyQt5 import QtWidgets , QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os
import main_gui
import pandas as pd
from scipy import signal
import numpy as np
from PyQt5.QtWidgets import QMessageBox
class MainWindow(QtWidgets.QMainWindow , main_gui.Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.view_1() #start the programm with one signal viewed

        #########variables######################

        self.current_widget = self.widget_1 #idicate the selected widget in groupBox
        #####timers for plots####
        self.timer1=0
        self.timer2=0
        self.timer3=0
        ######plot configuration#####
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.widget_configuration(self.widget_1 , "Signal 1")
        self.widget_configuration(self.widget_2, "Signal 2")
        self.widget_configuration(self.widget_3, "Signal 3")

        self.signals = [0,0,0] #list to store loaded signals
        self.x = [0,0,0] ### x , y to recieve data for plotting
        self.y = [0,0,0]
        #########actions triggeration###########
        self.actionOpen.triggered.connect(self.openfile)
        self.actionToolbar.triggered.connect(self.toggle_tool)
        self.actionStatus_bar.triggered.connect(self.toggle_status)
        self.actionPlay.triggered.connect(self.play)
        self.actionPause.triggered.connect(self.pause)
        self.actionStop.triggered.connect(self.stop)
        self.actionClose.triggered.connect(self.close)
        self.actionZoom_in.triggered.connect(self.zoom_in)
        self.actionZoom_out.triggered.connect(self.zoom_out)
        self.actionSpectrogram.triggered.connect(self.spectro)
        self.action1_Signal.triggered.connect(self.view_1)
        self.action2_Signals.triggered.connect(self.view_2)
        self.action3_Signals.triggered.connect(self.view_3)
        self.actionAbout.triggered.connect(self.pop_up)
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.rightButton.clicked.connect(self.scroll_right)
        self.leftButton.clicked.connect(self.scroll_left)
        self.upButton.clicked.connect(self.scroll_up)
        self.downButton.clicked.connect(self.scroll_down)
        ####chose the current_widget to control it
        self.radioButton_1.toggled.connect(self.select_1)       
        self.radioButton_2.toggled.connect(self.select_2)
        self.radioButton_3.toggled.connect(self.select_3)
        # radiobutton.toggled.connect
    def select_1(self):
        self.current_widget = self.widget_1
    def select_2(self):
        self.current_widget = self.widget_2
    def select_3(self):
        self.current_widget = self.widget_3



        
    #####to load and plot signal#######
    def openfile(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"", "Data files (*.csv)")
        if self.file_path:
            df = pd.read_csv(self.file_path)
            self.reset_widget()
            self.current_widget.setLabel('bottom', "Time (ms)")
            ####control which widget to plot in
            if self.radioButton_1.isChecked():
                self.index1 = 0
                self.signals[0] = self.file_path
                self.file_name = os.path.basename(self.signals[0])
                self.x[0] = df.index
                self.y[0] = df.iloc[:,0]
                self.reset_y(self.y[0])
                self.data_line1 =  self.widget_1.plot(self.x[0], self.y[0],name = self.file_name ,pen=self.pen)
                ##### create a timer for widget1#####
                self.timer1 = QtCore.QTimer()
                self.timer1.setInterval(50)
                self.timer1.timeout.connect(self.update_plot1)
            elif self.radioButton_2.isChecked():
                self.index2 = 0
                self.signals[1] = self.file_path
                self.file_name = os.path.basename(self.signals[1])
                self.x[1] = df.index
                self.y[1] = df.iloc[:,0]
                self.reset_y(self.y[1])
                self.data_line2 =  self.widget_2.plot(self.x[1], self.y[1],name = self.file_name ,pen=self.pen)
                ##### create a timer for widget2#####
                self.timer2 = QtCore.QTimer()
                self.timer2.setInterval(50)
                self.timer2.timeout.connect(self.update_plot2)
            else:
                self.index3 = 0
                self.signals[2] = self.file_path
                self.file_name = os.path.basename(self.signals[1])
                self.x[2] = df.index
                self.y[2] = df.iloc[:,0]
                self.reset_y(self.y[2])
                self.data_line3 =  self.widget_3.plot(self.x[2], self.y[2],name = self.file_name ,pen=self.pen)
                ##### create a timer for widget3#####
                self.timer3 = QtCore.QTimer()
                self.timer3.setInterval(50)
                self.timer3.timeout.connect(self.update_plot3)
            
            ######enable tools to control signal#####
            self.actionZoom_in.setEnabled(True)
            self.actionZoom_out.setEnabled(True)
            self.actionPlay.setEnabled(True)
            self.actionPause.setEnabled(True)
            self.actionStop.setEnabled(True)
            self.actionClose.setEnabled(True)
            self.actionSpectrogram.setEnabled(True)
            self.rightButton.setEnabled(True)
            self.leftButton.setEnabled(True)
            self.upButton.setEnabled(True)
            self.downButton.setEnabled(True)

    ########upate function to make the plot moving###### 
    def update_plot1(self):

        if self.signals[0] != 0:
            self.index1 = self.index1 + 1
            self.widget_1.setXRange(0 + self.index1, 1000 + self.index1, padding=0)
            self.data_line1.setData(self.x[0], self.y[0]) 

    def update_plot2(self):

        if self.signals[1] != 0:
            self.index2 = self.index2 + 1
            self.widget_2.setXRange(0 + self.index2, 1000 + self.index2, padding=0)
            self.data_line2.setData(self.x[1], self.y[1])

    def update_plot3(self):                    
        if self.signals[2] != 0:
            self.index3 = self.index3 + 1
            self.widget_3.setXRange(0 + self.index3, 1000 + self.index3, padding=0)
            self.data_line3.setData(self.x[2], self.y[2]) 
                    
    #######play function to start the movement####
    def play(self):
        if self.radioButton_1.isChecked():
            if self.timer1 == 0:
                pass
            else:
                self.timer1.start()
        elif self.radioButton_2.isChecked():
            if self.timer2 == 0:
                pass
            else:
                self.timer2.start()
        else:
            if self.timer3 == 0:
                pass
            else:
                self.timer3.start()
    #######pause function to pause the movement####
    def pause(self):
        if self.radioButton_1.isChecked():
            if self.timer1 == 0:
                pass
            else:
                self.timer1.stop()
        elif self.radioButton_2.isChecked():
            if self.timer2 == 0:
                pass
            else:
                self.timer2.stop()
        else:
            if self.timer3 == 0:
                pass
            else:
                self.timer3.stop()
    #######stop function to stop the movement and reset the signal plot####
    def stop(self):
        if self.radioButton_1.isChecked():
            if self.timer1 == 0:
                pass
            else:
                self.timer1.stop()
                self.index1 = 0
                self.current_widget.plot(self.x[0], self.y[0], pen=self.pen)
                self.current_widget.setXRange(0, 1000, padding=0)


        elif self.radioButton_2.isChecked():
            if self.timer2 == 0:
                pass
            else:
                self.timer2.stop()
                self.index2 = 0
                self.current_widget.plot(self.x[1], self.y[1], pen=self.pen)
                self.current_widget.setXRange(0, 1000, padding=0)


        else:
            if self.timer3 == 0:
                pass
            else:
                self.timer3.stop()
                self.index3 = 0
                self.current_widget.plot(self.x[2], self.y[2], pen=self.pen)
                self.current_widget.setXRange(0, 1000, padding=0)
    
    #######close function to clear the plot####
    def close(self):
        if self.radioButton_1.isChecked():
            self.timer1 = 0
            self.signals[0] = 0
        elif self.radioButton_2.isChecked():
            self.timer2 = 0
            self.signals[1] = 0
        else:
            self.timer3 = 0
            self.signals[2] = 0
        self.reset_widget()
        if (self.signals[0] == 0) and (self.signals[1] == 0) and (self.signals[2] == 0):
            self.actionZoom_in.setEnabled(False)
            self.actionZoom_out.setEnabled(False)
            self.actionPlay.setEnabled(False)
            self.actionPause.setEnabled(False)
            self.actionStop.setEnabled(False)
            self.actionClose.setEnabled(False)
            self.actionSpectrogram.setEnabled(False)
            self.rightButton.setEnabled(False)
            self.leftButton.setEnabled(False)
            self.upButton.setEnabled(False)
            self.downButton.setEnabled(False)
        
    def spectro(self):
        self.current_widget.clear()
        fs = 1000 ####sampling frequency
        if self.radioButton_1.isChecked():
            self.timer1 = 0
            values = self.y[0]

        elif self.radioButton_2.isChecked():
            self.timer2 = 0
            values = self.y[1]

        else:
            self.timer3 = 0
            values = self.y[2]

        f,t,Sxx = signal.spectrogram(values,fs)

        pg.setConfigOptions(imageAxisOrder='row-major')
        self.img= pg.ImageItem()
        self.current_widget.addItem(self.img)
        # Add a histogram to control the gradient of the image
        self.hist = pg.HistogramLUTItem()
        # Link the histogram to the image
        self.hist.setImageItem(self.img)
        # Fit the min and max levels of the histogram
        self.hist.setLevels(np.min(Sxx), np.max(Sxx))

        self.hist.gradient.restoreState(
                {'mode': 'rgb',
                'ticks': [(0.5, (0, 182, 188, 255)),
                        (1.0, (246, 111, 0, 255)),
                        (0.0, (75, 0, 113, 255))]})
        self.img.setImage(Sxx)

        self.img.scale(t[-1]/np.size(Sxx, axis=1), f[-1]/np.size(Sxx, axis=0))

        self.current_widget.setXRange(0 , t[-1] , padding=0)
        self.current_widget.setYRange(0 , f[-1] , padding=0)

        self.current_widget.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        # Add labels to the axis
        self.current_widget.setLabel('bottom', "Time", units='s')
        
        self.current_widget.setLabel('left', "Frequency", units='Hz')

    ###########functions to control the number of showen plots###
    def view_1(self):
        self.widget_1.show()
        self.widget_2.hide()
        self.widget_3.hide()
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
    def view_2(self):
        self.widget_1.show()
        self.widget_2.show()
        self.widget_3.hide()
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(False)
    def view_3(self):
        self.widget_1.show()
        self.widget_2.show()
        self.widget_3.show()
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
    ##function to show about in popup message
    def pop_up(self):
        msg = QMessageBox()
        msg.setWindowTitle("About...")
        msg.setText('Signalviewer Version 1.0')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText('Copyright (C) 2021 SBME cairo university')
        x = msg.exec_()

    ########function to show and hide the toolbar#####
    def toggle_tool(self, action):

        if action:
            self.toolBar.show()
        else:
            self.toolBar.hide()

    ########function to show and hide the status bar#####
    def toggle_status(self, action):

        if action:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    ######functionts for zoomig in and out
    def zoom_in(self):
        self.current_widget.plotItem.getViewBox().scaleBy((1 / 1.25, 1 / 1.25))
    def zoom_out(self):
        self.current_widget.plotItem.getViewBox().scaleBy((1.25,1.25))

    ######functionts for scrolling
    def scroll_right(self):
        x_range = self.current_widget.getViewBox().state['viewRange'][0] # the visible range in x axis
        rx = 0.1 * (x_range[1] - x_range[0])
        self.current_widget.setXRange((x_range[0]+rx),(x_range[1]+rx) , padding=0)

    def scroll_left(self):
        x_range = self.current_widget.getViewBox().state['viewRange'][0] # the visible range in x axis
        rx = 0.1 * (x_range[1] - x_range[0])
        self.current_widget.setXRange((x_range[0]-rx),(x_range[1]-rx) , padding=0)

    def scroll_up(self):
        y_range = self.current_widget.getViewBox().state['viewRange'][1] # the visible range in x axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.current_widget.setYRange((y_range[0]+ry),(y_range[1]+ry) , padding=0)
    
    def scroll_down(self):
        y_range = self.current_widget.getViewBox().state['viewRange'][1] # the visible range in x axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.current_widget.setYRange((y_range[0]-ry),(y_range[1]-ry) , padding=0)
    ###function to adjust plot widget automatically after spectrogram
    def reset_widget(self):
        self.current_widget.clear() ## to clear the current widget
        self.current_widget.setLimits(xMin=-np.inf, xMax=np.inf, yMin=-np.inf, yMax=np.inf)
        self.current_widget.setXRange(0 , 1000 , padding=0)
        self.current_widget.setLabel('bottom')
        self.current_widget.setLabel('left')


    #####function to adjust automatically y axis range after zooming , scrolling or spectrogram
    def reset_y(self , data):

        self.current_widget.setYRange(min(data),max(data) , padding=0)
        

    ########configuration of plot widgets#####    
    def widget_configuration(self,widget,title):
        widget.showGrid(True, True, alpha=0.8)
        widget.setBackground('w')  
        widget.addLegend()
        widget.setTitle(title)
        widget.setXRange(0, 1000, padding=0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()