from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Windows.MainWindow import Ui_MainWindow
from Utils.thread_for_qt import WorkWithFigures


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.all_number = None
        self.threads = None
        self.workers = None
        self.setupUi(self)
        self.pushButtonStart.clicked.connect(self.start_procces)
        self.num = 0

    def start_procces(self):

        self.pushButtonStart.setEnabled(False)
        self.groupBoxNumberOfFigures.setEnabled(False)
        self.groupBoxWorkingMode.setEnabled(False)
        self.all_number = self.spinBoxNumber.value()
        self.threads = {}
        self.workers = {}

        if self.checkBoxNorm.checkState() == 2:
            self.workers[1] = WorkWithFigures(self.all_number, 1)
            self.normal_progress_bar.setValue(0)
            self.start_thread(1, self.workers[1].get_normal)
            self.num += 1

        if self.checkBoxThreading.checkState() == 2:
            self.workers[2] = WorkWithFigures(self.all_number, index=2)
            self.threading_progress_bar.setValue(0)
            self.start_thread(2, self.workers[2].get_threading)
            self.num += 1

        if self.checkBoxMultithreading.checkState() == 2:
            self.workers[3] = WorkWithFigures(self.all_number, index=3)
            self.myltithreading_progress_bar.setValue(0)
            self.start_thread(3, self.workers[3].get_multiprocessing)
            self.num += 1

        if self.checkBoxUnited.checkState() == 2:
            self.workers[4] = WorkWithFigures(self.all_number, 4)
            self.united_progress_bar.setValue(0)
            self.start_thread(4, self.workers[4].get_united)
            self.num += 1

    def start_thread(self, index, worker_method):
        self.threads[index] = QThread()
        self.workers[index].moveToThread(self.threads[index])
        self.threads[index].started.connect(worker_method)
        self.workers[index].time.connect(self.time_func)
        self.workers[index].progress_bar.connect(self.progress_bar_func)
        self.threads[index].finished.connect(self.thread_finished)
        self.threads[index].start()

    def thread_finished(self):
        self.num -= 1

        if self.num == 0:
            self.pushButtonStart.setEnabled(True)
            self.groupBoxNumberOfFigures.setEnabled(True)
            self.groupBoxWorkingMode.setEnabled(True)
            QMessageBox.information(self, "Done", f"All operations are completed")

    def time_func(self, time, index):
        match index:
            case 1:
                self.normal_time_lbl.setText("%.7s" % time)
            case 2:
                self.theading_time_lbl.setText("%.7s" % time)
            case 3:
                self.procesing_time_lbl.setText("%.7s" % time)
            case 4:
                self.united_time_lbl.setText("%.7s" % time)
        self.threads[index].quit()
        self.threads[index].wait()

    def progress_bar_func(self, numb, index):
        match index:
            case 1:
                self.normal_progress_bar.setValue(int((numb / self.all_number) * 100))
            case 2:
                self.threading_progress_bar.setValue(int((numb / self.all_number) * 100))
            case 3:
                self.myltithreading_progress_bar.setValue(int((numb / self.all_number) * 100))
            case 4:
                self.united_progress_bar.setValue(int((numb / self.all_number) * 100))

    @staticmethod
    def on_close_event(event):
        event.accept()
