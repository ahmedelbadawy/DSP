# -*- coding: utf-8 -*-
# Enhanced Signal Viewer UI — clean light theme with improved UX

from PyQt5 import QtCore, QtGui, QtWidgets


STYLESHEET = """
/* ─── Global ─────────────────────────────────────────────── */
QMainWindow, QWidget {
    background-color: #f0f2f5;
    color: #1a1d23;
    font-family: "Segoe UI", "SF Pro Text", "Helvetica Neue", sans-serif;
    font-size: 13px;
}

/* ─── Menu bar ────────────────────────────────────────────── */
QMenuBar {
    background-color: #ffffff;
    color: #2d3748;
    border-bottom: 1px solid #e2e8f0;
    padding: 2px 6px;
    spacing: 2px;
}
QMenuBar::item {
    padding: 5px 10px;
    border-radius: 5px;
}
QMenuBar::item:selected {
    background-color: #edf2ff;
    color: #3b5bdb;
}
QMenu {
    background-color: #ffffff;
    color: #2d3748;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 5px;
}
QMenu::item {
    padding: 7px 28px 7px 14px;
    border-radius: 5px;
    margin: 1px 0;
}
QMenu::item:selected {
    background-color: #edf2ff;
    color: #3b5bdb;
}
QMenu::item:disabled {
    color: #a0aec0;
}
QMenu::separator {
    height: 1px;
    background-color: #e2e8f0;
    margin: 4px 10px;
}

/* ─── Tool bar ────────────────────────────────────────────── */
QToolBar {
    background-color: #ffffff;
    border-bottom: 1px solid #e2e8f0;
    padding: 5px 10px;
    spacing: 3px;
}
QToolBar::separator {
    width: 1px;
    background-color: #e2e8f0;
    margin: 5px 8px;
}
QToolButton {
    background-color: transparent;
    color: #4a5568;
    border: none;
    border-radius: 6px;
    padding: 6px 9px;
    font-size: 13px;
}
QToolButton:hover {
    background-color: #edf2ff;
    color: #3b5bdb;
}
QToolButton:pressed {
    background-color: #dbe4ff;
    color: #2f44b0;
}
QToolButton:disabled {
    color: #cbd5e0;
}

/* ─── Tab widget ──────────────────────────────────────────── */
QTabWidget::pane {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    background-color: #ffffff;
    top: -1px;
}
QTabBar {
    background: transparent;
}
QTabBar::tab {
    background-color: #f7f9fc;
    color: #718096;
    border: 1px solid #e2e8f0;
    border-bottom: none;
    border-radius: 7px 7px 0 0;
    padding: 8px 22px;
    margin-right: 2px;
    font-size: 12px;
    font-weight: 500;
    min-width: 90px;
}
QTabBar::tab:selected {
    background-color: #ffffff;
    color: #3b5bdb;
    border-top: 2px solid #3b5bdb;
    font-weight: 600;
}
QTabBar::tab:hover:!selected {
    background-color: #edf2ff;
    color: #3b5bdb;
}
QTabBar::scroller {
    width: 20px;
}

/* ─── Push buttons ────────────────────────────────────────── */
QPushButton {
    background-color: #3b5bdb;
    color: #ffffff;
    border: none;
    border-radius: 7px;
    padding: 9px 22px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.2px;
}
QPushButton:hover {
    background-color: #3451c7;
}
QPushButton:pressed {
    background-color: #2c44ad;
}
QPushButton:disabled {
    background-color: #e2e8f0;
    color: #a0aec0;
}

/* ─── Vertical sliders (channel gain) ────────────────────── */
QSlider::groove:vertical {
    background-color: #e2e8f0;
    width: 4px;
    border-radius: 2px;
}
QSlider::handle:vertical {
    background-color: #3b5bdb;
    border: 2px solid #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    width: 16px;
    height: 16px;
    margin: 0 -6px;
    border-radius: 8px;
}
QSlider::handle:vertical:hover {
    background-color: #3451c7;
}
QSlider::handle:vertical:disabled {
    background-color: #cbd5e0;
    border-color: #f0f2f5;
}
QSlider::sub-page:vertical {
    background-color: #748ffc;
    border-radius: 2px;
}

/* ─── Horizontal sliders (speed / scroll) ────────────────── */
QSlider::groove:horizontal {
    background-color: #e2e8f0;
    height: 4px;
    border-radius: 2px;
}
QSlider::handle:horizontal {
    background-color: #12b886;
    border: 2px solid #ffffff;
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}
QSlider::handle:horizontal:hover {
    background-color: #0ca678;
}
QSlider::handle:horizontal:disabled {
    background-color: #cbd5e0;
    border-color: #f0f2f5;
}
QSlider::sub-page:horizontal {
    background-color: #38d9a9;
    border-radius: 2px;
}

/* ─── Status bar ──────────────────────────────────────────── */
QStatusBar {
    background-color: #ffffff;
    color: #718096;
    border-top: 1px solid #e2e8f0;
    font-size: 12px;
    padding: 3px 10px;
}

/* ─── Scroll bars (subtle) ───────────────────────────────── */
QScrollBar:vertical {
    background: #f7f9fc;
    width: 8px;
    border-radius: 4px;
}
QScrollBar::handle:vertical {
    background: #cbd5e0;
    border-radius: 4px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover { background: #a0aec0; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }

/* ─── Labels ──────────────────────────────────────────────── */
QLabel {
    background: transparent;
    color: #4a5568;
}

/* ─── Group boxes ─────────────────────────────────────────── */
QGroupBox {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 6px;
    font-size: 11px;
    font-weight: 600;
    color: #718096;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 6px;
    left: 12px;
    color: #718096;
    letter-spacing: 0.5px;
}

/* ─── Tool-tip ────────────────────────────────────────────── */
QToolTip {
    background-color: #2d3748;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    padding: 5px 9px;
    font-size: 12px;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 920)
        MainWindow.setStyleSheet(STYLESHEET)
        MainWindow.setWindowTitle("Signal Viewer")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ecg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        root = QtWidgets.QVBoxLayout(self.centralwidget)
        root.setContentsMargins(14, 10, 14, 10)
        root.setSpacing(10)

        # ── Plot area (tab widget) ────────────────────────────────────────────
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        root.addWidget(self.tabWidget, stretch=1)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet("background-color: #ffffff;")

        tab_layout = QtWidgets.QGridLayout(self.tab)
        tab_layout.setContentsMargins(8, 8, 8, 8)
        tab_layout.setSpacing(8)
        self.gridLayout_4 = tab_layout

        inner = QtWidgets.QHBoxLayout()
        inner.setSpacing(8)
        self.horizontalLayout_2 = inner

        left_col = QtWidgets.QVBoxLayout()
        left_col.setSpacing(8)
        self.verticalLayout = left_col

        from pyqtgraph import PlotWidget as PW

        self.widget_before1 = PW(self.tab)
        self.widget_before1.setObjectName("widget_before1")
        self.widget_before1.setBackground("#ffffff")
        left_col.addWidget(self.widget_before1)

        self.widget_after1 = PW(self.tab)
        self.widget_after1.setObjectName("widget_after1")
        self.widget_after1.setBackground("#ffffff")
        left_col.addWidget(self.widget_after1)

        inner.addLayout(left_col)

        right_col = QtWidgets.QVBoxLayout()
        right_col.setObjectName("verticalLayout_2")
        self.verticalLayout_2 = right_col

        self.widget_1s = PW(self.tab)
        self.widget_1s.setObjectName("widget_1s")
        self.widget_1s.setBackground("#ffffff")
        right_col.addWidget(self.widget_1s)

        inner.addLayout(right_col)
        tab_layout.addLayout(inner, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")

        # ── Bottom control panel ──────────────────────────────────────────────
        bottom_panel = QtWidgets.QWidget(self.centralwidget)
        bottom_panel.setObjectName("bottomPanel")
        bottom_panel.setStyleSheet("""
            QWidget#bottomPanel {
                background: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 10px;
            }
        """)
        bottom_layout = QtWidgets.QHBoxLayout(bottom_panel)
        bottom_layout.setContentsMargins(16, 10, 16, 10)
        bottom_layout.setSpacing(20)
        root.addWidget(bottom_panel)

        # ── Channel Gain group ────────────────────────────────────────────────
        gain_group = QtWidgets.QGroupBox("CHANNEL GAIN")
        gain_group.setObjectName("gainGroup")
        gain_inner = QtWidgets.QHBoxLayout(gain_group)
        gain_inner.setContentsMargins(8, 14, 8, 8)
        gain_inner.setSpacing(4)

        self.slider_list_widgets = []
        channel_names = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4"]
        slider_attr_names = [
            "verticalSlider_1","verticalSlider_2","verticalSlider_3",
            "verticalSlider_4","verticalSlider_5","verticalSlider_6",
            "verticalSlider_7","verticalSlider_8","verticalSlider_9","verticalSlider_10"
        ]

        for i, (ch, attr) in enumerate(zip(channel_names, slider_attr_names)):
            col = QtWidgets.QVBoxLayout()
            col.setAlignment(QtCore.Qt.AlignHCenter)
            col.setSpacing(4)

            lbl = QtWidgets.QLabel(ch)
            lbl.setAlignment(QtCore.Qt.AlignHCenter)
            lbl.setStyleSheet(
                "color: #718096; font-size: 10px; font-weight: 700;"
                "letter-spacing: 0.3px; background: transparent;"
            )
            lbl.setFixedWidth(30)
            col.addWidget(lbl)

            slider = QtWidgets.QSlider(self.centralwidget)
            slider.setEnabled(False)
            slider.setMaximum(50)
            slider.setSingleStep(1)
            slider.setProperty("value", 10)
            slider.setOrientation(QtCore.Qt.Vertical)
            slider.setObjectName(attr)
            slider.setFixedWidth(18)
            slider.setFixedHeight(90)
            slider.setToolTip(f"Channel {ch} gain")
            col.addWidget(slider, alignment=QtCore.Qt.AlignHCenter)

            val_lbl = QtWidgets.QLabel("1.0")
            val_lbl.setAlignment(QtCore.Qt.AlignHCenter)
            val_lbl.setObjectName(f"gainLabel_{i}")
            val_lbl.setStyleSheet(
                "color: #a0aec0; font-size: 10px; background: transparent;"
            )
            val_lbl.setFixedWidth(30)
            col.addWidget(val_lbl)

            setattr(self, attr, slider)
            gain_inner.addLayout(col)

        bottom_layout.addWidget(gain_group)

        # ── Separator ─────────────────────────────────────────────────────────
        sep1 = QtWidgets.QFrame()
        sep1.setFrameShape(QtWidgets.QFrame.VLine)
        sep1.setStyleSheet("color: #e2e8f0;")
        bottom_layout.addWidget(sep1)

        # ── Spectrogram controls group ─────────────────────────────────────────
        spectro_group = QtWidgets.QGroupBox("SPECTROGRAM RANGE")
        spectro_inner = QtWidgets.QVBoxLayout(spectro_group)
        spectro_inner.setContentsMargins(10, 14, 10, 8)
        spectro_inner.setSpacing(8)

        for attr, label, val in [
            ("verticalSlider_12", "Max", 100),
            ("verticalSlider_11", "Min", 0),
        ]:
            row = QtWidgets.QHBoxLayout()
            lbl = QtWidgets.QLabel(label)
            lbl.setStyleSheet(
                "color: #718096; font-size: 11px; font-weight: 600;"
                "min-width: 28px; background: transparent;"
            )
            row.addWidget(lbl)

            slider = QtWidgets.QSlider(self.centralwidget)
            slider.setEnabled(False)
            sp = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
            )
            slider.setSizePolicy(sp)
            slider.setMaximum(100)
            slider.setProperty("value", val)
            slider.setOrientation(QtCore.Qt.Horizontal)
            slider.setObjectName(attr)
            slider.setFixedWidth(130)
            slider.setToolTip(f"Spectrogram {label.lower()} frequency range")
            row.addWidget(slider)

            pct = QtWidgets.QLabel(f"{val}%")
            pct.setObjectName(f"spectroLabel_{attr}")
            pct.setStyleSheet(
                "color: #a0aec0; font-size: 10px; min-width: 32px; background: transparent;"
            )
            row.addWidget(pct)
            setattr(self, attr, slider)
            spectro_inner.addLayout(row)

        bottom_layout.addWidget(spectro_group)

        # ── Separator ─────────────────────────────────────────────────────────
        sep2 = QtWidgets.QFrame()
        sep2.setFrameShape(QtWidgets.QFrame.VLine)
        sep2.setStyleSheet("color: #e2e8f0;")
        bottom_layout.addWidget(sep2)

        # ── Play Sound button ─────────────────────────────────────────────────
        btn_col = QtWidgets.QVBoxLayout()
        btn_col.setAlignment(QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton("▶  Play Sound")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedHeight(42)
        self.pushButton.setFixedWidth(140)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setToolTip("Play the output signal as audio")
        btn_col.addWidget(self.pushButton)
        bottom_layout.addLayout(btn_col)

        bottom_layout.addStretch()

        MainWindow.setCentralWidget(self.centralwidget)

        # ── Menu bar ──────────────────────────────────────────────────────────
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile         = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView         = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp         = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuColor_palette = QtWidgets.QMenu(self.menubar)
        self.menuColor_palette.setObjectName("menuColor_palette")
        MainWindow.setMenuBar(self.menubar)

        # ── Status bar ────────────────────────────────────────────────────────
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ── Tool bar ──────────────────────────────────────────────────────────
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setIconSize(QtCore.QSize(18, 18))
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # ── Actions ───────────────────────────────────────────────────────────
        def _action(name, icon_file=None, enabled=True, checkable=False, checked=False):
            act = QtWidgets.QAction(MainWindow)
            act.setObjectName(name)
            act.setEnabled(enabled)
            if checkable:
                act.setCheckable(True)
                act.setChecked(checked)
            if icon_file:
                ico = QtGui.QIcon()
                ico.addPixmap(QtGui.QPixmap(icon_file), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                act.setIcon(ico)
            return act

        self.actionOpen         = _action("actionOpen",         "icons/folder.png")
        self.actionToolbar      = _action("actionToolbar",       checkable=True, checked=True)
        self.actionStatus_bar   = _action("actionStatus_bar",    checkable=True, checked=True)
        self.actionZoom_in      = _action("actionZoom_in",       "icons/zoom-in.png",                     False)
        self.actionZoom_out     = _action("actionZoom_out",      "icons/magnifying-glass.png",             False)
        self.actionAbout        = _action("actionAbout")
        self.actionClose        = _action("actionClose",         "icons/rejected.png",                    False)
        self.actionPlay         = _action("actionPlay",          "icons/play.png",                        False)
        self.actionPause        = _action("actionPause",         "icons/pause(1).png",                    False)
        self.actionStop         = _action("actionStop",          "icons/iconfinder_Stop_85391.png",        False)
        self.action1_Signal     = _action("action1_Signal",      checkable=True, checked=True)
        self.action2_Signals    = _action("action2_Signals",     checkable=True)
        self.action3_Signals    = _action("action3_Signals",     checkable=True)
        self.actionSpectrogram  = _action("actionSpectrogram",   "icons/color-circle.png",                False)
        self.actionExit         = _action("actionExit")
        self.actionSignal_graph = _action("actionSignal_graph",  "icons/ecg-lines.png")
        self.actionSave_as_PDF  = _action("actionSave_as_PDF",                                            False)
        self.actionFaster       = _action("actionFaster",        "icons/fast-forward.png",                False)
        self.actionSlower       = _action("actionSlower",        "icons/fast-forward(1).png",             False)
        self.actionColor_1      = _action("actionColor_1",                                                False)
        self.actionColor_2      = _action("actionColor_2",                                                False)
        self.actionColor_3      = _action("actionColor_3",                                                False)
        self.actionColor_4      = _action("actionColor_4",                                                False)
        self.actionColor_5      = _action("actionColor_5",                                                False)
        self.actionScroll_up    = _action("actionScroll_up",     "icons/up-arrow.png",                    False)
        self.actionScroll_down  = _action("actionScroll_down",   "icons/arrow-down-sign-to-navigate.png", False)
        self.actionScroll_left  = _action("actionScroll_left",   "icons/left-arrow.png",                  False)
        self.actionScroll_right = _action("actionScroll_right",  "icons/right-arrow.png",                 False)
        self.actionSave         = _action("actionSave",                                                    False)
        self.actionNew_tab      = _action("actionNew_tab")

        # ── Menus ─────────────────────────────────────────────────────────────
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew_tab)
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

        for act in [self.actionColor_1, self.actionColor_2, self.actionColor_3,
                    self.actionColor_4, self.actionColor_5]:
            self.menuColor_palette.addAction(act)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuColor_palette.menuAction())

        # ── Toolbar ───────────────────────────────────────────────────────────
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addAction(self.actionSlower)
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
        _t = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_t("MainWindow", "Signal Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _t("MainWindow", "Signal 1"))
        self.pushButton.setText(_t("MainWindow", "▶  Play Sound"))
        self.menuFile.setTitle(_t("MainWindow", "File"))
        self.menuView.setTitle(_t("MainWindow", "View"))
        self.menuHelp.setTitle(_t("MainWindow", "Help"))
        self.menuColor_palette.setTitle(_t("MainWindow", "Color Palette"))
        self.statusbar.showMessage("Ready")
        self.toolBar.setWindowTitle(_t("MainWindow", "Main Toolbar"))

        self.actionOpen.setText(_t("MainWindow", "Open…"))
        self.actionOpen.setStatusTip(_t("MainWindow", "Open a CSV or WAV signal file"))
        self.actionOpen.setShortcut(_t("MainWindow", "Ctrl+O"))
        self.actionToolbar.setText(_t("MainWindow", "Toolbar"))
        self.actionStatus_bar.setText(_t("MainWindow", "Status Bar"))
        self.actionZoom_in.setText(_t("MainWindow", "Zoom In"))
        self.actionZoom_in.setShortcut(_t("MainWindow", "Ctrl+E"))
        self.actionZoom_out.setText(_t("MainWindow", "Zoom Out"))
        self.actionZoom_out.setShortcut(_t("MainWindow", "Ctrl+D"))
        self.actionAbout.setText(_t("MainWindow", "About…"))
        self.actionAbout.setShortcut(_t("MainWindow", "Ctrl+H"))
        self.actionClose.setText(_t("MainWindow", "Close Signal"))
        self.actionClose.setShortcut(_t("MainWindow", "Ctrl+Q"))
        self.actionPlay.setText(_t("MainWindow", "Play"))
        self.actionPlay.setShortcut(_t("MainWindow", "Ctrl+P"))
        self.actionPause.setText(_t("MainWindow", "Pause"))
        self.actionPause.setShortcut(_t("MainWindow", "Space"))
        self.actionStop.setText(_t("MainWindow", "Stop"))
        self.actionStop.setShortcut(_t("MainWindow", "Return"))
        self.action1_Signal.setText(_t("MainWindow", "Signal 1"))
        self.action1_Signal.setShortcut(_t("MainWindow", "F1"))
        self.action2_Signals.setText(_t("MainWindow", "Signal 2"))
        self.action2_Signals.setShortcut(_t("MainWindow", "F2"))
        self.action3_Signals.setText(_t("MainWindow", "Signal 3"))
        self.action3_Signals.setShortcut(_t("MainWindow", "F3"))
        self.actionSpectrogram.setText(_t("MainWindow", "Spectrogram"))
        self.actionSpectrogram.setStatusTip(_t("MainWindow", "Toggle spectrogram view"))
        self.actionSpectrogram.setShortcut(_t("MainWindow", "Ctrl+T"))
        self.actionExit.setText(_t("MainWindow", "Exit"))
        self.actionExit.setShortcut(_t("MainWindow", "Esc"))
        self.actionSignal_graph.setText(_t("MainWindow", "Signal Graph"))
        self.actionSignal_graph.setShortcut(_t("MainWindow", "Ctrl+G"))
        self.actionSave_as_PDF.setText(_t("MainWindow", "Save as PDF…"))
        self.actionSave_as_PDF.setShortcut(_t("MainWindow", "Ctrl+S"))
        self.actionFaster.setText(_t("MainWindow", "Faster"))
        self.actionSlower.setText(_t("MainWindow", "Slower"))
        for i, act in enumerate([self.actionColor_1, self.actionColor_2, self.actionColor_3,
                                  self.actionColor_4, self.actionColor_5], 1):
            act.setText(_t("MainWindow", f"Palette {i}"))
        self.actionScroll_up.setText(_t("MainWindow", "Scroll Up"))
        self.actionScroll_up.setShortcut(_t("MainWindow", "Up"))
        self.actionScroll_down.setText(_t("MainWindow", "Scroll Down"))
        self.actionScroll_down.setShortcut(_t("MainWindow", "Down"))
        self.actionScroll_left.setText(_t("MainWindow", "Scroll Left"))
        self.actionScroll_left.setShortcut(_t("MainWindow", "Left"))
        self.actionScroll_right.setText(_t("MainWindow", "Scroll Right"))
        self.actionScroll_right.setShortcut(_t("MainWindow", "Right"))
        self.actionSave.setText(_t("MainWindow", "Save Sound"))
        self.actionNew_tab.setText(_t("MainWindow", "New Tab"))
        self.actionNew_tab.setShortcut(_t("MainWindow", "Ctrl+N"))


if __name__ == "__main__":
    import sys
    from pyqtgraph import PlotWidget
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
