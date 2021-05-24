from pageobject.RegisterPage import RegisterPage
from time import sleep



def test_registration(browser):
    browser.get('http://localhost/index.php?route=account/register')
    RegisterPage(browser).\
        fill_form().\
        agree_polycy().\
        click_continue()
    sleep(5)
    assert browser.current_url == "http://localhost/index.php?route=account/success", 'неудача'



def test_add_new_item(browser):
    pass

def test_delete_item(browser):
    pass

def test_switch_currency(browser):
    pass

