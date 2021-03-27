from PyQt5 import QtWidgets , QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  
import os
import MainGui
import pandas as pd
class MainWindow(QtWidgets.QMainWindow , MainGui.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openfile)
        self.actionToolbar.triggered.connect(self.toggle_tool)
        self.actionStatus_bar.triggered.connect(self.toggle_status)
        self.actionPlay.triggered.connect(self.play)
        self.actionPause.triggered.connect(self.pause)
        self.actionStop.triggered.connect(self.stop)
        self.actionClose.triggered.connect(self.close)


        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        self.pen = pg.mkPen(color=(255, 0, 0))

    def openfile(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'All Files (*);;Open File',"", "All Files (*);;Data files (*.jpg *.jpeg *.gif)")
        if self.file_path:
            self.timer = 0 
            self.index = 0
            self.actionZoom_in.setEnabled(True)
            self.actionZoom_out.setEnabled(True)
            self.actionPlay.setEnabled(True)
            self.actionPause.setEnabled(True)
            self.actionStop.setEnabled(True)
            self.actionClose.setEnabled(True)
            self.graphWidget.clear()
            df = pd.read_csv(self.file_path)
            self.x = list(df.index)
            self.y = list(df.iloc[:,0])
            print(self.file_path)
            self.graphWidget.setXRange(0 , 100 )
            self.data_line =  self.graphWidget.plot(self.x, self.y, pen=self.pen)

            
            


    def update_plot(self):
        self.index = self.index + 1
        print(self.index)
        self.graphWidget.setXRange(0 + self.index, 100 + self.index, padding=0)
        self.data_line.setData(self.x, self.y) 
    

    def play(self):
        self.stop=False
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    def pause(self):
        self.stop=True
        self.timer = QtCore.QTimer()
    
    def stop(self):
        self.index = 0
        self.timer = 0
        self.graphWidget.setXRange(0, 100, padding=0)
        self.graphWidget.plot(self.x, self.y, pen=self.pen)

    def close(self):
        self.timer = 0
        self.graphWidget.clear()
        self.actionZoom_in.setEnabled(False)
        self.actionZoom_out.setEnabled(False)
        self.actionPlay.setEnabled(False)
        self.actionPause.setEnabled(False)
        self.actionStop.setEnabled(False)


    def toggle_tool(self, action):

        if action:
            self.toolBar.show()
        else:
            self.toolBar.hide()


    def toggle_status(self, action):

        if action:
            self.statusbar.show()
        else:
            self.statusbar.hide()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()