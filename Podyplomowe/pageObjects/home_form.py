from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.faker = Faker('pl_PL')
        self.X_POP_UP = (By.ID, "popup-widget307423-close-icon")
        self.FIRST_NAME = (By.XPATH, "//input[@data-aid='First Name']")
        self.LAST_NAME = (By.XPATH, "//input[@data-aid='Last Name']")
        self.EMAIL_ADDRESS = (By.XPATH, "//input[@data-aid='CONTACT_FORM_EMAIL']")
        self.PHONE_NUMBER = (By.XPATH, "//input[@data-aid='By entering a Phone Number you agree to our SMS Terms of Service']")
        self.MESSAGE_FIELD = (By.XPATH, "//textarea[@data-aid='CONTACT_FORM_MESSAGE']")
        self.SUBMIT_BUTTON = (By.XPATH, "//button[@data-aid='CONTACT_SUBMIT_BUTTON_REND']")
        self.CONTACT_EMAIL_ERR_REND = (By.XPATH, "//p[@data-aid='CONTACT_EMAIL_ERR_REND']")
        self.action = ActionChains(driver)
        self.THANK_YOU_CONTACT = (By.XPATH, "//div[@data-aid='CONTACT_FORM_SUBMIT_SUCCESS_MESSAGE']/p")
        self.THANK_YOU_TITLE = By.XPATH, "//h2[@data-aid='CONTACT_SECTION_TITLE_REND']/span"
        self.THANK_YOU_HEADER = (By.XPATH, "//div[@data-aid='CONTACT_SECTION_INFO_REND']/h4")
        self.THANK_YOU_MSG = (By.XPATH, "//div[@data-aid='CONTACT_INTRO_DESC_REND']/p")
        self.THANK_YOU_HEADER_ADDRESS = (By.XPATH, "//div[@data-aid='CONTACT_SECTION_DETAILS_REND']/h4")
        self.THANK_YOU_ADDRESS = (By.XPATH, "//div[@data-aid='CONTACT_SECTION_DETAILS_REND']/p[@data-aid='CONTACT_INFO_ADDRESS_REND']")
        self.THANK_YOU_PHONE_EMAIL = (By.XPATH, "//div[@data-aid='CONTACT_SECTION_DETAILS_REND']/p[2]")
        self.THANK_YOU_HEADER_HOURS = (By.XPATH, "//h4[@data-aid='CONTACT_HOURS_TITLE_REND']")
        self.THANK_YOU_CONTACT_HOURS = (By.XPATH, "//div[@data-aid='CONTACT_HOURS_CUST_MSG_REND']//span")

    def close_pop_up(self):
        self.driver.find_element(*self.X_POP_UP).click()

    def move_to_element(self, element):
        element = self.driver.find_element(*element)
        self.action.move_to_element(element).perform()

    def fill_contact_us_first_name (self):
        first_name = self.faker.first_name()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def fill_contact_us_last_name (self):
        last_name = self.faker.last_name()
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def fill_contact_us_email (self):
        email = self.faker.email()
        self.driver.find_element(*self.EMAIL_ADDRESS).send_keys(email)

    def fill_contact_us_wrong_email(self, wrong_email):
        self.driver.find_element(*self.EMAIL_ADDRESS).send_keys(wrong_email)

    def fill_contact_us_phone_number (self):
        phone_number = self.faker.phone_number()
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)

    def fill_contact_us_message (self):
        message = self.faker.text(max_nb_chars=200)
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(message)

    def click_submit (self):
        time.sleep(5)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def fill_entire_form(self):
        self.fill_contact_us_first_name()
        self.fill_contact_us_last_name()
        self.fill_contact_us_email()
        self.fill_contact_us_phone_number()
        self.fill_contact_us_message()
        self.click_submit()

    def catch_error_text_contact_us_for_email(self):
        time.sleep(3)
        error_message = self.driver.find_element(*self.CONTACT_EMAIL_ERR_REND).text
        return error_message

#Thank you page after contact us
    def catch_thank_you_title(self):
        title = self.driver.find_element(*self.THANK_YOU_TITLE).text
        return title

    def catch_thank_you_contuct_test(self):
        time.sleep(5)
        thank_you_msg = self.driver.find_element(*self.THANK_YOU_CONTACT).text
        return thank_you_msg

    def catch_thank_you_header(self):
        header_msg = self.driver.find_element(*self.THANK_YOU_HEADER).text
        return header_msg

    def catch_thank_you_text_message(self):
        text_msg = self.driver.find_element(*self.THANK_YOU_MSG).text
        return text_msg

    def catch_thank_you_header_address(self):
        header_address = self.driver.find_element(*self.THANK_YOU_HEADER_ADDRESS).text
        return header_address

    def catch_thank_you_address_message(self):
        address_msg = self.driver.find_element(*self.THANK_YOU_ADDRESS).text
        return address_msg

    def catch_thank_you_phone_and_email(self):
        phone_email_msg = self.driver.find_element(*self.THANK_YOU_PHONE_EMAIL).text
        return phone_email_msg

    def catch_thank_you_hours_header(self):
        header_hours = self.driver.find_element(*self.THANK_YOU_HEADER_HOURS).text
        return header_hours

    def get_contact_hours(self):
        spans = self.driver.find_elements(*self.THANK_YOU_CONTACT_HOURS)
        return [s.text for s in spans]