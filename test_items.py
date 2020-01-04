import time

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0 , "Button not found"
