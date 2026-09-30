import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def open_signup_page(driver):

    driver.get("https://admin.adraproductstudio.com/")

    login_page = LoginPage(driver)
    login_page.click_register_candidate()

    signup_page = SignupPage(driver)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            signup_page.FRESHER
        )
    )

    return signup_page


def generate_unique_test_data():

    timestamp = str(
        int(time.time())
    )

    phone = "9" + timestamp[-9:]

    email = (
        "qa_automation_"
        + timestamp
        + "@example.com"
    )

    return phone, email


def fill_required_signup_fields(
    signup_page,
    email,
    phone
):

    # =========================================================
    # Candidate Details
    # =========================================================

    signup_page.enter_full_name("Test User")
    signup_page.enter_age("23")
    signup_page.enter_phone(phone)
    signup_page.enter_email(email)
    signup_page.select_gender("Male")
    signup_page.enter_address("Coimbatore")

    # =========================================================
    # Family Details
    # =========================================================

    signup_page.enter_parent_name("Test Parent")
    signup_page.enter_parent_occupation("Business")
    signup_page.select_marital_status("Un Married")
    signup_page.enter_sibling_name("Test Sibling")
    signup_page.enter_cbe_address("Coimbatore")

    # =========================================================
    # Academic Details
    # =========================================================

    signup_page.enter_sslc_school(
        "ABC Higher Secondary School"
    )

    signup_page.enter_sslc_marks("85")

    signup_page.enter_hsc_school(
        "ABC Higher Secondary School"
    )

    signup_page.enter_hsc_marks("82")

    signup_page.enter_college(
        "ABC College"
    )

    signup_page.enter_qualification(
        "MCA"
    )

    signup_page.enter_cgpa("8.2")

    # =========================================================
    # Fresher / Experienced
    # =========================================================

    signup_page.select_fresher()

    # =========================================================
    # Role
    # =========================================================

    signup_page.select_role(
        "Automation_test_Campaign"
    )

    # =========================================================
    # Salary
    # =========================================================

    signup_page.enter_present_salary("0")

    signup_page.enter_expected_salary(
        "300000"
    )


def test_navigate_to_candidate_registration(driver):

    signup_page = open_signup_page(driver)

    assert (
        "/candidates_registration"
        in driver.current_url
    )


def test_fresher_hides_work_experience(driver):

    signup_page = open_signup_page(driver)

    signup_page.select_fresher()

    assert (
        signup_page.is_organization_visible()
        is False
    )


def test_experienced_shows_work_experience(driver):

    signup_page = open_signup_page(driver)

    signup_page.select_experienced()

    assert (
        signup_page.is_organization_visible()
        is True
    )


def test_signup_required_fields_validation(driver):

    signup_page = open_signup_page(driver)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            signup_page.CONTINUE_BUTTON
        )
    )

    signup_page.click_continue()

    assert (
        "/candidates_registration"
        in driver.current_url
    )

    messages = (
        signup_page.get_validation_messages()
    )

    expected_messages = [
        "Full Name required",
        "Age required",
        "Phone number required",
        "Email required",
        "Gender required",
        "Address required",
        "School Name required",
        "Marks/Percentage required",
        "College Name required",
        "Qualification required",
    ]

    for expected_message in expected_messages:

        assert expected_message in messages, (
            f"Expected validation message not found: "
            f"{expected_message}\n"
            f"Actual messages: {messages}"
        )


def test_phone_number_less_than_10_digits(driver):

    signup_page = open_signup_page(driver)

    # Generate a unique email so that
    # duplicate-data validation does not interfere.
    unused_phone, email = generate_unique_test_data()

    # Use 9 digits intentionally.
    invalid_phone = "987654321"

    fill_required_signup_fields(
        signup_page,
        email,
        invalid_phone
    )

    signup_page.click_continue()

    toast_message = (
        signup_page.get_toast_message()
    )

    assert (
        toast_message
        == "Mobile number should be 10 digit."
    )


def test_invalid_email_format(driver):

    signup_page = open_signup_page(driver)

    # Generate a fresh phone number.
    # This prevents the duplicate-data validation
    # from running before email-format validation.
    phone, unused_email = generate_unique_test_data()

    # Fill all required fields.
    # Email is intentionally invalid.
    fill_required_signup_fields(
        signup_page,
        "abc",
        phone
    )

    signup_page.click_continue()

    toast_message = (
        signup_page.get_toast_message()
    )

    assert (
        toast_message
        == "Please enter valid email address"
    )


def test_valid_candidate_registration(driver):

    signup_page = open_signup_page(driver)

    # Generate unique candidate data
    # for every test execution.
    phone, email = (
        generate_unique_test_data()
    )

    # Fill complete registration form.
    fill_required_signup_fields(
        signup_page,
        email,
        phone
    )

    # Submit registration.
    signup_page.click_continue()

    # =========================================================
    # Verify redirect to login page
    # =========================================================

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            LoginPage.USERNAME
        )
    )

    assert (
        "/candidates_registration"
        not in driver.current_url
    )

    # =========================================================
    # Verify username is populated
    # =========================================================

    login_page = LoginPage(driver)

    assert (
        login_page.get_username_value()
        == phone
    )

    # =========================================================
    # Verify password is populated
    # =========================================================

    assert (
        login_page.is_password_populated()
        is True
    )