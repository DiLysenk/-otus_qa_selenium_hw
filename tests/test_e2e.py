from pageobject.RegisterPage import RegisterPage
from pageobject.AdminPage import AdminPage
from pageobject.LoginPage import LoginAdminPage
from pageobject.MainPage import MainPage
from time import sleep



def test_registration(browser):
    browser.get('http://localhost/index.php?route=account/register')
    RegisterPage(browser).\
        fill_form().\
        agree_polycy().\
        click_continue()
    assert browser.current_url == "http://localhost/index.php?route=account/success", 'неудача'



def test_add_new_item(browser):
    browser.get('http://localhost/admin/')
    LoginAdminPage(browser).login_admin()
    AdminPage(browser).go_to_Products()
    AdminPage(browser).add_product('bars3')
    sleep(5)

def test_delete_item(browser):
    browser.get('http://localhost/admin/')
    LoginAdminPage(browser).login_admin()
    AdminPage(browser).go_to_Products()
    AdminPage(browser).select_product()
    AdminPage(browser).delete_product()


def test_switch_currency(browser):
    browser.get("http://localhost/index.php?route=common/home")
    MainPage(browser).change_currency()
    sleep(5)


