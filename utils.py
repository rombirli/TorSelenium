from selenium.webdriver.remote.webdriver import WebDriver, WebElement


def click2(browser: WebDriver, elem: WebElement) -> None:
    """
    To fix not interactable error
    https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
    """
    browser.execute_script("arguments[0].click();", elem)
