from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    # =========================================================
    # Candidate Details
    # =========================================================

    FULL_NAME = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Full Name')]/following-sibling::input"
    )

    AGE = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Age')]/following-sibling::input"
    )

    PHONE = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Phone Number')]/following-sibling::input"
    )

    EMAIL = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Email')]/following-sibling::input"
    )

    GENDER = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Gender')]/following-sibling::select"
    )

    PHOTO_UPLOAD = (
        By.ID,
        "file_upload"
    )

    ADDRESS = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Address')]/following-sibling::textarea"
    )

    # =========================================================
    # Family Details
    # =========================================================

    PARENT_NAME = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Parent name')]/following-sibling::input"
    )

    PARENT_OCCUPATION = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Parent occupation')]/following-sibling::input"
    )

    MARITAL_STATUS = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Marital status')]/following-sibling::select"
    )

    SIBLING_NAME = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Brother / Sister name')]/following-sibling::input"
    )

    CBE_ADDRESS = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Address (Cbe if Any)')]/following-sibling::input"
    )

    # =========================================================
    # Academic Details
    # =========================================================

    SSLC_SCHOOL = (
        By.XPATH,
        "//label[contains(normalize-space(), 'School Name (SSLC)')]/following-sibling::input"
    )

    SSLC_MARKS = (
        By.XPATH,
        "//label[contains(normalize-space(), 'School Name (SSLC)')]/parent::div/following-sibling::div[1]//input"
    )

    HSC_SCHOOL = (
        By.XPATH,
        "//label[contains(normalize-space(), 'School Name (HSC)')]/following-sibling::input"
    )

    HSC_MARKS = (
        By.XPATH,
        "//label[contains(normalize-space(), 'School Name (HSC)')]/parent::div/following-sibling::div[1]//input"
    )

    COLLEGE = (
        By.XPATH,
        "//label[contains(normalize-space(), 'College')]/following-sibling::input"
    )

    QUALIFICATION = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Qualification')]/following-sibling::input"
    )

    CGPA = (
        By.XPATH,
        "//label[contains(normalize-space(), 'CGPA/Percentage')]/following-sibling::input"
    )

    # =========================================================
    # Fresher / Experienced
    # =========================================================

    FRESHER = (
        By.ID,
        "Fresher"
    )

    EXPERIENCED = (
        By.ID,
        "Experienced"
    )

    # =========================================================
    # Role
    # =========================================================

    ROLE = (
        By.XPATH,
        "//h5[normalize-space()='Role']/following::select[1]"
    )

    # =========================================================
    # Work Experience
    # =========================================================

    ORGANIZATION = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Organization name')]/following-sibling::input"
    )

    DESIGNATION = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Desigination')]/following-sibling::input"
    )

    YEARS_EXPERIENCE = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Years of Experience')]/following-sibling::select"
    )

    # =========================================================
    # Salary
    # =========================================================

    PRESENT_SALARY = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Present Salary')]/following-sibling::input"
    )

    EXPECTED_SALARY = (
        By.XPATH,
        "//label[contains(normalize-space(), 'Expected Salary')]/following-sibling::input"
    )

    # =========================================================
    # Remarks
    # =========================================================

    REMARKS = (
        By.XPATH,
        "//label[normalize-space()='Write here']/following-sibling::textarea"
    )

    # =========================================================
    # Continue
    # =========================================================

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Continue']"
    )

    # =========================================================
    # Validation Messages
    # =========================================================

    VALIDATION_MESSAGES = (
        By.CSS_SELECTOR,
        ".text-danger"
    )

    # =========================================================
    # Toast
    # =========================================================

    TOAST_MESSAGE = (
        By.CSS_SELECTOR,
        "div[role='alert']"
    )

    # =========================================================
    # Constructor
    # =========================================================

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Generic Methods
    # =========================================================

    def enter_text(self, locator, value):

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(value)

    def select_option(self, locator, visible_text):

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        Select(element).select_by_visible_text(visible_text)

    # =========================================================
    # Candidate Details
    # =========================================================

    def enter_full_name(self, value):
        self.enter_text(self.FULL_NAME, value)

    def enter_age(self, value):
        self.enter_text(self.AGE, value)

    def enter_phone(self, value):
        self.enter_text(self.PHONE, value)

    def enter_email(self, value):
        self.enter_text(self.EMAIL, value)

    def select_gender(self, value):
        self.select_option(self.GENDER, value)

    def upload_photo(self, file_path):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHOTO_UPLOAD)
        )

        element.send_keys(file_path)

    def enter_address(self, value):
        self.enter_text(self.ADDRESS, value)

    # =========================================================
    # Family Details
    # =========================================================

    def enter_parent_name(self, value):
        self.enter_text(self.PARENT_NAME, value)

    def enter_parent_occupation(self, value):
        self.enter_text(self.PARENT_OCCUPATION, value)

    def select_marital_status(self, value):
        self.select_option(self.MARITAL_STATUS, value)

    def enter_sibling_name(self, value):
        self.enter_text(self.SIBLING_NAME, value)

    def enter_cbe_address(self, value):
        self.enter_text(self.CBE_ADDRESS, value)

    # =========================================================
    # Academic Details
    # =========================================================

    def enter_sslc_school(self, value):
        self.enter_text(self.SSLC_SCHOOL, value)

    def enter_sslc_marks(self, value):
        self.enter_text(self.SSLC_MARKS, value)

    def enter_hsc_school(self, value):
        self.enter_text(self.HSC_SCHOOL, value)

    def enter_hsc_marks(self, value):
        self.enter_text(self.HSC_MARKS, value)

    def enter_college(self, value):
        self.enter_text(self.COLLEGE, value)

    def enter_qualification(self, value):
        self.enter_text(self.QUALIFICATION, value)

    def enter_cgpa(self, value):
        self.enter_text(self.CGPA, value)

    # =========================================================
    # Fresher / Experienced
    # =========================================================

    def select_fresher(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FRESHER)
        )

        element.click()

    def select_experienced(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.EXPERIENCED)
        )

        element.click()

    def is_organization_visible(self):

        return self.driver.find_element(
            *self.ORGANIZATION
        ).is_displayed()

    # =========================================================
    # Role
    # =========================================================

    def select_role(self, value):

        self.select_option(
            self.ROLE,
            value
        )

    # =========================================================
    # Work Experience
    # =========================================================

    def enter_organization(self, value):
        self.enter_text(self.ORGANIZATION, value)

    def enter_designation(self, value):
        self.enter_text(self.DESIGNATION, value)

    def select_years_experience(self, value):
        self.select_option(
            self.YEARS_EXPERIENCE,
            value
        )

    # =========================================================
    # Salary
    # =========================================================

    def enter_present_salary(self, value):
        self.enter_text(self.PRESENT_SALARY, value)

    def enter_expected_salary(self, value):
        self.enter_text(self.EXPECTED_SALARY, value)

    # =========================================================
    # Remarks
    # =========================================================

    def enter_remarks(self, value):
        self.enter_text(self.REMARKS, value)

    # =========================================================
    # Validation
    # =========================================================

    def get_validation_messages(self):

        elements = self.driver.find_elements(
            *self.VALIDATION_MESSAGES
        )

        messages = []

        for element in elements:

            text = element.text.strip()

            if text:
                messages.append(text)

        return messages

    # =========================================================
    # Toast
    # =========================================================

    def get_toast_message(self):

        toast = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.TOAST_MESSAGE
            )
        )

        return toast.text.strip()

    # =========================================================
    # Continue
    # =========================================================

    def click_continue(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        element.click()