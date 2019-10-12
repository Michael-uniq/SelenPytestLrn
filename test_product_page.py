import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

home_link = 'http://selenium1py.pythonanywhere.com/'
link_of_product = f'{home_link}catalogue/the-shellcoders-handbook_209/'
login_link = f'{home_link}accounts/login/'
mask = f'{home_link}catalogue/coders-at-work_207/?promo=offer'
xfile = 7
links_for_promo = [mask + str(i) for i in range(10) if i != xfile]
xfail_link = pytest.param(mask + str(xfile), marks=pytest.mark.xfail(reason="On page a not critical mistake"))
links_for_promo.insert(xfile, xfail_link)

@pytest.mark.need_review
@pytest.mark.parametrize('param_link', links_for_promo)
def test_guest_can_add_product_to_basket(browser, param_link):
    page = ProductPage(browser, param_link)
    page.open()
    page.should_be_button_add_to_busket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_product_in_basket()
    page.should_be_equal_sum_in_basket_with_price()

@pytest.mark.skip
def test_disappear_and_not_present(browser):
    link_product_promo = f'{link_of_product}?promo=newYear'
    page = ProductPage(browser, link_product_promo)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.should_object_is_disappear()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.add_product_to_basket()
    page.should_object_is_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.go_to_login_page()
    page.should_be_current_page_is_login()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.shoud_be_message_about_empty_basket()
    basket_page.should_be_nothing_in_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        email = f'{time.time()}User@foo.bar'
        password = email[:10]
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, link_of_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, link_of_product)
        page.open()
        page.should_be_button_add_to_busket()
        page.add_product_to_basket()
        page.should_be_product_in_basket()
        page.should_be_equal_sum_in_basket_with_price()