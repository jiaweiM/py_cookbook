import threading


class MaoMessager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = MaoMessager(name="Send out messages")
y = MaoMessager(name="Receive messages")
x.start()
y.start()
