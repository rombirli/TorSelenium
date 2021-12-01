from time import sleep
from random import random
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


def rand_sleep(min_t: float, max_t: float) -> None:
    dt = max_t - min_t
    sleep(min_t + dt * random())


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


def lematin_dislike(browser: WebDriver) -> None:
    print_useragent(browser)
    print_ip(browser)
    browser.get("https://www.lematin.ch/story/8422-nouveaux-cas-enregistres-en-suisse-22-morts-834462679038")
    dislike_buttons = browser.find_elements_by_class_name('RatingItem_downRating__1fLK-')
    print(f'found {len(dislike_buttons)} dislike buttons on this page')
    sleep(10)
    for dislike_button in dislike_buttons:
        rand_sleep(0, 1.5)
        for popup_close_x in browser.find_elements_by_class_name(
                'sc-1r4h1lh-2 jaCRUZ'):  # try to close every popup before every click
            click2(browser, popup_close_x)
            print('\tclosed a popup')
        rand_sleep(0, 1.5)
        click2(browser, dislike_button)


def adfly_click(browser: WebDriver) -> None:
    """
    Actually this doesn't work
    """
    # login :
    # email=zusmmuzozxeapdcvev@nvhrw.com
    # password=zusmmuzozxeapdcvev@nvhrw.com1
    browser.get('http://fumacrom.com/366Z6')
    click2(browser, browser.find_element_by_id('skip_bu2tton'))


def shortest_click(browser: WebDriver) -> None:
    # email=mbtxealazrfnlskshf@bvhrs.com
    # password=mbtxealazrfnlskshf@bvhrs.com
    pass


def linkslyco_click(browser: WebDriver) -> None:
    # https://linksly.co/member/links
    # email=gokkotutre@yevme.com
    # password=gokkotutre@yevme.com
    browser.get('https://linksly.co/fuckyourmom')
    click2(browser, browser.find_element_by_id('skip_bu2tton'))


def okio_click(browser: WebDriver) -> None:
    # email=gokkotutre@yevme.com
    # password=gokkotutre
    browser.get('https://oke.io/SedzVoIc')
    browser.execute_script("document.getElementById('link-view').submit()")