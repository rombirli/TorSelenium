from selenium.webdriver.remote import webdriver

def print_useragent(browser: webdriver.WebDriver) -> None:
    browser.get("https://icanhazip.com")
    print(browser.find_element_by_tag_name('pre').text)

def print_ip(browser: webdriver.WebDriver) -> None:
    browser.get("https://icanhazip.com")
    print(browser.find_element_by_tag_name('pre').text)


def lematin_unlike(browser: webdriver.WebDriver) -> None:
    print_ip(browser)
    browser.get("https://www.lematin.ch/story/8422-nouveaux-cas-enregistres-en-suisse-22-morts-834462679038")
    for elem in browser.find_elements_by_class_name('RatingItem_downRating__1fLK-'):
        browser.execute_script("arguments[0].click();", elem) # instead of elem.click because of this : https://stackoverflow.com/questions/56194094/how-to-fix-this-issue-element-not-interactable-selenium-python
        print('One dislike more for le matin :)')
