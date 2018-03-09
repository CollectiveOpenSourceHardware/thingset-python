import queue

class Listener(object):
    def __init__(self):
        self.buffer = queue.Queue(0)

    def listen(self, timeout=1):
        try:
            self.buffer.get(block=True, timeout=timeout)
        except queue.Empty:
            return None
