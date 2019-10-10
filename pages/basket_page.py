from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_nothing_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET_STRING_INVALID), (
            'Goods have in basket, but must not'
        )

    def shoud_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), (
            'Message about empty basket is not find'
        )