from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest
import faker
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# @pytest.mark.skip
@pytest.mark.need_review
@pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param(
                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                       marks=pytest.mark.xfail(reason="bug")),
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"{links}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_form()
    page.check_name_product()
    page.check_price_product()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_form()
    page.should_not_be_success_message()


# pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_form()
    page.should_be_disappeared_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# @pytest.mark.skip
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_basket_empty_text()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        f = faker.Faker()
        email = f.email()
        page = MainPage(self.browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.open()
        login_page.register_new_user(email, "123456789vlad123456789")
        time.sleep(3)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        print(link)
        page = ProductPage(self.browser, link)
        page.open()
        page.click_add_to_basket_form()
        page.check_name_product()
        page.check_price_product()