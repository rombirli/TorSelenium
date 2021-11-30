from bots import lematin_dislike

N_THREADS: int = 4  # number of parallel instances of the bot
N_ITER: int = 2000 # total number of bot iterations
TIMEOUT = 20 # leave 20 seconds to the bot to do its task
CHROME_DRIVER: str = 'res/chromedrivers/chromedriver_chrome96.exe'  # path to chromedrivers for the correct version of chrome
BOT_FUNCTION = lematin_dislike # must have signature webdriver.WebDriver -> Any

