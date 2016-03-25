from eventual import observable
import time
import threading


class Timer:
    def __init__(self, **kwargs):
        self.elapsedEvent = observable.Observable()
        self._started = False
        self.period = kwargs.pop('period')
        self.isAsync = kwargs.pop('async', True)

    def start(self):
        self._started = True

        thr = threading.Thread(target=self.__run, args=())
        thr.start()

    def stop(self):
        self._started = False

    def __run(self):
        while self._started:
            time.sleep(self.period)
            if self._started:
                if self.isAsync:
                    self.elapsedEvent.notifyObeserversAsync(self, None)
                else:
                    self.elapsedEvent.notifyObeservers(self, None)
