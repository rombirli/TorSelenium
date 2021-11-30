from threading import Thread

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from typing import List, Optional


def click2(browser: WebDriver, elem: WebElement) -> None:
    """
    To fix not interactable error
    https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
    """
    browser.execute_script("arguments[0].click();", elem)


def join_all(threads: List[Thread], timeout: Optional[float] = None):
    """
    if you write
    for thread in threads : thread.join(timeout=timeout)
    Some thread join after some time and
    """
    t = Thread(target=lambda: [thread.join() for thread in threads])
    t.join(timeout=timeout)
