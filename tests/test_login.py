import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


LOGIN_URL = "https://admin.adraproductstudio.com/"
SUCCESS_URL_PART = "/candidates_home/qa-assessment"


def open_login_page(driver):

    driver.get(LOGIN_URL)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            LoginPage.USERNAME
        )
    )

    return LoginPage(driver)


def test_login_with_valid_credentials(driver):

    username = os.getenv("ADRA_TEST_USERNAME")
    password = os.getenv("ADRA_TEST_PASSWORD")

    assert username, (
        "ADRA_TEST_USERNAME environment variable is not set"
    )

    assert password, (
        "ADRA_TEST_PASSWORD environment variable is not set"
    )

    login_page = open_login_page(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)

    login_page.click_login()

    WebDriverWait(driver, 15).until(
        lambda d: SUCCESS_URL_PART in d.current_url
    )

    assert SUCCESS_URL_PART in driver.current_url


def test_login_with_invalid_credentials(driver):

    login_page = open_login_page(driver)

    login_page.enter_username("12345678")
    login_page.enter_password("123456")

    login_page.click_login()

    error_message = login_page.get_error_message()

    assert error_message == "User not found"


def test_login_with_empty_fields(driver):

    login_page = open_login_page(driver)

    login_page.click_login()

    # Application does not show a validation message.
    # Verify that login did not occur.
    assert driver.current_url == LOGIN_URL


def test_login_with_only_username(driver):

    login_page = open_login_page(driver)

    login_page.enter_username("12345678")

    login_page.click_login()

    # Login should not occur when password is empty.
    assert driver.current_url == LOGIN_URL


def test_login_with_only_password(driver):

    login_page = open_login_page(driver)

    login_page.enter_password("123456")

    login_page.click_login()

    # Login should not occur when username is empty.
    assert driver.current_url == LOGIN_URL