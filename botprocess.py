from sys import argv
from config import BOT_FUNCTION
from config import CHROME_DRIVER
from selenium.webdriver import Chrome, ChromeOptions
from ntorlib.ntorlib import get_proxy
from dummy_useragent import UserAgent

ua = UserAgent()


def create_browser(i: int, user_agent=None):
    if (user_agent is None):
        user_agent = ua.random()
    options = ChromeOptions()
    options.add_argument(f'--proxy-server={get_proxy(i)}')
    # options.add_argument(f'--user-agent={user_agent}')
    return Chrome(executable_path=CHROME_DRIVER, options=options)


if len(argv) == 2:
    i = int(argv[1])
    b = create_browser(i)
    try:
        BOT_FUNCTION(b)
    except:
        print(f'A problem happened with botprocess {i}')
    b.quit()

else:
    print(f'Error launching a botprocess')

quit()
