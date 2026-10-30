import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time:', round(time.time() - self.start, 2))


@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print('time:', round(time.time() - start, 2))


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(1.5)
