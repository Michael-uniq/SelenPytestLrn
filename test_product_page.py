import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links_for_promo = [mask + str(i) for i in range(10) if i != xfile]
xfail_link = pytest.param(mask + str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links_for_promo.insert(xfile, xfail_link)
link_of_product = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

@pytest.mark.skip
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
    time.sleep(1)
    page.should_not_be_success_message()
    page.should_object_is_disappear()




@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link_of_product)
    page.open()
    page.add_product_to_basket()
    time.sleep(2)
    page.should_not_be_success_message()

@pytest.mark.skip       #включить потом
def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link_of_product)
    page.open()
    time.sleep(2)
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, link_of_product)
    page.open()
    page.add_product_to_basket()
    time.sleep(1)
    page.should_object_is_disappear()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_of_product)
    page.open()
    page.go_to_login_page()
    page.should_be_current_page_is_login()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    page = ProductPage(browser, link_of_product)  # инициализируем
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    time.sleep(2)
    basket_page.shoud_be_message_about_empty_basket()
    basket_page.should_be_nothing_in_basket()

@pytest.mark.testing_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, login_link)
        page.open()
        email = f'{time.time()}User@foo.bar'
        password = email[:10]
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    def test_user_cant_see_success_message(self):
        """
        Открываем страницу товара
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(self.browser, link_of_product)
        page.open()
        time.sleep(2)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, link_of_product)
        page.open()
        page.should_be_button_add_to_busket()
        page.add_product_to_basket()
        time.sleep(1)
        page.should_be_product_in_basket()
        page.should_be_equal_sum_in_basket_with_price()