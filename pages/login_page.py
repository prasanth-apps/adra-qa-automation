from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (
        By.NAME,
        "Username"
    )

    PASSWORD = (
        By.NAME,
        "Password"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[title='Login']"
    )

    REGISTER_CANDIDATE = (
        By.CSS_SELECTOR,
        "a[href='/candidates_registration']"
    )

    ERROR_TOAST = (
        By.CSS_SELECTOR,
        "div[role='alert']"
    )

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        element.clear()
        element.send_keys(username)

    def get_username_value(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        return element.get_attribute("value")

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        element.clear()
        element.send_keys(password)

    def is_password_populated(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD)
        )
        value = element.get_attribute("value")
        return bool(value)

    def click_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        element.click()

    def click_register_candidate(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGISTER_CANDIDATE)
        )
        element.click()

    def get_error_message(self):
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_TOAST)
        )
        return error.text.strip()