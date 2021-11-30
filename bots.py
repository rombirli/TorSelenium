import time

from selenium.webdriver.remote.webdriver import WebDriver
from utils import click2


def print_useragent(browser: WebDriver) -> None:
    print(browser.execute_script("return navigator.userAgent;"))


def print_ip(browser: WebDriver) -> None:
    browser.get("https://icanhazip.com")
    print(browser.find_element_by_tag_name('pre').text)





def lematin_unlike(browser: WebDriver) -> None:
    print_ip(browser)
    browser.get("https://www.lematin.ch/story/8422-nouveaux-cas-enregistres-en-suisse-22-morts-834462679038")
    time.sleep(5)
    for elem in browser.find_elements_by_class_name('RatingItem_downRating__1fLK-'):
        for elem in browser.find_elements_by_class_name(
                'sc-1r4h1lh-2 jaCRUZ'):  # try to close every popup before every click
            browser.execute_script("arguments[0].click();", elem)
            print('closed a popup')
        browser.execute_script("arguments[0].click();",elem)  # instead of elem.click because of this : https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
    print('One 3-dislike serie more for le matin :)')
