from selenium.webdriver.common.by import By

class BasePageLocators():

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    USER_ICON_INVALID = (By.CSS_SELECTOR, ".icon-user-inv")

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn")
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, ".btn-group .btn-inv")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, '#register_form .btn-lg')
    REGISTER_FORM_BUTTON_INVALID = (By.CSS_SELECTOR, '#register_form .btn-lg-inv')

    REGISTER_FORM_PASSWORD_INPUT_1 = (By.ID, 'id_registration-password1')
    REGISTER_FORM_PASSWORD_INPUT_2 = (By.ID, 'id_registration-password2')
    REGISTER_FORM_PASSWORD_INPUT_INVALID = (By.ID, 'id_registration-password-inv')

    REGISTER_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTER_FORM_EMAIL_INPUT_INVALID = (By.ID, 'id_registration-email-inv')

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
    GOODS_IN_BASKET_STRING_INVALID = (By.CSS_SELECTOR, '#content_inner p')

    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    MESSAGE_EMPTY_BASKET_INVALID = (By.CSS_SELECTOR, '#content_inner .basket-title')