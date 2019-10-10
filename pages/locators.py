from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

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
