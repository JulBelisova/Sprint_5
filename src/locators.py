from selenium.webdriver.common.by import By

class Locators:
    #плейсхолдер "Имя":
    NAME = (By.XPATH, "(.//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'name'])[1]")
    #плейсхолдер "Email":
    EMAIL = (By.XPATH, "(.//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'name'])[2]")
    #плейсхолдер "Пароль":
    PASSWORD = (By.XPATH, ".//form[@class ='Auth_form__3qKeq mb-20']//input[@name = 'Пароль']")
    #кнопка "зарегистрироваться":
    REGISTER_BUTTON = (By.XPATH, ".//form[@class ='Auth_form__3qKeq mb-20']//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    #заголовок "войти" на странице входа:
    TEXT_ENTER = (By.XPATH, ".//main//h2[text()='Вход']")
    #надпись "Некорректный пароль" на странице ругистрации:
    INCORRECT_PASSWORD = (By.XPATH, "(.//form[@class ='Auth_form__3qKeq mb-20']//p[@class = 'input__error text_type_main-default'])")