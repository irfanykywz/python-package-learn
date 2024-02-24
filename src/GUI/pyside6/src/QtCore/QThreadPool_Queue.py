from PySide6.QtCore import (
    QRunnable,
    QThreadPool,
    QThread,
    Signal,
)
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

import queue
import time

class Worker(QRunnable):
    def __init__(self, parentThread, index):
        super().__init__()
        self.parentThread = parentThread
        self.index = index
        self.status = parentThread.status
        self.process = parentThread.process
        self.totalPayload = len(parentThread.payload)
        self.live = True
        self.loop = {}

    def doing(self, data):
        self.process.emit(f'running on thread: {self.index}')
        print(data)
        self.process.emit(f'finished thread: {self.index}')
        time.sleep(3)

    def run(self):

        while self.live:

            # get task from put
            self.job = self.parentThread.theQueue.get()

            # if task none stop inifinite looop
            if self.job is None:
                self.parentThread.theQueue.task_done()
                return

            # start job
            if self.live: # check live if fast closed
                self.doing(self.job)

            # set done
            self.parentThread.theQueue.task_done()

            # dont run faster
            time.sleep(1)

    def terminate(self):
        # remove queue list
        self.parentThread.theQueue.empty()
        self.parentThread.theQueue.put(None)
        self.parentThread.theQueue.task_done()

        # stop while
        self.live = False

class Thread(QThread):

    status = Signal(tuple)
    process = Signal(tuple)

    def __init__(self, parent, payload):
        super().__init__(parent)
        self.parent = parent
        self.payload = payload

    def run(self):

        MAX_THREADS = 5
        self.theQueue = queue.Queue()
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(MAX_THREADS)
        self.workers = {}

        # create thread
        for thread in range(MAX_THREADS):
            self.workers[thread] = Worker(self, thread)
            self.pool.start(self.workers[thread])

        # insert payload as task
        for data in self.payload:
            self.theQueue.put(data)

        # Tell the threads in the pool to finish
        for i in range(MAX_THREADS):
            self.theQueue.put(None)

        # Wait all sub-thread done
        self.pool.waitForDone()

    def terminate(self):
        super().terminate()

        print('stop threadpool')
        self.pool.clear()
        self.pool.deleteLater()

        # stop worker
        print('stop worker')
        for worker in self.workers:
            self.workers[worker].terminate()

class Main(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):

        button = QPushButton('Start')
        button.clicked.connect(self.start)

        layout = QHBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def start(self):

        def status(val):
            print(val)
        def process(val):
            print(val)
        def started():
            print('started')
        def finished():
            print('finished')

        payload = [
         ['1'] for i in range(10)
        ]
        thread = Thread(self, payload)
        thread.status.connect(status)
        thread.process.connect(process)
        thread.started.connect(started)
        thread.finished.connect(finished)
        thread.start()


if __name__ == "__main__":
    app = QApplication([])

    window = Main()
    window.show()

    app.exec_()