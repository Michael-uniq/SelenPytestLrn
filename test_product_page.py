import time
import pytest
from .pages.product_page import ProductPage


xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, xlink)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_busket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_product_in_basket()
    page.should_be_equal_sum_in_basket_with_price()
