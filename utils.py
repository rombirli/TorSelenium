from threading import Thread

from typing import List, Optional



def join_all(threads: List[Thread], timeout: Optional[float] = None):
    """
    if you write
    for thread in threads : thread.join(timeout=timeout)
    Some thread join after some time and total timeout will be longer
    join_all is to fix it
    """
    t = Thread(target=lambda: [thread.join() for thread in threads])
    t.start()
    t.join(timeout=timeout)






