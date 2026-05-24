from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import os
import os.path
import main_gui
from fourier_transform import fourier, spectro_range
import pandas as pd
from scipy import signal
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.Qt import QFileInfo
from scipy.io import wavfile
import sounddevice as sd
import time
from pdf import GeneratePDF
import pyqtgraph.exporters
from scipy.io.wavfile import write


# ─── pyqtgraph global style ──────────────────────────────────────────────────
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', '#4a5568')


class MainWindow(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # ── state lists (one entry per tab) ──────────────────────────────────
        self.timer            = [0]
        self.interval         = [0]
        self.index            = [0]
        self.gain             = [10 * [1]]
        self.spectro_min      = [0]
        self.spectro_max      = [1]
        self.spectro_flag     = [0]
        self.signals          = [0]
        self.file_name        = [0]
        self.input_signal     = [0]
        self.freq_sampling    = [0]
        self.output_signal    = [0]
        self.current_color    = [0]
        self.current_tab_index = 0
        self.i = 2          # next-tab counter
        self.tab    = {}
        self.layout = {}

        # ── slider references ─────────────────────────────────────────────────
        self.slider_list = [
            self.verticalSlider_1,  self.verticalSlider_2,
            self.verticalSlider_3,  self.verticalSlider_4,
            self.verticalSlider_5,  self.verticalSlider_6,
            self.verticalSlider_7,  self.verticalSlider_8,
            self.verticalSlider_9,  self.verticalSlider_10,
        ]
        for i in range(10):
            self.gain[0][i] = float(self.slider_list[i].value()) / 10

        # ── plot pen (blue, clean) ────────────────────────────────────────────
        self.pen = pg.mkPen(color='#3b5bdb', width=1.2)

        # ── color palettes for spectrogram ────────────────────────────────────
        self.color = [
            [(0.5, (0, 182, 188, 255)),  (1.0, (246, 111, 0, 255)),   (0.0, (75,  0, 113, 255))],
            [(0.5, (170, 0, 0, 255)),    (1.0, (0,   0, 255, 255)),   (0.0, (170,255,255, 255))],
            [(0.5, (0, 255, 0, 255)),    (1.0, (170,170,255, 255)),   (0.0, (255, 85,  0, 255))],
            [(0.5, (0, 255, 0, 255)),    (1.0, (85,  0, 255, 255)),   (0.0, (0,  255,127, 255))],
            [(0.5, (0,   0, 255, 255)),  (1.0, (170,255,127, 255)),   (0.0, (255,255,127, 255))],
        ]
        self.actionColor = [
            self.actionColor_1, self.actionColor_2, self.actionColor_3,
            self.actionColor_4, self.actionColor_5,
        ]

        # ── graph widget lists ────────────────────────────────────────────────
        self.input_graph     = [self.widget_before1]
        self.output_graph    = [self.widget_after1]
        self.spectro_widgets = [self.widget_1s]

        self._configure_plot(self.widget_before1, "Input Signal")
        self._configure_plot(self.widget_after1,  "Output Signal")
        self._configure_plot(self.widget_1s,      "Spectrogram")
        self.widget_1s.hide()

        # ── status-bar message widget ─────────────────────────────────────────
        self._status_file_label = QtWidgets.QLabel("")
        self._status_file_label.setStyleSheet("color: #3b5bdb; font-weight: 600; padding: 0 8px;")
        self.statusbar.addPermanentWidget(self._status_file_label)

        self._status_state_label = QtWidgets.QLabel("No file loaded")
        self._status_state_label.setStyleSheet("color: #718096; padding: 0 4px;")
        self.statusbar.addWidget(self._status_state_label)

        # ── wire up all signals ───────────────────────────────────────────────
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.tabWidget.currentChanged.connect(self.select)

        for i in range(10):
            self._connect_gain_slider(i)
        for i in range(5):
            self._connect_color_action(i)

        self.verticalSlider_11.valueChanged.connect(self._on_spectro_slider)
        self.verticalSlider_12.valueChanged.connect(self._on_spectro_slider)

        self.actionOpen.triggered.connect(self.openfile)
        self.actionSave_as_PDF.triggered.connect(self.export_pdf)
        self.actionToolbar.triggered.connect(self.toggle_tool)
        self.actionStatus_bar.triggered.connect(self.toggle_status)
        self.actionPlay.triggered.connect(self.play)
        self.actionPause.triggered.connect(self.pause)
        self.actionStop.triggered.connect(self.stop)
        self.actionClose.triggered.connect(self.close_signal)
        self.actionFaster.triggered.connect(lambda: self.playback(1))
        self.actionSlower.triggered.connect(lambda: self.playback(-1))
        self.actionZoom_in.triggered.connect(lambda: self.zoom(1 / 1.25))
        self.actionZoom_out.triggered.connect(lambda: self.zoom(1.25))
        self.actionSpectrogram.triggered.connect(self.toggle_spectro)
        self.actionNew_tab.triggered.connect(self.new_tab)
        self.actionAbout.triggered.connect(self.pop_up)
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionScroll_right.triggered.connect(lambda: self.scroll_x(1))
        self.actionScroll_left.triggered.connect(lambda:  self.scroll_x(-1))
        self.actionScroll_up.triggered.connect(lambda:    self.scroll_y(1))
        self.actionScroll_down.triggered.connect(lambda:  self.scroll_y(-1))
        self.pushButton.clicked.connect(self.play_sound)

    # ─── helpers ─────────────────────────────────────────────────────────────

    def _connect_gain_slider(self, i):
        self.slider_list[i].valueChanged.connect(lambda _, idx=i: self.get_gain(idx))

    def _connect_color_action(self, i):
        self.actionColor[i].triggered.connect(lambda _, idx=i: self.color_palette(idx))

    def _configure_plot(self, widget, title):
        """Apply consistent styling to a PlotWidget."""
        widget.setBackground('#ffffff')
        widget.showGrid(True, True, alpha=0.25)
        widget.addLegend(offset=(10, 10))
        widget.setTitle(f"<span style='color:#4a5568;font-size:11pt;font-weight:600'>{title}</span>")
        widget.setXRange(0, 5000, padding=0)
        widget.getAxis('bottom').setPen(pg.mkPen('#e2e8f0'))
        widget.getAxis('left').setPen(pg.mkPen('#e2e8f0'))
        widget.getAxis('bottom').setTextPen(pg.mkPen('#718096'))
        widget.getAxis('left').setTextPen(pg.mkPen('#718096'))

    def _set_status(self, state: str, filename: str = ""):
        self._status_state_label.setText(state)
        self._status_file_label.setText(filename)

    def _update_gain_label(self, tab_idx, slider_idx):
        """Refresh the small gain value label under each slider."""
        lbl = self.findChild(QtWidgets.QLabel, f"gainLabel_{slider_idx}")
        if lbl:
            lbl.setText(f"{self.gain[tab_idx][slider_idx]:.1f}")

    def _update_spectro_labels(self):
        for attr, obj_name in [("verticalSlider_11", "spectroLabel_verticalSlider_11"),
                                ("verticalSlider_12", "spectroLabel_verticalSlider_12")]:
            slider = getattr(self, attr)
            lbl = self.findChild(QtWidgets.QLabel, obj_name)
            if lbl:
                lbl.setText(f"{slider.value()}%")

    # ─── tab management ───────────────────────────────────────────────────────

    def close_tab(self, index):
        if self.tabWidget.count() == 1:
            return   # keep at least one tab
        if self.timer[index] and self.timer[index] != 0:
            self.timer[index].stop()
        self.tabWidget.removeTab(index)
        for lst in [self.input_graph, self.output_graph, self.spectro_widgets,
                    self.current_color, self.spectro_flag, self.signals,
                    self.file_name, self.input_signal, self.freq_sampling,
                    self.output_signal, self.spectro_min, self.spectro_max,
                    self.timer, self.interval, self.index, self.gain]:
            lst.pop(index)

    def select(self):
        self.current_tab_index = self.tabWidget.currentIndex()
        if self.signals[self.current_tab_index] == 0:
            self.disable_items()
            self._set_status("No file loaded")
        else:
            self.enable_items()
            self._set_status("Ready", self.file_name[self.current_tab_index])

        for i in range(10):
            self.slider_list[i].setValue(int(self.gain[self.current_tab_index][i] * 10))
            self._update_gain_label(self.current_tab_index, i)

        self.verticalSlider_11.setValue(int(self.spectro_min[self.current_tab_index] * 100))
        self.verticalSlider_12.setValue(int(self.spectro_max[self.current_tab_index] * 100))
        self._update_spectro_labels()

    # ─── gain sliders ─────────────────────────────────────────────────────────

    def get_gain(self, i):
        if self.signals[self.current_tab_index] == 0:
            return
        self.gain[self.current_tab_index][i] = float(self.slider_list[i].value()) / 10
        self._update_gain_label(self.current_tab_index, i)

        # persist to CSV
        if os.path.isfile('sliders.csv'):
            df = pd.read_csv('sliders.csv', index_col=0)
        else:
            df = pd.DataFrame(columns=['name'] + [f'gain_{j+1}' for j in range(10)])

        fname = self.file_name[self.current_tab_index]
        row_data = [fname] + self.gain[self.current_tab_index]
        if df.isin([fname]).any().any():
            idx = df.index[df['name'] == fname].tolist()[0]
            df.iloc[idx, 1:] = self.gain[self.current_tab_index]
        else:
            df.loc[len(df)] = row_data
        df.to_csv('sliders.csv')

        self.plot_output()
        self.plot_spectro(self.output_signal[self.current_tab_index],
                          self.color[self.current_color[self.current_tab_index]])

        y_range = self.input_graph[self.current_tab_index].getViewBox().state['viewRange'][1]
        g = self.gain[self.current_tab_index][i]
        self.output_graph[self.current_tab_index].setYRange(
            y_range[0] * g, y_range[1] * g, padding=0
        )

    # ─── file loading ─────────────────────────────────────────────────────────

    def openfile(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open Signal File', "", "Signal files (*.csv *.wav)"
        )
        if not file_path:
            return

        self._set_status("Loading…")
        QtWidgets.QApplication.processEvents()

        try:
            if file_path.endswith('.wav'):
                data = wavfile.read(file_path)
                audio_df = pd.DataFrame(data)
                self.freq_sampling[self.current_tab_index] = audio_df.iloc[0, 0]
                self.input_signal[self.current_tab_index]  = audio_df.iloc[1, 0]
            else:
                df = pd.read_csv(file_path)
                self.input_signal[self.current_tab_index]  = df.iloc[:, 0]
                self.freq_sampling[self.current_tab_index] = 1000

            self.signals[self.current_tab_index]   = file_path
            self.file_name[self.current_tab_index] = os.path.basename(file_path)

            self.reset_widget()
            self.plot_input()
            self.plot_output()
            self.enable_items()
            self.start_animation()
            self.update_sliders()
            self.spectro_sliders()
            self.plot_spectro(self.output_signal[self.current_tab_index], self.color[0])

            self._set_status("Playing", self.file_name[self.current_tab_index])
            self.tabWidget.setTabText(
                self.current_tab_index,
                self.file_name[self.current_tab_index]
            )

        except Exception as e:
            QMessageBox.critical(self, "Load Error", f"Could not open file:\n{e}")
            self._set_status("Error loading file")

    def update_sliders(self):
        fname = self.file_name[self.current_tab_index]
        if os.path.isfile('sliders.csv'):
            df = pd.read_csv('sliders.csv', index_col=0)
            self.df = df
            if df.isin([fname]).any().any():
                self.gain[self.current_tab_index] = \
                    df[df['name'] == fname].values.tolist()[0][1:]
        else:
            data = [fname] + self.gain[self.current_tab_index]
            self.df = pd.DataFrame([data])
            self.df.columns = ['name'] + [f'gain_{j+1}' for j in range(10)]
            self.df.to_csv('sliders.csv')

        for i in range(10):
            self.slider_list[i].setValue(int(self.gain[self.current_tab_index][i] * 10))
            self._update_gain_label(self.current_tab_index, i)

    # ─── plotting ─────────────────────────────────────────────────────────────

    def plot_input(self):
        sig = self.input_signal[self.current_tab_index]
        self._set_limits(self.input_graph[self.current_tab_index], sig)
        self.input_graph[self.current_tab_index].plot(
            sig, name=self.file_name[self.current_tab_index], pen=self.pen
        )

    def plot_output(self):
        self.output_signal[self.current_tab_index], _ = fourier(
            self.input_signal[self.current_tab_index],
            self.gain[self.current_tab_index]
        )
        out = self.output_signal[self.current_tab_index]
        self.output_graph[self.current_tab_index].clear()
        self.output_graph[self.current_tab_index].plot(
            out, name=self.file_name[self.current_tab_index], pen=self.pen
        )
        self._set_limits(self.output_graph[self.current_tab_index], out)

    # ─── animation ────────────────────────────────────────────────────────────

    def start_animation(self):
        self.index[self.current_tab_index]    = 0
        self.interval[self.current_tab_index] = 25
        i = self.current_tab_index
        t = QtCore.QTimer()
        t.setInterval(50)
        t.timeout.connect(lambda: self.update_plot(i))
        self.timer[i] = t
        t.start()

    def update_plot(self, i):
        if self.signals[i] == 0:
            return
        self.index[i] += self.interval[i]
        self.input_graph[i].setXRange(self.index[i], 5000 + self.index[i], padding=0)
        self.output_graph[i].setXRange(self.index[i], 5000 + self.index[i], padding=0)

    # ─── playback controls ────────────────────────────────────────────────────

    def play(self):
        t = self.timer[self.current_tab_index]
        if t and t != 0:
            self._set_limits(self.output_graph[self.current_tab_index],
                             self.output_signal[self.current_tab_index])
            t.start()
            self._set_status("Playing", self.file_name[self.current_tab_index])

    def pause(self):
        t = self.timer[self.current_tab_index]
        if t and t != 0:
            t.stop()
            self._set_status("Paused", self.file_name[self.current_tab_index])

    def stop(self):
        t = self.timer[self.current_tab_index]
        if t and t != 0:
            t.stop()
            self.index[self.current_tab_index] = 0
            self.input_graph[self.current_tab_index].setXRange(0, 5000, padding=0)
            self.output_graph[self.current_tab_index].setXRange(0, 5000, padding=0)
            self._set_status("Stopped", self.file_name[self.current_tab_index])

    def playback(self, sign):
        iv = self.interval[self.current_tab_index]
        new_iv = iv + sign * 10
        if 5 < new_iv < 45:
            self.interval[self.current_tab_index] = new_iv
            self.timer[self.current_tab_index].setInterval(new_iv)
            speed = "faster" if sign > 0 else "slower"
            self._set_status(f"Speed: {speed} (interval={new_iv}ms)",
                             self.file_name[self.current_tab_index])

    # ─── close signal ─────────────────────────────────────────────────────────

    def close_signal(self):
        t = self.timer[self.current_tab_index]
        if t and t != 0:
            t.stop()
        self.timer[self.current_tab_index]   = 0
        self.signals[self.current_tab_index] = 0
        self.reset_widget()
        self.disable_items()
        self.tabWidget.setTabText(self.current_tab_index,
                                  f"Signal {self.current_tab_index + 1}")
        self._set_status("No file loaded")

    # ─── audio ────────────────────────────────────────────────────────────────

    def play_sound(self):
        try:
            out  = self.output_signal[self.current_tab_index]
            fs   = self.freq_sampling[self.current_tab_index]
            duration = len(out) / fs
            sd.play(out, fs)
            self._set_status("Playing audio…", self.file_name[self.current_tab_index])
            time.sleep(duration)
            sd.stop()
            self._set_status("Ready", self.file_name[self.current_tab_index])
        except Exception as e:
            QMessageBox.warning(self, "Audio Error", str(e))

    # ─── enable / disable toolbar items ──────────────────────────────────────

    def enable_items(self):
        for act in [self.actionZoom_in, self.actionZoom_out, self.actionPlay,
                    self.actionPause, self.actionStop, self.actionClose,
                    self.actionFaster, self.actionSlower, self.actionSpectrogram,
                    self.actionScroll_right, self.actionScroll_left,
                    self.actionScroll_up, self.actionScroll_down,
                    self.actionColor_1, self.actionColor_2, self.actionColor_3,
                    self.actionColor_4, self.actionColor_5, self.actionSave_as_PDF]:
            act.setEnabled(True)
        self.pushButton.setEnabled(True)
        for s in self.slider_list:
            s.setEnabled(True)
        self.verticalSlider_11.setEnabled(True)
        self.verticalSlider_12.setEnabled(True)

    def disable_items(self):
        for act in [self.actionZoom_in, self.actionZoom_out, self.actionPlay,
                    self.actionPause, self.actionStop, self.actionClose,
                    self.actionFaster, self.actionSlower, self.actionSpectrogram,
                    self.actionScroll_right, self.actionScroll_left,
                    self.actionScroll_up, self.actionScroll_down,
                    self.actionColor_1, self.actionColor_2, self.actionColor_3,
                    self.actionColor_4, self.actionColor_5, self.actionSave_as_PDF]:
            act.setEnabled(False)
        self.pushButton.setEnabled(False)
        for s in self.slider_list:
            s.setEnabled(False)
        self.verticalSlider_11.setEnabled(False)
        self.verticalSlider_12.setEnabled(False)

    # ─── spectrogram ──────────────────────────────────────────────────────────

    def toggle_spectro(self):
        if self.signals[self.current_tab_index] == 0:
            return
        if self.spectro_flag[self.current_tab_index] == 0:
            self.spectro_widgets[self.current_tab_index].show()
            self.spectro_flag[self.current_tab_index] = 1
            self._set_status("Spectrogram visible", self.file_name[self.current_tab_index])
        else:
            self.spectro_widgets[self.current_tab_index].hide()
            self.spectro_flag[self.current_tab_index] = 0
            self._set_status("Spectrogram hidden", self.file_name[self.current_tab_index])

    def spectro_sliders(self):
        self.verticalSlider_11.setValue(0)
        self.verticalSlider_12.setValue(100)
        self.spectro_min[self.current_tab_index] = 0.0
        self.spectro_max[self.current_tab_index] = 1.0
        self._update_spectro_labels()

    def _on_spectro_slider(self):
        if self.signals[self.current_tab_index] == 0:
            return
        self.update_spectro()
        self._update_spectro_labels()

    def update_spectro(self):
        self.spectro_min[self.current_tab_index] = float(self.verticalSlider_11.value()) / 100
        self.spectro_max[self.current_tab_index] = float(self.verticalSlider_12.value()) / 100
        self.verticalSlider_11.setMaximum(self.verticalSlider_12.value())
        self.verticalSlider_12.setMinimum(self.verticalSlider_11.value())
        spectro_values = spectro_range(
            self.output_signal[self.current_tab_index],
            self.spectro_min[self.current_tab_index],
            self.spectro_max[self.current_tab_index]
        )
        self.plot_spectro(spectro_values, self.color[self.current_color[self.current_tab_index]])
        self.spectro_widgets[self.current_tab_index].setYRange(
            self.f[-1] * self.spectro_min[self.current_tab_index],
            self.f[-1] * self.spectro_max[self.current_tab_index],
            padding=0
        )

    def plot_spectro(self, output_signal, color):
        fs = self.freq_sampling[self.current_tab_index]
        self.f, self.t, self.Sxx = signal.spectrogram(output_signal, fs)

        w = self.spectro_widgets[self.current_tab_index]
        w.clear()
        pg.setConfigOptions(imageAxisOrder='row-major')

        img  = pg.ImageItem()
        w.addItem(img)
        hist = pg.HistogramLUTItem()
        hist.setImageItem(img)
        hist.setLevels(np.min(self.Sxx), np.max(self.Sxx))
        hist.gradient.restoreState({'mode': 'rgb', 'ticks': color})
        img.setImage(self.Sxx)
        # img.scale() was removed in newer pyqtgraph; use setRect instead
        img.setRect(QtCore.QRectF(0, 0, self.t[-1], self.f[-1]))

        w.setXRange(0, self.t[-1], padding=0)
        w.setYRange(0, self.f[-1], padding=0)
        w.setLimits(xMin=0, xMax=self.t[-1], yMin=0, yMax=self.f[-1])
        w.setLabel('bottom', "Time", units='s')
        w.setLabel('left',   "Frequency", units='Hz')

    def color_palette(self, i):
        self.plot_spectro(self.output_signal[self.current_tab_index], self.color[i])
        self.current_color[self.current_tab_index] = i

    # ─── zoom / scroll ────────────────────────────────────────────────────────

    def zoom(self, factor):
        self.input_graph[self.current_tab_index].plotItem.getViewBox().scaleBy((factor, factor))
        self.output_graph[self.current_tab_index].plotItem.getViewBox().scaleBy((factor, factor))

    def scroll_x(self, sign):
        xr = self.input_graph[self.current_tab_index].getViewBox().state['viewRange'][0]
        rx = 0.1 * (xr[1] - xr[0]) * sign
        self.input_graph[self.current_tab_index].setXRange(xr[0] + rx, xr[1] + rx, padding=0)
        self.output_graph[self.current_tab_index].setXRange(xr[0] + rx, xr[1] + rx, padding=0)

    def scroll_y(self, sign):
        for graph in [self.input_graph[self.current_tab_index],
                      self.output_graph[self.current_tab_index]]:
            yr = graph.getViewBox().state['viewRange'][1]
            ry = 0.1 * (yr[1] - yr[0]) * sign
            graph.setYRange(yr[0] + ry, yr[1] + ry, padding=0)

    # ─── widget helpers ────────────────────────────────────────────────────────

    def reset_widget(self):
        idx = self.current_tab_index
        for w in [self.input_graph[idx], self.output_graph[idx]]:
            w.clear()
            w.setLabel('bottom', "Time (ms)")
        self.spectro_widgets[idx].clear()
        self.spectro_widgets[idx].hide()
        self.spectro_flag[idx] = 0

    def _set_limits(self, widget, data):
        lo, hi = float(min(data)), float(max(data))
        widget.setYRange(lo, hi, padding=0)
        widget.setLimits(xMin=0, xMax=len(data) - 1, yMin=lo, yMax=hi)

    # ─── toolbar / status visibility ──────────────────────────────────────────

    def toggle_tool(self, checked):
        self.toolBar.setVisible(checked)

    def toggle_status(self, checked):
        self.statusbar.setVisible(checked)

    # ─── PDF export ───────────────────────────────────────────────────────────

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (*.pdf);;All Files(*)')
        if not fn:
            return
        if QFileInfo(fn).suffix() == "":
            fn += '.pdf'
        if not self.input_graph[self.current_tab_index].scene():
            return

        self._set_status("Exporting PDF…")
        QtWidgets.QApplication.processEvents()
        try:
            pg.exporters.ImageExporter(
                self.input_graph[self.current_tab_index].scene()
            ).export('input_signal.png')
            pg.exporters.ImageExporter(
                self.output_graph[self.current_tab_index].scene()
            ).export('output_signal.png')
            self.spectro_widgets[self.current_tab_index].show()
            pg.exporters.ImageExporter(
                self.spectro_widgets[self.current_tab_index].scene()
            ).export('spectrogram.png')

            pdf = GeneratePDF(fn)
            pdf.create_pdf()
            pdf.save_pdf()

            if self.spectro_flag[self.current_tab_index] == 0:
                self.spectro_widgets[self.current_tab_index].hide()

            self._set_status("PDF saved", fn)
        except Exception as e:
            QMessageBox.critical(self, "Export Error", str(e))
            self._set_status("PDF export failed")

    # ─── about dialog ─────────────────────────────────────────────────────────

    def pop_up(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("About Signal Viewer")
        msg.setText("<b>Signal Viewer</b> &nbsp; v1.0")
        msg.setInformativeText(
            "A multi-channel biomedical signal viewer with equalizer, "
            "spectrogram, and PDF export.\n\n"
            "© 2021 SBME, Cairo University"
        )
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # ─── new tab ──────────────────────────────────────────────────────────────

    def new_tab(self):
        n = self.i
        tab_widget = QtWidgets.QWidget()
        tab_widget.setObjectName(f"tab{n}")
        tab_widget.setStyleSheet("background-color: #ffffff;")

        grid = QtWidgets.QGridLayout(tab_widget)
        grid.setContentsMargins(8, 8, 8, 8)
        grid.setSpacing(8)

        h_layout  = QtWidgets.QHBoxLayout()
        left_col  = QtWidgets.QVBoxLayout()
        left_col.setSpacing(8)
        right_col = QtWidgets.QVBoxLayout()

        in_w  = PlotWidget(tab_widget)
        out_w = PlotWidget(tab_widget)
        sp_w  = PlotWidget(tab_widget)

        left_col.addWidget(in_w)
        left_col.addWidget(out_w)
        right_col.addWidget(sp_w)

        h_layout.addLayout(left_col)
        h_layout.addLayout(right_col)
        grid.addLayout(h_layout, 0, 0, 1, 1)

        self.tabWidget.addTab(tab_widget, f" Signal {n} ")

        self._configure_plot(in_w,  f"Input Signal {n}")
        self._configure_plot(out_w, f"Output Signal {n}")
        self._configure_plot(sp_w,  f"Spectrogram {n}")
        sp_w.hide()

        self.input_graph.append(in_w)
        self.output_graph.append(out_w)
        self.spectro_widgets.append(sp_w)

        self.tab[f"tab{n}"] = tab_widget
        self.current_color.append(0)
        self.spectro_flag.append(0)
        self.signals.append(0)
        self.file_name.append(0)
        self.input_signal.append(0)
        self.freq_sampling.append(0)
        self.output_signal.append(0)
        self.spectro_min.append(0)
        self.spectro_max.append(1)
        self.timer.append(0)
        self.interval.append(0)
        self.index.append(0)
        self.gain.append(10 * [1])

        self.i += 1
        self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
