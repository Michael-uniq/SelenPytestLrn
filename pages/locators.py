from selenium.webdriver.common.by import By

class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn")
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, ".btn-group .btn-inv")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    DISAPPEAR_OBJECT = (By.CSS_SELECTOR, '#messages .alertinner')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGES_AFTER_CLICK_ON_BASKET = (By.CSS_SELECTOR, '.fade strong')
    MESSAGE_NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.fade strong')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')

class BasketPageLocators():
    GOODS_IN_BASKET_STRING = (By.CSS_SELECTOR, '#content_inner .basket-title')
    GOODS_IN_BASKET_STRING_INVALID = (By.CSS_SELECTOR, '#cont_inner .basket-title')

    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    MESSAGE_EMPTY_BASKET_INVALID = (By.CSS_SELECTOR, '#content_inner pin')