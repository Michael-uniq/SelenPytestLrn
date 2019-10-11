from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_busket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET), 'Not find button for add to basket'

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        basket_button.click()

    def should_be_product_in_basket(self):
        message_product = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT_IN_BASKET).text
        product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert product == message_product, f'Message must be = "{message_product}", not "{product}"'

    def should_be_equal_sum_in_basket_with_price(self):
        basket_price = self.browser.find_elements(*ProductPageLocators.MESSAGES_AFTER_CLICK_ON_BASKET)[2].text
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price in basket_price, f'Basket have another price: {basket_price}, then price of product: {price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_object_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPEAR_OBJECT), \
            "Object is presented, but should be disappear"
