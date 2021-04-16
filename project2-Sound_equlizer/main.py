from PyQt5 import QtWidgets , QtCore, QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os
import os.path
import main_gui
from fourier_transform import fourier , spectro_range
import pandas as pd
from scipy import signal
import numpy as np
from PyQt5.QtWidgets import QMessageBox , QFileDialog
from PyQt5.Qt import QFileInfo
from PyQt5.QtPrintSupport import QPrinter
from scipy.io import wavfile
import sounddevice as sd
import time
from pdf import GeneratePDF
import pyqtgraph.exporters

class MainWindow(QtWidgets.QMainWindow , main_gui.Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #########variables######################
        self.i = 0 #counter for (for loob)
        #####timers for plots####
        self.timer1=0
        self.timer2=0
        self.timer3=0
        self.timer=  [

            self.timer1, 
            self.timer2, 
            self.timer3 
        ] 

        self.interval = 3 * [None]
        ###index for dynamic plot
        self.index1 = 0
        self.index2 = 0
        self.index3 = 0
        self.index = [
        
            self.index1,
            self.index2,
            self.index3
        ]
        ####### list for slider
        self.gain = 3 * [10 * [None]]
        self.slider_list = [self.verticalSlider_1, self.verticalSlider_2, self.verticalSlider_3, self.verticalSlider_4, self.verticalSlider_5, self.verticalSlider_6, self.verticalSlider_7,
        self.verticalSlider_8, self.verticalSlider_9, self.verticalSlider_10]
        for i in range(10):
            self.gain[0][i] = float(self.slider_list[i].value())/10
        ######plot configuration#####
        self.pen = pg.mkPen(color=(255, 0, 0))
        # for i in sel
        self.widget_configuration(self.widget_before1 , "Input signal 1")
        self.widget_configuration(self.widget_before2, "Input signal 2")
        self.widget_configuration(self.widget_before3, "Input signal 3")
        self.widget_configuration(self.widget_after1 , "Output signal 1")
        self.widget_configuration(self.widget_after2, "Output signal 2")
        self.widget_configuration(self.widget_after3, "Output signal 3")
        self.widget_configuration(self.widget_1s , "Spectrogram 1")
        self.widget_configuration(self.widget_2s, "Spectrogram 2")
        self.widget_configuration(self.widget_3s, "Spectrogram 3")

        self.graphs = [

            self.widget_before1,
            self.widget_before2,
            self.widget_before3,
            self.widget_after1,
            self.widget_after2,
            self.widget_after3

        ]
        self.spectros = [

            self.widget_1s,
            self.widget_2s,
            self.widget_3s

        ]
        for i in self.spectros:
            i.hide()
        
        self.spectro_min = 3 * [0]
        self.spectro_max = 3 * [1]

        # self.current_widget = self.graphs[0] #idicate the selected widget in groupBox
        self.current_widget_i = 0  ###indicate current widget index

        #####color palette for spectro gram
        self.color =[ [(0.5, (0, 182, 188, 255)),
                        (1.0, (246, 111, 0, 255)),
                        (0.0, (75, 0, 113, 255))]

                        ,[(0.5, (170, 0, 0, 255)),
                        (1.0, (0, 0, 255, 255)),
                        (0.0, (170, 255, 255, 255))]

                        ,[(0.5, (0, 255, 0, 255)),
                        (1.0, (170, 170, 255, 255)),
                        (0.0, (255, 85, 0, 255))]

                        ,[(0.5, (0, 255, 0, 255)),
                        (1.0, (85, 0, 255, 255)),
                        (0.0, (0, 255, 127, 255))]

                        ,[(0.5, (0, 0, 255, 255)),
                        (1.0, (170, 255, 127, 255)),
                        (0.0, (255, 255, 127, 255))] ]

        self.current_color = 3 * [0]
        #####aflag to indicate which is shown signal graph(1) or spectrogram(0) 
        
        self.shown = 3 * [0]
        
        self.signals = 3 * [0] #list to store loaded signals
        self.file_name = 3 * [0]
        self.x = 3 * [0] ### x , y to recieve data for plotting
        self.y = 3 * [0]
        self.freq_sampling = 3 * [0]
        self.output_signal = 3 * [0]

        #start the programm with one signal viewed

        #########actions triggeration###########
        self.verticalSlider_1.valueChanged.connect(lambda: self.get_gain(0))
        self.verticalSlider_2.valueChanged.connect(lambda: self.get_gain(1))
        self.verticalSlider_3.valueChanged.connect(lambda: self.get_gain(2))
        self.verticalSlider_4.valueChanged.connect(lambda: self.get_gain(3))
        self.verticalSlider_5.valueChanged.connect(lambda: self.get_gain(4))
        self.verticalSlider_6.valueChanged.connect(lambda: self.get_gain(5))
        self.verticalSlider_7.valueChanged.connect(lambda: self.get_gain(6))
        self.verticalSlider_8.valueChanged.connect(lambda: self.get_gain(7))
        self.verticalSlider_9.valueChanged.connect(lambda: self.get_gain(8))
        self.verticalSlider_10.valueChanged.connect(lambda: self.get_gain(9))
        self.verticalSlider_11.valueChanged.connect(self.update_spectro)
        self.verticalSlider_12.valueChanged.connect(self.update_spectro)
        self.tabWidget.currentChanged.connect(self.select)
        self.actionOpen.triggered.connect(self.openfile)
        self.actionSave_as_PDF.triggered.connect(self.export_pdf)
        self.actionToolbar.triggered.connect(self.toggle_tool)
        self.actionStatus_bar.triggered.connect(self.toggle_status)
        self.actionPlay.triggered.connect(self.play)
        self.actionPause.triggered.connect(self.pause)
        self.actionStop.triggered.connect(self.stop)
        self.actionClose.triggered.connect(self.close)
        self.actionFaster.triggered.connect(self.faster)
        self.actionSlower.triggered.connect(self.slower)
        self.actionZoom_in.triggered.connect(self.zoom_in)
        self.actionZoom_out.triggered.connect(self.zoom_out)
        self.actionSpectrogram.triggered.connect(self.spectro)
        self.actionColor_1.triggered.connect(lambda:self.color_palette(0))
        self.actionColor_2.triggered.connect(lambda:self.color_palette(1))
        self.actionColor_3.triggered.connect(lambda:self.color_palette(2))
        self.actionColor_4.triggered.connect(lambda:self.color_palette(3))
        self.actionColor_5.triggered.connect(lambda:self.color_palette(4))
        self.actionAbout.triggered.connect(self.pop_up)
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionScroll_right.triggered.connect(self.scroll_right)
        self.actionScroll_left.triggered.connect(self.scroll_left)
        self.actionScroll_up.triggered.connect(self.scroll_up)
        self.actionScroll_down.triggered.connect(self.scroll_down)
        self.pushButton.clicked.connect(self.play_sound)
        ####chose the current_widget to control it
        # self.radioButton_1.toggled.connect(self.select_1)       
        # self.radioButton_2.toggled.connect(self.select_2)
        # self.radioButton_3.toggled.connect(self.select_3)
        # radiobutton.toggled.connect
    def select(self):
        self.current_widget_i = self.tabWidget.currentIndex( )
        if self.signals[self.current_widget_i] == 0 :
            self.disable_items()
        else:
            self.enable_items()
        for i in range(10):
            self.slider_list[i].setValue(self.gain[self.current_widget_i][i]*10)

        self.verticalSlider_11.setValue(self.spectro_min[self.current_widget_i]* 100)
        self.verticalSlider_12.setValue(self.spectro_max[self.current_widget_i] * 100)
        

        # print(self.current_widget_i)
    # def select_2(self):
    #     if self.shown_2 == 1 :
    #         self.current_widget = self.graphs[1]
    #     else:
    #         self.current_widget = self.spectros[1]
    #     self.current_widget_i = 1
    # def select_3(self):
    #     if self.shown_3 == 1 :
    #         self.current_widget = self.graphs[2]
    #     else:
    #         self.current_widget = self.spectros[2]
    #     self.current_widget_i = 2
    def get_gain(self , i):
        if self.signals[self.current_widget_i] != 0:
            self.gain[self.current_widget_i][i] =  float(self.slider_list[i].value())/10
            if self.df.isin([self.file_name[self.current_widget_i]]).any().any() :
                index = self.df.index[self.df['name'] == self.file_name[self.current_widget_i]].tolist()[0]
                self.df.iloc[index,1:] = self.gain[self.current_widget_i]
                # print(self.df)
            else :
                self.df.loc[len(self.df)] = [self.file_name[self.current_widget_i]] + self.gain[self.current_widget_i]
            # print(self.gain[self.current_widget_i][i])
            self.df.to_csv('sliders.csv')

            self.plot_output()

            self.plot_spectro(self.output_signal[self.current_widget_i] , self.color[self.current_color[self.current_widget_i]])
            
        
       



        
    #####to load and plot signal#######
    def openfile(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',"", "Data files (*.csv *.wav)")
        
        if self.file_path:
            if self.file_path.endswith('.wav') :  ### to read .wav file
                
                self.data = wavfile.read(self.file_path)
                # self.sample_rate = self.data.getframerate()
                # print (self.sample_rate)
                audio_df = pd.DataFrame(self.data)
                # print(audio_df.head())
                self.freq_sampling[self.current_widget_i] = audio_df.iloc[0 , 0]
                self.y[self.current_widget_i] = audio_df.iloc[1 , 0]
                # print(self.freq_sampling , self.y[self.current_widget_i])
            else:
                df = pd.read_csv(self.file_path)
                self.y[self.current_widget_i] = df.iloc[:,0]
                self.freq_sampling[self.current_widget_i] = 1000

            self.signals[self.current_widget_i] = self.file_path
            self.file_name[self.current_widget_i] = os.path.basename(self.signals[self.current_widget_i])

            self.reset_widget()
    
            self.plot_input()
            self.plot_output()
            self.enable_items()
            self.moving()
            self.update_sliders()
            self.spectro_sliders()
            self.plot_spectro(self.output_signal[self.current_widget_i],self.color[0]) #to create spectrogram
            
    def update_sliders(self):
        if os.path.isfile('sliders.csv'):
            self.df = pd.read_csv('sliders.csv', index_col=0)
            # print(df)
            # print(self.file_name)
            # print(df.isin([self.file_name]).any().any())
            if self.df.isin([self.file_name[self.current_widget_i]]).any().any() :
                self.gain[self.current_widget_i] = self.df[self.df['name'] == self.file_name[self.current_widget_i]].values.tolist()[0][1:]
                # print(len(self.gain[self.current_widget_i]))
                # print(len(self.slider_list))
            else:
                self.gain[self.current_widget_i] = 10 * [1]
            for i in range(10):
                self.slider_list[i].setValue(self.gain[self.current_widget_i][i]*10)

        else:
            data = [self.file_name[self.current_widget_i]] +  self.gain[self.current_widget_i]
            self.df = pd.DataFrame(data ).transpose()
            self.df.columns = ['name','gain_1','gain_2','gain_3','gain_4','gain_5','gain_6','gain_7','gain_8','gain_9','gain_10']
            # print(self.df)
            self.df.to_csv('sliders.csv')



    def plot_input(self):
        self.limits(self.y[self.current_widget_i] , self.current_widget_i)
        self.graphs[self.current_widget_i].plot(self.y[self.current_widget_i],name = self.file_name[self.current_widget_i] ,pen=self.pen)

    def plot_output(self):
        # print(self.gain[self.current_widget_i] )
        self.output_signal[self.current_widget_i], z = fourier(self.y[self.current_widget_i] , self.gain[self.current_widget_i])
        self.graphs[self.current_widget_i + 3].clear()
        self.limits(self.output_signal[self.current_widget_i] ,self.current_widget_i + 3 )
        self.graphs[self.current_widget_i + 3].plot(self.output_signal[self.current_widget_i] ,name = self.file_name[self.current_widget_i] ,pen=self.pen)

    def moving(self):
        ##### create a timer for widgets#####
        self.index[self.current_widget_i] = 0
        self.interval[self.current_widget_i] = 25
        self.timer[self.current_widget_i] = QtCore.QTimer()
        self.timer[self.current_widget_i].setInterval(50)
        if self.current_widget_i == 0:
            # self.timer[0] = QtCore.QTimer()
            # self.timer[0].setInterval(10)
            self.timer[0].timeout.connect(self.update_plot1)

        elif self.current_widget_i == 1:
            # self.timer[1] = QtCore.QTimer()
            # self.timer[1].setInterval(50)
            self.timer[1].timeout.connect(self.update_plot2)

        else:
            # self.timer[2] = QtCore.QTimer()
            # self.timer[2].setInterval(50)
            self.timer[2].timeout.connect(self.update_plot3)


        self.timer[self.current_widget_i].start()
    
   

    def enable_items(self):
            
        ######enable tools to control signal#####
        self.actionZoom_in.setEnabled(True)
        self.actionZoom_out.setEnabled(True)
        self.actionPlay.setEnabled(True)
        self.actionPause.setEnabled(True)
        self.actionStop.setEnabled(True)
        self.actionClose.setEnabled(True)
        self.actionFaster.setEnabled(True)
        self.actionSlower.setEnabled(True)
        self.actionSpectrogram.setEnabled(True)
        self.actionScroll_right.setEnabled(True)
        self.actionScroll_left.setEnabled(True)
        self.actionScroll_up.setEnabled(True)
        self.actionScroll_down.setEnabled(True)
        self.actionColor_1.setEnabled(True)
        self.actionColor_2.setEnabled(True)
        self.actionColor_3.setEnabled(True)
        self.actionColor_4.setEnabled(True)
        self.actionColor_5.setEnabled(True)
        self.pushButton.setEnabled(True)
        for i in range(10):
            self.slider_list[i].setEnabled(True)
        self.verticalSlider_11.setEnabled(True)
        self.verticalSlider_12.setEnabled(True)

            

    ########update function to make the plot moving###### 
    def update_plot1(self):

        if self.signals[0] != 0:
            self.index[0] = self.index[0] + self.interval[self.current_widget_i]
            self.graphs[0].setXRange(0 + self.index[0], 1000 + self.index[0], padding=0)
            self.graphs[3].setXRange(0 + self.index[0], 1000 + self.index[0], padding=0)

    def update_plot2(self):

        if self.signals[1] != 0:
            self.index[1] = self.index[1] + self.interval[self.current_widget_i]
            self.graphs[1].setXRange(0 + self.index[1], 1000 + self.index[1], padding=0)
            self.graphs[4].setXRange(0 + self.index[1], 1000 + self.index[1], padding=0)

    def update_plot3(self):                    
        if self.signals[2] != 0:
            self.index[2] = self.index[2] + self.interval[self.current_widget_i]
            self.graphs[2].setXRange(0 + self.index[2], 1000 + self.index[2], padding=0)
            self.graphs[5].setXRange(0 + self.index[2], 1000 + self.index[2], padding=0)
                    
    #######play function to start the movement####
    def play(self):
        
        if self.timer[self.current_widget_i] != 0 :
            self.timer[self.current_widget_i].start()

    #######pause function to pause the movement####
    def pause(self):
      
        if self.timer[self.current_widget_i] != 0 :
            self.timer[self.current_widget_i].stop()

    #######stop function to stop the movement and reset the signal plot####
    def stop(self):
    
        if self.timer[self.current_widget_i] != 0 :
            self.timer[self.current_widget_i].stop()
            self.index[self.current_widget_i] = 0
            self.graphs[self.current_widget_i].setXRange(0, 1000, padding=0)
            self.graphs[self.current_widget_i + 3].setXRange(0, 1000, padding=0)
    def faster(self):
        if self.interval[self.current_widget_i] < 45 :
            self.interval[self.current_widget_i] += 10
            print(self.interval[self.current_widget_i])
            self.timer[self.current_widget_i].setInterval(self.interval[self.current_widget_i])
    def slower(self):
        if self.interval[self.current_widget_i] > 5 :
            self.interval[self.current_widget_i] -= 10
            print(self.interval[self.current_widget_i])
            self.timer[self.current_widget_i].setInterval(self.interval[self.current_widget_i])
    #######close function to clear the plot####
    def close(self):
 
        self.timer[self.current_widget_i] = 0
        self.signals[self.current_widget_i] = 0
        self.reset_widget()
        self.disable_items()

    def play_sound(self):
        # print(self.output_signal[self.current_widget_i])
        duration = len(self.output_signal[self.current_widget_i]) / self.freq_sampling[self.current_widget_i]                
        sd.play(self.output_signal[self.current_widget_i],self.freq_sampling[self.current_widget_i])
        time.sleep(duration)
        sd.stop

    def disable_items(self):
        self.actionZoom_in.setEnabled(False)
        self.actionZoom_out.setEnabled(False)
        self.actionPlay.setEnabled(False)
        self.actionPause.setEnabled(False)
        self.actionStop.setEnabled(False)
        self.actionClose.setEnabled(False)
        self.actionSpectrogram.setEnabled(False)
        self.actionScroll_right.setEnabled(False)
        self.actionScroll_left.setEnabled(False)
        self.actionScroll_up.setEnabled(False)
        self.actionScroll_down.setEnabled(False)
        self.actionColor_1.setEnabled(False)
        self.actionColor_2.setEnabled(False)
        self.actionColor_3.setEnabled(False)
        self.actionColor_4.setEnabled(False)
        self.actionColor_5.setEnabled(False)
        self.pushButton.setEnabled(False)
        for i in range(10):
            self.slider_list[i].setEnabled(False)   
        self.verticalSlider_11.setEnabled(False)
        self.verticalSlider_12.setEnabled(False)


     ########function to plot spectrogram####################
    def spectro(self):
        
        if self.signals[self.current_widget_i] != 0:
            if self.shown[self.current_widget_i] ==0 :
                self.spectros[self.current_widget_i].show()
                self.shown[self.current_widget_i] = 1
            else:
                self.spectros[self.current_widget_i].hide()
                self.shown[self.current_widget_i] = 0

    def spectro_sliders(self):
        self.verticalSlider_11.setValue(0)
        self.verticalSlider_12.setValue(100)
        self.spectro_min[self.current_widget_i]  = 0.0
        self.spectro_max[self.current_widget_i]  = 1.0

    def plot_spectro(self , output_signal ,color):
        fs = self.freq_sampling[self.current_widget_i] ####sampling frequency
        self.f,self.t,self.Sxx = signal.spectrogram(output_signal,fs)
        self.spectros[self.current_widget_i].clear()
        pg.setConfigOptions(imageAxisOrder='row-major')

        self.img= pg.ImageItem()
        self.spectros[self.current_widget_i].addItem(self.img)
        # Add a histogram to control the gradient of the image
        self.hist = pg.HistogramLUTItem()
        # Link the histogram to the image
        self.hist.setImageItem(self.img)
        # Fit the min and max levels of the histogram
        self.hist.setLevels(np.min(self.Sxx), np.max(self.Sxx))

        self.hist.gradient.restoreState(
                {'mode': 'rgb',
                'ticks': color})
        self.img.setImage(self.Sxx)

        self.img.scale(self.t[-1]/np.size(self.Sxx, axis=1),  self.f[-1]/np.size(self.Sxx, axis=0))

        self.spectros[self.current_widget_i].setXRange(0 , self.t[-1] , padding=0)
        self.spectros[self.current_widget_i].setYRange(0 ,  self.f[-1] , padding=0)

        self.spectros[self.current_widget_i].setLimits(xMin=0, xMax=self.t[-1], yMin= 0 , yMax= self.f[-1])
        # Add labels to the axis
        self.spectros[self.current_widget_i].setLabel('bottom', "Time", units='s')
            
        self.spectros[self.current_widget_i].setLabel('left', "Frequency", units='Hz')

    def update_spectro(self):
        self.spectro_min[self.current_widget_i] = float(self.verticalSlider_11.value())/100
        self.spectro_max[self.current_widget_i] = float(self.verticalSlider_12.value())/100
        self.verticalSlider_11.setMaximum(self.verticalSlider_12.value()) ## the maximum slider cant be higher than the min slider
        self.verticalSlider_12.setMinimum(self.verticalSlider_11.value())
        spectro_values = spectro_range(self.output_signal[self.current_widget_i] , self.spectro_min[self.current_widget_i] , self.spectro_max[self.current_widget_i])
        self.plot_spectro(spectro_values , self.color[self.current_color[self.current_widget_i]])
    #####function for color palette
    def color_palette(self, i):
        self.plot_spectro(self.output_signal[self.current_widget_i] , self.color[i])
        self.current_color[self.current_widget_i] = i

    ##################################################################
   

    
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
        self.graphs[self.current_widget_i].plotItem.getViewBox().scaleBy((1 / 1.25, 1 / 1.25))
        self.graphs[self.current_widget_i + 3].plotItem.getViewBox().scaleBy((1 / 1.25, 1 / 1.25))
    def zoom_out(self):
        self.graphs[self.current_widget_i].plotItem.getViewBox().scaleBy((1.25,1.25))
        self.graphs[self.current_widget_i + 3].plotItem.getViewBox().scaleBy((1.25,1.25))

    ######functionts for scrolling
    def scroll_right(self):
        x_range = self.graphs[self.current_widget_i].getViewBox().state['viewRange'][0] # the visible range in x axis
        rx = 0.1 * (x_range[1] - x_range[0])
        self.graphs[self.current_widget_i].setXRange((x_range[0]+rx),(x_range[1]+rx) , padding=0)
        self.graphs[self.current_widget_i + 3].setXRange((x_range[0]+rx),(x_range[1]+rx) , padding=0)

    def scroll_left(self):
        x_range = self.graphs[self.current_widget_i].getViewBox().state['viewRange'][0] # the visible range in x axis
        rx = 0.1 * (x_range[1] - x_range[0])
        self.graphs[self.current_widget_i].setXRange((x_range[0]-rx),(x_range[1]-rx) , padding=0)
        self.graphs[self.current_widget_i + 3].setXRange((x_range[0]-rx),(x_range[1]-rx) , padding=0)

    def scroll_up(self):
        y_range = self.graphs[self.current_widget_i].getViewBox().state['viewRange'][1] # the visible range in y axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.graphs[self.current_widget_i].setYRange((y_range[0]+ry),(y_range[1]+ry) , padding=0)

        y_range = self.graphs[self.current_widget_i + 3].getViewBox().state['viewRange'][1] # the visible range in y axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.graphs[self.current_widget_i + 3].setYRange((y_range[0]+ry),(y_range[1]+ry) , padding=0)
    
    def scroll_down(self):
        y_range = self.graphs[self.current_widget_i].getViewBox().state['viewRange'][1] # the visible range in x axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.graphs[self.current_widget_i].setYRange((y_range[0]-ry),(y_range[1]-ry) , padding=0)

        y_range = self.graphs[self.current_widget_i + 3].getViewBox().state['viewRange'][1] # the visible range in x axis
        ry = 0.1 * (y_range[1] - y_range[0])
        self.graphs[self.current_widget_i + 3].setYRange((y_range[0]-ry),(y_range[1]-ry) , padding=0)
    ###function to adjust plot widget automatically 

    def reset_widget(self):
        self.graphs[self.current_widget_i].clear()
        self.graphs[self.current_widget_i].setLabel('bottom', "Time (ms)")
        self.graphs[self.current_widget_i + 3].clear()
        self.graphs[self.current_widget_i + 3].setLabel('bottom', "Time (ms)")
        self.spectros[self.current_widget_i].clear()
        self.spectros[self.current_widget_i].hide()
        self.shown[self.current_widget_i] = 0
        
        
            
    #####function to adjust automatically y axis range after zooming , scrolling 
    def limits(self , data ,i):

        # self.current_widget.setYRange(min(data),max(data) , padding=0)
        # self.current_widget.setLimits()
        self.graphs[i].setYRange(np.float(min(data)),np.float(max(data)) , padding=0)
        self.graphs[i].setLimits(xMin=0, xMax=(len(data) - 1), yMin=np.float(min(data)), yMax=np.float(max(data)))
        

    ########configuration of plot widgets#####    
    def widget_configuration(self,widget,title):
        widget.showGrid(True, True, alpha=0.8)
        widget.setBackground('w') 
        widget.addLegend()
        widget.setTitle(title)
        widget.setXRange(0, 1000, padding=0)
    
    def export_pdf (self):
        
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "" :
                fn += '.pdf'
        

            if self.graphs[self.current_widget_i].scene():
                # export all items in all viewers as images
                exporter1 = pg.exporters.ImageExporter(self.graphs[self.current_widget_i].scene())
                exporter1.export('input_signal.png')
    
                exporter3 = pg.exporters.ImageExporter(self.graphs[self.current_widget_i + 3].scene())
                exporter3.export('output_signal.png')
    
                #show spectrogram before printing
                self.spectros[self.current_widget_i].show()
                exporter4 = pg.exporters.ImageExporter(self.spectros[self.current_widget_i].scene())
                exporter4.export('spectrogram.png')
                
                my_pdf = GeneratePDF(fn)
                my_pdf.create_pdf()
                my_pdf.save_pdf()
                if self.shown[self.current_widget_i] == 0 :
                    self.spectros[self.current_widget_i].hide()
            
           

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()