import time
from subprocess import Popen
from sys import argv

from config import N_ITER, N_THREADS, CHROME_DRIVER, BOT_FUNCTION, TIMEOUT
from config import CHROME_DRIVER
from selenium.webdriver import Chrome, ChromeOptions
from ntorlib.ntorlib import get_proxy, clean_dependencies, create_n_dependencies, run_n_tor
from dummy_useragent import UserAgent

ua = UserAgent()


def create_browser(i: int, user_agent=None):
    if (user_agent is None):
        user_agent = ua.random()
    options = ChromeOptions()
    options.add_argument(f'--proxy-server={get_proxy(i)}')
    options.add_argument(f'--user-agent={user_agent}')
    return Chrome(executable_path=CHROME_DRIVER, options=options)


def create_bot_process(i: int):
    def f():
        try:
            b = create_browser(i)
            BOT_FUNCTION(b)
            b.quit()
        except:
            print(f'A problem happened with thread {i}')

    return Popen(['python', 'botprocess.py', str(i)])


def run_main():
    clean_dependencies()
    create_n_dependencies(N_THREADS)
    for k in range(0, N_ITER, N_THREADS):
        tor_threads = run_n_tor(N_THREADS)
        bot_threads = list(map(create_bot_process, range(N_THREADS)))
        time.sleep(TIMEOUT)
        for bot_thread, tor_thread in zip(bot_threads, tor_threads):
            bot_thread.kill()
            tor_thread.kill()


if len(argv) > 2 and argv[1] == 'slave':
    t_id = int(argv[2])

else:
    run_main()
