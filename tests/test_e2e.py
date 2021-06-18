from pageobject.RegisterPage import RegisterPage
from pageobject.AdminPage import AdminPage
from pageobject.LoginPage import LoginAdminPage
from pageobject.MainPage import MainPage
import pytest
from faker import Faker

myFactory = Faker()

@pytest.mark.usefixtures('loging')
def test_registration(browser):
    RegisterPage(browser). \
        forward_to_url(RegisterPage.URL_REGISTER). \
        fill_form(myFactory.name(), myFactory.email()). \
        agree_polycy(). \
        click_continue()
    assert browser.current_url == "http://localhost/index.php?route=account/success", 'неудача'

@pytest.mark.usefixtures('loging')
def test_add_new_item(browser):

    name = myFactory.color()
    LoginAdminPage(browser).\
        forward_to_url(LoginAdminPage.ADMIN_PAGE).\
        login_admin()
    AdminPage(browser).go_to_Products() \
        .add_product(name)
    assert LoginAdminPage(browser).element_text(name), f"не найден товар{name}"

@pytest.mark.usefixtures('loging')
def test_delete_item(browser):
    LoginAdminPage(browser).\
        forward_to_url(LoginAdminPage.ADMIN_PAGE).\
        login_admin()
    AdminPage(browser).go_to_Products() \
        .select_product() \
        .delete_product()
    assert AdminPage(browser).element_css(AdminPage.SUCCESS_DELETE), "товар не удалён"

@pytest.mark.usefixtures('loging')
def test_switch_currency(browser):
    MainPage(browser).\
        forward_to_url(MainPage.OpenCArt).\
        change_currency()
    assert MainPage(browser).element_text('£'), "валюта не переведена"
