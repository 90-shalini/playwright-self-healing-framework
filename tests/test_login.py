from pages.login_page import LoginPage
from pages.home_page import HomePage

from utils.asserter import Asserter

url = "https://www.saucedemo.com"
def test_invalid_login(page):
    page.goto(url)
    login_page = LoginPage(page)
    asserter = Asserter(page)

    login_page.login("invalid_user", "secret_sauce")
    asserter.element_visible("h3[data-test=\"error\"]", "do not match")
    
def test_empty_username(page):
    page.goto(url)
    login_page = LoginPage(page)
    asserter = Asserter(page)

    login_page.login("", "secret_sauce")
    asserter.element_visible("h3[data-test=\"error\"]", "Username is required")
    
def test_empty_password(page):
    page.goto(url)
    login_page = LoginPage(page)
    asserter = Asserter(page)

    login_page.login("standard_user", "")
    asserter.element_visible("h3[data-test=\"error\"]", "Password is required")

def test_locked_user_login(page):
    page.goto(url)
    login_page = LoginPage(page)
    asserter = Asserter(page)

    login_page.login("locked_out_user", "secret_sauce")
    asserter.element_visible("h3[data-test=\"error\"]", " Sorry, this user has been locked out")

def test_login(page):
    page.goto(url)
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

def test_add_product_to_cart(page):
    page.goto(url)
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

    home_page = HomePage(page)
    home_page.add_product_to_cart()

def test_remove_product_to_cart(page):
    page.goto(url)
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

    home_page = HomePage(page)
    home_page.remove_product_to_cart()


def test_logout(page):
    page.goto(url)
    login_page = LoginPage(page)
    asserter = Asserter(page)
    login_page.login("standard_user", "secret_sauce")
    asserter.element_visible("div[class=\"app_logo\"]", "Swag Labs")
    
    home_page = HomePage(page)
    home_page.logout()