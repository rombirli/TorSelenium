from selenium.webdriver.remote.webdriver import WebDriver, WebElement


def click2(browser: WebDriver, elem: WebElement) -> None:
    browser.execute_script("arguments[0].click();", elem)
