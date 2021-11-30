from subprocess import Popen
from sys import argv

from config import N_ITER, N_THREADS, TIMEOUT

from ntorlib.ntorlib import create_n_dependencies, clean_dependencies, run_n_tor, run_1_tor
from utils import join_all


def create_bot_process(i: int):
    return Popen([fr'venv\Scripts\python.exe', f'botprocess.py', str(i)], shell=True, )


def run_main():
    clean_dependencies()
    create_n_dependencies(N_THREADS)
    for k in range(0, N_ITER, N_THREADS):
        tor_threads = run_n_tor(N_THREADS)
        bot_threads = list(map(create_bot_process, range(N_THREADS)))
        join_all(bot_threads, timeout=TIMEOUT)
        for i, (bot_thread, tor_thread) in enumerate(zip(bot_threads, tor_threads)):
            bot_thread.kill()
            tor_thread.kill()


run_main()
