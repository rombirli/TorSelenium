from bots import lematin_unlike

N_THREADS: int = 2  # number of parallel instances of the bot
N_ITER: int = 200 # total number of bot iterations
TIMEOUT = 20 # leave 20 seconds to the bot to do its task
CHROME_DRIVER: str = 'res/chromedriver/chromedriver_chrome96.exe'  # path to chromedriver for the correct version of chrome
BOT_FUNCTION = lematin_unlike # must have signature webdriver.WebDriver -> None

