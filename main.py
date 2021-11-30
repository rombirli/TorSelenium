from config import N_ITER, N_THREADS, CHROME_DRIVER, BOT_FUNCTION, TIMEOUT
from fake_useragent.fake import UserAgent
from selenium.webdriver import Chrome, ChromeOptions
from threading import Thread
from utils import join_all
from ntorlib.ntorlib import get_proxy, clean_dependencies, create_n_dependencies, run_n_tor

ua = UserAgent(fallback='-')


def create_thread(i: int):
    def create_browser(i: int):
        options = ChromeOptions()
        options.add_argument(f'--proxy-server={get_proxy(i)}')
        options.add_argument(f'--user-agent={ua.update()}')
        return Chrome(executable_path=CHROME_DRIVER, options=options)

    def f():
        try:
            b = create_browser(i)
            BOT_FUNCTION(b)
            b.quit()
        except:
            print(f'A problem happened with thread {i}')

    return Thread(target=f)


def run():
    clean_dependencies()
    create_n_dependencies(N_THREADS)
    for k in range(0, N_ITER, N_THREADS):
        tor_threads = run_n_tor(N_THREADS)
        bot_threads = list(map(create_thread, range(N_THREADS)))
        for thread in bot_threads:
            thread.start()
        join_all(bot_threads, TIMEOUT)
        for thread in tor_threads:
            thread.kill()


run()
