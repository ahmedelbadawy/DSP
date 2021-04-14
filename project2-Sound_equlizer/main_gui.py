# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 882)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ecg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 931, 571))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_before1 = PlotWidget(self.horizontalLayoutWidget)
        self.widget_before1.setObjectName("widget_before1")
        self.verticalLayout.addWidget(self.widget_before1)
        self.widget_after1 = PlotWidget(self.horizontalLayoutWidget)
        self.widget_after1.setObjectName("widget_after1")
        self.verticalLayout.addWidget(self.widget_after1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_1s = PlotWidget(self.horizontalLayoutWidget)
        self.widget_1s.setObjectName("widget_1s")
        self.verticalLayout_2.addWidget(self.widget_1s)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 931, 571))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_before2 = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget_before2.setObjectName("widget_before2")
        self.verticalLayout_3.addWidget(self.widget_before2)
        self.widget_after2 = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget_after2.setObjectName("widget_after2")
        self.verticalLayout_3.addWidget(self.widget_after2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2s = PlotWidget(self.horizontalLayoutWidget_2)
        self.widget_2s.setObjectName("widget_2s")
        self.verticalLayout_4.addWidget(self.widget_2s)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 931, 571))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_before3 = PlotWidget(self.horizontalLayoutWidget_3)
        self.widget_before3.setObjectName("widget_before3")
        self.verticalLayout_5.addWidget(self.widget_before3)
        self.widget_after3 = PlotWidget(self.horizontalLayoutWidget_3)
        self.widget_after3.setObjectName("widget_after3")
        self.verticalLayout_5.addWidget(self.widget_after3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_3s = PlotWidget(self.horizontalLayoutWidget_3)
        self.widget_3s.setObjectName("widget_3s")
        self.verticalLayout_7.addWidget(self.widget_3s)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        spacerItem = QtWidgets.QSpacerItem(1, 600, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_1.setEnabled(False)
        self.verticalSlider_1.setMaximum(50)
        self.verticalSlider_1.setSingleStep(1)
        self.verticalSlider_1.setProperty("value", 10)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.horizontalLayout_5.addWidget(self.verticalSlider_1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setEnabled(False)
        self.verticalSlider_2.setMaximum(50)
        self.verticalSlider_2.setProperty("value", 10)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout_5.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setEnabled(False)
        self.verticalSlider_3.setMaximum(50)
        self.verticalSlider_3.setProperty("value", 10)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout_5.addWidget(self.verticalSlider_3)
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setEnabled(False)
        self.verticalSlider_4.setMaximum(50)
        self.verticalSlider_4.setProperty("value", 10)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout_5.addWidget(self.verticalSlider_4)
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setEnabled(False)
        self.verticalSlider_5.setMaximum(50)
        self.verticalSlider_5.setProperty("value", 10)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout_5.addWidget(self.verticalSlider_5)
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setEnabled(False)
        self.verticalSlider_6.setMaximum(50)
        self.verticalSlider_6.setProperty("value", 10)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.horizontalLayout_5.addWidget(self.verticalSlider_6)
        self.verticalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_7.setEnabled(False)
        self.verticalSlider_7.setMaximum(50)
        self.verticalSlider_7.setProperty("value", 10)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.horizontalLayout_5.addWidget(self.verticalSlider_7)
        self.verticalSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_8.setEnabled(False)
        self.verticalSlider_8.setMaximum(50)
        self.verticalSlider_8.setProperty("value", 10)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.horizontalLayout_5.addWidget(self.verticalSlider_8)
        self.verticalSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_9.setEnabled(False)
        self.verticalSlider_9.setMaximum(50)
        self.verticalSlider_9.setProperty("value", 10)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout_5.addWidget(self.verticalSlider_9)
        self.verticalSlider_10 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_10.setEnabled(False)
        self.verticalSlider_10.setMaximum(50)
        self.verticalSlider_10.setProperty("value", 10)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.horizontalLayout_5.addWidget(self.verticalSlider_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalSlider_11 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_11.setEnabled(False)
        self.verticalSlider_11.setMaximum(100)
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.horizontalLayout_5.addWidget(self.verticalSlider_11)
        self.verticalSlider_12 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_12.setEnabled(False)
        self.verticalSlider_12.setMaximum(100)
        self.verticalSlider_12.setProperty("value", 100)
        self.verticalSlider_12.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_12.setObjectName("verticalSlider_12")
        self.horizontalLayout_5.addWidget(self.verticalSlider_12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuColor_palette = QtWidgets.QMenu(self.menubar)
        self.menuColor_palette.setObjectName("menuColor_palette")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionToolbar = QtWidgets.QAction(MainWindow)
        self.actionToolbar.setCheckable(True)
        self.actionToolbar.setChecked(True)
        self.actionToolbar.setObjectName("actionToolbar")
        self.actionStatus_bar = QtWidgets.QAction(MainWindow)
        self.actionStatus_bar.setCheckable(True)
        self.actionStatus_bar.setChecked(True)
        self.actionStatus_bar.setObjectName("actionStatus_bar")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        self.actionZoom_in.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon2)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        self.actionZoom_out.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon3)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/rejected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName("actionClose")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon5)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/pause(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon6)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/iconfinder_Stop_85391.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName("actionStop")
        self.action1_Signal = QtWidgets.QAction(MainWindow)
        self.action1_Signal.setCheckable(True)
        self.action1_Signal.setChecked(True)
        self.action1_Signal.setObjectName("action1_Signal")
        self.action2_Signals = QtWidgets.QAction(MainWindow)
        self.action2_Signals.setCheckable(True)
        self.action2_Signals.setObjectName("action2_Signals")
        self.action3_Signals = QtWidgets.QAction(MainWindow)
        self.action3_Signals.setCheckable(True)
        self.action3_Signals.setObjectName("action3_Signals")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/color-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon8)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSignal_graph = QtWidgets.QAction(MainWindow)
        self.actionSignal_graph.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/ecg-lines.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignal_graph.setIcon(icon9)
        self.actionSignal_graph.setObjectName("actionSignal_graph")
        self.actionSave_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_as_PDF.setObjectName("actionSave_as_PDF")
        self.actionFaster = QtWidgets.QAction(MainWindow)
        self.actionFaster.setEnabled(False)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtWidgets.QAction(MainWindow)
        self.actionSlower.setEnabled(False)
        self.actionSlower.setObjectName("actionSlower")
        self.actionColor_1 = QtWidgets.QAction(MainWindow)
        self.actionColor_1.setEnabled(False)
        self.actionColor_1.setObjectName("actionColor_1")
        self.actionColor_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_2.setEnabled(False)
        self.actionColor_2.setObjectName("actionColor_2")
        self.actionColor_3 = QtWidgets.QAction(MainWindow)
        self.actionColor_3.setEnabled(False)
        self.actionColor_3.setObjectName("actionColor_3")
        self.actionColor_4 = QtWidgets.QAction(MainWindow)
        self.actionColor_4.setEnabled(False)
        self.actionColor_4.setObjectName("actionColor_4")
        self.actionColor_5 = QtWidgets.QAction(MainWindow)
        self.actionColor_5.setEnabled(False)
        self.actionColor_5.setObjectName("actionColor_5")
        self.actionScroll_up = QtWidgets.QAction(MainWindow)
        self.actionScroll_up.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_up.setIcon(icon10)
        self.actionScroll_up.setObjectName("actionScroll_up")
        self.actionScroll_down = QtWidgets.QAction(MainWindow)
        self.actionScroll_down.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/arrow-down-sign-to-navigate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_down.setIcon(icon11)
        self.actionScroll_down.setObjectName("actionScroll_down")
        self.actionScroll_left = QtWidgets.QAction(MainWindow)
        self.actionScroll_left.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_left.setIcon(icon12)
        self.actionScroll_left.setObjectName("actionScroll_left")
        self.actionScroll_right = QtWidgets.QAction(MainWindow)
        self.actionScroll_right.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_right.setIcon(icon13)
        self.actionScroll_right.setWhatsThis("")
        self.actionScroll_right.setObjectName("actionScroll_right")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_as_PDF)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionToolbar)
        self.menuView.addAction(self.actionStatus_bar)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPlay)
        self.menuView.addAction(self.actionPause)
        self.menuView.addAction(self.actionStop)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFaster)
        self.menuView.addAction(self.actionSlower)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSpectrogram)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionScroll_up)
        self.menuView.addAction(self.actionScroll_down)
        self.menuView.addAction(self.actionScroll_left)
        self.menuView.addAction(self.actionScroll_right)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menuColor_palette.addAction(self.actionColor_1)
        self.menuColor_palette.addAction(self.actionColor_2)
        self.menuColor_palette.addAction(self.actionColor_3)
        self.menuColor_palette.addAction(self.actionColor_4)
        self.menuColor_palette.addAction(self.actionColor_5)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuColor_palette.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSpectrogram)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Signal 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Signal 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Signal 3"))
        self.label_2.setText(_translate("MainWindow", "                                                                                              Equalizer                                                                                                                  "))
        self.label.setText(_translate("MainWindow", "Specrogram range"))
        self.pushButton.setText(_translate("MainWindow", "Play sound"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuColor_palette.setTitle(_translate("MainWindow", "Color palette"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Ready"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an existing document"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionToolbar.setText(_translate("MainWindow", "Toolbar"))
        self.actionToolbar.setStatusTip(_translate("MainWindow", "Show or hide the toolbar"))
        self.actionStatus_bar.setText(_translate("MainWindow", "Status bar"))
        self.actionStatus_bar.setStatusTip(_translate("MainWindow", "Show or hide the status bar"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionZoom_in.setStatusTip(_translate("MainWindow", "Zoom in"))
        self.actionZoom_in.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionZoom_out.setStatusTip(_translate("MainWindow", "Zoom out"))
        self.actionZoom_out.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Show Information, version number and copy rights "))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close the selected signal"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setStatusTip(_translate("MainWindow", "Play the signal"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setStatusTip(_translate("MainWindow", "Pause the signal"))
        self.actionPause.setShortcut(_translate("MainWindow", "Space"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setStatusTip(_translate("MainWindow", "Stop signal flow"))
        self.actionStop.setShortcut(_translate("MainWindow", "Return"))
        self.action1_Signal.setText(_translate("MainWindow", "Signal 1"))
        self.action1_Signal.setStatusTip(_translate("MainWindow", "View the first signal"))
        self.action1_Signal.setShortcut(_translate("MainWindow", "F1"))
        self.action2_Signals.setText(_translate("MainWindow", "Signal 2"))
        self.action2_Signals.setStatusTip(_translate("MainWindow", "View the second signal"))
        self.action2_Signals.setShortcut(_translate("MainWindow", "F2"))
        self.action3_Signals.setText(_translate("MainWindow", "Signal 3"))
        self.action3_Signals.setStatusTip(_translate("MainWindow", "View the third signal"))
        self.action3_Signals.setShortcut(_translate("MainWindow", "F3"))
        self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))
        self.actionSpectrogram.setStatusTip(_translate("MainWindow", "Create a spectrogram of the selected signal"))
        self.actionSpectrogram.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionSignal_graph.setText(_translate("MainWindow", "Signal graph"))
        self.actionSignal_graph.setStatusTip(_translate("MainWindow", "Show the signal ghraph"))
        self.actionSignal_graph.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionSave_as_PDF.setText(_translate("MainWindow", "Save as PDF"))
        self.actionSave_as_PDF.setStatusTip(_translate("MainWindow", "Save signals as pdf"))
        self.actionSave_as_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionFaster.setText(_translate("MainWindow", "Faster"))
        self.actionFaster.setStatusTip(_translate("MainWindow", "Make the playback faster"))
        self.actionSlower.setText(_translate("MainWindow", "Slower"))
        self.actionSlower.setStatusTip(_translate("MainWindow", "Make the playback slower"))
        self.actionColor_1.setText(_translate("MainWindow", "Color 1"))
        self.actionColor_2.setText(_translate("MainWindow", "Color 2"))
        self.actionColor_3.setText(_translate("MainWindow", "Color 3"))
        self.actionColor_4.setText(_translate("MainWindow", "Color 4"))
        self.actionColor_5.setText(_translate("MainWindow", "Color 5"))
        self.actionScroll_up.setText(_translate("MainWindow", "Scroll up"))
        self.actionScroll_up.setStatusTip(_translate("MainWindow", "Scroll the graph up"))
        self.actionScroll_up.setShortcut(_translate("MainWindow", "Up"))
        self.actionScroll_down.setText(_translate("MainWindow", "Scroll down"))
        self.actionScroll_down.setStatusTip(_translate("MainWindow", "Scroll the graph down"))
        self.actionScroll_down.setShortcut(_translate("MainWindow", "Down"))
        self.actionScroll_left.setText(_translate("MainWindow", "Scroll left"))
        self.actionScroll_left.setStatusTip(_translate("MainWindow", "Scroll the graph left"))
        self.actionScroll_left.setShortcut(_translate("MainWindow", "Left"))
        self.actionScroll_right.setText(_translate("MainWindow", "Scroll right"))
        self.actionScroll_right.setStatusTip(_translate("MainWindow", "Scroll the graph right"))
        self.actionScroll_right.setShortcut(_translate("MainWindow", "Right"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
