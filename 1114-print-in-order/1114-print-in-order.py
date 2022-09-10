import threading
class Foo:
    def __init__(self):
        self.lock12 = threading.Lock()
        self.lock23 = threading.Lock()
        self.lock12.acquire()
        self.lock23.acquire()
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock12.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock12:
            printSecond()
            self.lock23.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.lock23:
            printThird()
