import time
from time import sleep
from random import random
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


############################# HELPER FUNCTIONS & OBJECTS #############################
class Counter:
    i: int = 0

    def inc(self) -> int:
        self.i = self.i + 1
        return self.i


counter = Counter()


def click2(browser: WebDriver, elem: WebElement) -> None:
    """
    To fix not interactable error
    https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
    """
    browser.execute_script("arguments[0].click();", elem)


def print_useragent(browser: WebDriver) -> None:
    print(browser.execute_script("return navigator.userAgent;"))


def print_ip(browser: WebDriver) -> None:
    browser.get("https://icanhazip.com")
    print(browser.find_element_by_tag_name('pre').text)


def randsleep(min_t: float, max_t: float) -> None:
    dt = max_t - min_t
    time.sleep(min_t + dt * random())


################################ BOTS ################################
def lematin_dislike(browser: WebDriver) -> None:
    print_useragent(browser)
    print_ip(browser)
    browser.get("https://www.lematin.ch/story/8422-nouveaux-cas-enregistres-en-suisse-22-morts-834462679038")
    elems = browser.find_elements_by_class_name('RatingItem_downRating__1fLK-')
    for elem in elems:
        for elem in browser.find_elements_by_class_name('sc-1r4h1lh-2 jaCRUZ'):  # try to close every popup before every click
            click2(browser, elem)
            print('closed a popup')
        randsleep(0, 3)
        click2(browser, elem)
    if len(elems) > 0:
        print(f'{counter.inc()} dislikes for le matin')
