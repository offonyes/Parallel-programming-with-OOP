import concurrent.futures
import random as rd
from PyQt5.QtCore import *
import time
from .Figures import *

def work(_):
    results = [
        Trapezoid([rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Rectangle([rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Square([rd.randint(1, 10)]).area()
    ]

def work_for_proc(_):
    results = [
        Trapezoid([rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Rectangle([rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Square([rd.randint(1, 10)]).area()
    ]
def work_for_process_pool_executor(numb, _):
    with concurrent.futures.ThreadPoolExecutor(20) as executor:
        executor.map(work_for_proc, range(numb // 20))

class WorkWithFigures(QObject):
    progress_bar = pyqtSignal(int, int)
    time = pyqtSignal(float, int)
    def __init__(self, number, index):
        super(WorkWithFigures, self).__init__()
        self.number = number
        self.index = index

    def norm_work(self, i):
        results = []
        results.append(Trapezoid([rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10)]).area())
        results.append(Rectangle([rd.randint(1, 10), rd.randint(1, 10)]).area())
        results.append(Square([rd.randint(1, 10)]).area())
        self.progress_bar.emit(i + 1, self.index)
        return results

    def work_thread(self, i):
        results = [
        Trapezoid([rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Rectangle([rd.randint(1, 10), rd.randint(1, 10)]).area(),
        Square([rd.randint(1, 10)]).area()
    ]
        self.progress_bar.emit(i + 1, self.index)
    
    def get_normal(self):
        start = time.perf_counter()
        result = list(map(self.norm_work,[i for i in range(self.number)]))
        finish = time.perf_counter()
        self.time.emit(finish - start, self.index)

    def get_threading(self):
        start = time.perf_counter()

        with (concurrent.futures.ThreadPoolExecutor() as executor):
            executor.map(self.work_thread, range(self.number))
        finish = time.perf_counter()
        self.time.emit(finish - start, self.index)

    def get_myltiprocessing(self):
        start = time.perf_counter()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(work, i) for i in range(self.number)]

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            result = future.result()
            self.progress_bar.emit(i + 1, self.index)

        finish = time.perf_counter()
        self.time.emit(finish - start, self.index)

    def get_united(self):
        start = time.perf_counter()
        with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(work_for_process_pool_executor,self.number, i) for i in range(5)]

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            result = future.result()
            self.progress_bar.emit(i + 1, self.index)

        self.progress_bar.emit(self.number + 1, self.index)
        finish = time.perf_counter()
        self.time.emit(finish - start, self.index)