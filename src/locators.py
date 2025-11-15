from selenium.webdriver.common.by import By


class Locators:
    # плейсхолдер "Имя":
    NAME = (
        By.XPATH,
        "(.//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'name'])[1]",
    )
    # плейсхолдер "Email":
    EMAIL = (
        By.XPATH,
        "(.//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'name'])[2]",
    )
    # плейсхолдер "Пароль":
    PASSWORD = (
        By.XPATH,
        ".//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'Пароль']",
    )
    # кнопка "зарегистрироваться":
    REGISTER_BUTTON = (
        By.XPATH,
        ".//form[@class ='Auth_form__3qKeq mb-20']//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']",
    )
    # заголовок "войти" на странице входа:
    TEXT_ENTER = (By.XPATH, ".//main//h2[text()='Вход']")
    # надпись "Некорректный пароль" на странице регистрации:
    INCORRECT_PASSWORD = (
        By.XPATH,
        ".//form[@class ='Auth_form__3qKeq mb-20']//p[@class = 'input__error text_type_main-default']",
    )
    # Кнопка "Войти" на главной странице:
    BUTTON_SIGN_IN_MAIN = (
        By.XPATH,
        ".//main[@class ='App_componentContainer__2JC2W']//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']",
    )
    # Кнопка "личный кабинет" на главной странице:
    BUTTON_MY_ACCOUNT = (
        By.XPATH,
        ".//nav[@class = 'AppHeader_header__nav__g5hnF']//p[@class ='AppHeader_header__linkText__3q_va ml-2'][text()='Личный Кабинет']",
    )
    # Кнопка "Войти" на странице регистрации:
    BUTTON_SIGN_IN_FROM_REGISTRATION = (
        By.XPATH,
        ".//p[@class = 'undefined text text_type_main-default text_color_inactive mb-4']//a[@class = 'Auth_link__1fOlj']",
    )
    # Кнопка "Войти" на странице восстановления пароля:
    BUTTON_SIGN_IN_FROM_PASSWORD_RECOVERY = (
        By.XPATH,
        ".//p[@class ='undefined text text_type_main-default text_color_inactive mb-4']//a[@class ='Auth_link__1fOlj']",
    )
    # Кнопка "Конструктор":
    BUILDER = (
        By.XPATH,
        ".//p[@class = 'AppHeader_header__linkText__3q_va ml-2'][text()='Конструктор']",
    )
    # Логотип:
    LOGO = (By.XPATH, ".//div[contains(@class, 'header__logo')]//a")
    # переход на Соусы:
    SAUSE = (
        By.XPATH,
        ".//span[@class = 'text text_type_main-default'][text()='Соусы']",
    )
    # переход на Начинки:
    FILLING = (
        By.XPATH,
        ".//span[@class = 'text text_type_main-default'][text()='Начинки']",
    )
    # переход на Булки:
    BUN = (By.XPATH, ".//span[@class = 'text text_type_main-default'][text()='Булки']")
    # Текст"Начинки" на странице конструктора(для проверки перехода на данный раздел):
    TEXT_FILLING = (
        By.XPATH,
        ".//h2[@class ='text text_type_main-medium mb-6 mt-10'][text()='Начинки']",
    )
    # Выход
    LOG_OUT = (
        By.XPATH,
        ".//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive'][text()='Выход']",
    )
    # Оформить заказ(для проверки входа):
    ORDER = (
        By.XPATH,
        ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg'][text()='Оформить заказ']",
    )
