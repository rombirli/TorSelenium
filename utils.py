import time
from datetime import datetime, timedelta


def join_all(threads, timeout):
    t0 = datetime.now()
    while True:
        if datetime.now() - t0 >= timedelta(seconds=timeout) or all([thread.poll() is not None for thread in threads]):
            return
        else:
            time.sleep(.5)
