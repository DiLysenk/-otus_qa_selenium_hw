from pageobject.RegisterPage import RegisterPage
from pageobject.AdminPage import AdminPage
from pageobject.LoginPage import LoginAdminPage
from pageobject.MainPage import MainPage
from faker import Faker

myFactory = Faker()


def test_registration(browser):
    browser.get('http://localhost/index.php?route=account/register')
    RegisterPage(browser). \
        fill_form(myFactory.name(), myFactory.email()). \
        agree_polycy(). \
        click_continue()
    assert browser.current_url == "http://localhost/index.php?route=account/success", 'неудача'


def test_add_new_item(browser):
    browser.get('http://localhost/admin/')
    name = myFactory.color()
    LoginAdminPage(browser).login_admin()
    AdminPage(browser).go_to_Products() \
        .add_product(name)
    assert LoginAdminPage(browser).element_text(name), f"не найден товар{name}"


def test_delete_item(browser):
    browser.get('http://localhost/admin/')
    LoginAdminPage(browser).login_admin()
    AdminPage(browser).go_to_Products() \
        .select_product() \
        .delete_product()
    assert AdminPage(browser).element(AdminPage.SUCCESS_DELETE), "товар не удалён"


def test_switch_currency(browser):
    browser.get("http://localhost/index.php?route=common/home")
    MainPage(browser).change_currency()
    assert MainPage(browser).element_text('£'), "валюта не переведена"
