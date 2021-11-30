import time
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


############################# HELPER FUNCTIONS #############################
class Counter:
    i: int = 0

    def inc(self) -> int:
        self.i = self.i + 1
        return self.i


def click2(browser: WebDriver, elem: WebElement) -> None:
    """
    To fix not interactable error
    https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
    """
    browser.execute_script("arguments[0].click();", elem)


counter = Counter()


################################ BOTS ################################
def print_useragent(browser: WebDriver) -> None:
    print(browser.execute_script("return navigator.userAgent;"))


def print_ip(browser: WebDriver) -> None:
    browser.get("https://icanhazip.com")
    print(browser.find_element_by_tag_name('pre').text)


def lematin_dislike(browser: WebDriver) -> None:
    print_useragent(browser)
    print_ip(browser)
    browser.get("https://www.lematin.ch/story/8422-nouveaux-cas-enregistres-en-suisse-22-morts-834462679038")
    for elem in browser.find_elements_by_class_name('RatingItem_downRating__1fLK-'):
        for elem in browser.find_elements_by_class_name(
                'sc-1r4h1lh-2 jaCRUZ'):  # try to close every popup before every click
            click2(browser, elem)
            print('closed a popup')
        click2(browser, elem)  #
    print(f'{counter.inc()} dislikes for le matin')
