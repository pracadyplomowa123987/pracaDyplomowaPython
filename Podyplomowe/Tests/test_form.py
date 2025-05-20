from pageObjects.home_form import HomePage
import time


ERROR_MESSAGE = "Please enter a valid email address."
THANK_YOU_TITLE = "Contact Us"
THANK_YOU_MAIN_MSG = "Thank you for your inquiry! We will get back to you within 48 Years."
THANK_YOU_HEADER_TITLE = "Better yet, see us in person!"
THANK_YOU_TEXT_MSG = "CandyMapper is a completely fictional app, so feel free to visit during normal business hours. And thank you for listening to the Test Guild Halloween Podcast Episodes with Joe Colantonio!"
THANK_YOU_HEADER_ADDRESS = "CandyMapper: A Sandbox for SDETs"
THANK_YOU_ADDRESS = "Winchester Tavern, 221B Monson Road, New Cross Gate, London SE14 Odd"
THANK_YOU_PHONE = "+44 20 7946 0Boo\nadmin@Candymapper.com"
THANK_YOU_HOURS_HEADER = "Hours"

# 1. Test - walidacja formularza kontaktowego przy próbie wysłania pustego formularza.
def test_submit_without_filling(driver):
    print("TS01_Walidacja formularza kontaktowego przy próbie wysłania pustego formularza.")
    home_page = HomePage(driver)
    driver.get("https://candymapper.com/")
    print("Otwarta strona główna")
    home_page.close_pop_up()
    print("Zamknięto popup")
    home_page.move_to_element(home_page.SUBMIT_BUTTON)
    print("Scroll do formularza (submit button)")
    home_page.click_submit()
    print("Kliknięto Submit bez uzupełnienia formularza")
    error_message = home_page.catch_error_text_contact_us_for_email()
    assert error_message == ERROR_MESSAGE
    print(f"Walidacja pod polem Email się pokazała o treści: {ERROR_MESSAGE}")

# 2. Test - walidacja formularza kontaktowego przy próbie wysłania formularza bez obowiązkowego pola Email.
def test_fill_form_without_email(driver):
    print("TA02_Walidacja formularza kontaktowego przy próbie wysłania formularza bez obowiązkowego pola Email.")
    home_page = HomePage(driver)
    driver.get("https://candymapper.com/")
    print("Otwarta strona główna")
    home_page.close_pop_up()
    print("Zamknięto popup")
    home_page.move_to_element(home_page.SUBMIT_BUTTON)
    print("Scroll do formularza (submit button)")
    home_page.fill_contact_us_first_name()
    home_page.fill_contact_us_last_name()
    home_page.fill_contact_us_phone_number()
    home_page.fill_contact_us_message()
    print("Uzupełniono pola:\n-First Name,\n-Last Name,\n-Phone Number,\n-Message")
    home_page.click_submit()
    print("Kliknięto Submit bez uzupełnienia pola Email")
    error_message = home_page.catch_error_text_contact_us_for_email()
    assert error_message == ERROR_MESSAGE
    print(f"Walidacja pod polem Email się pokazała o treści: {ERROR_MESSAGE}")

# 3. Test - walidacja formularza kontaktowego przy próbie wysłania formularza z niepoprawnym Email.
def test_fill_form_with_wrong_email(driver):
    print("TA03_Walidacja formularza kontaktowego przy próbie wysłania formularza z niepoprawnym Email.")
    home_page = HomePage(driver)
    driver.get("https://candymapper.com/")
    print("Otwarta strona główna")
    home_page.close_pop_up()
    print("Zamknięto popup")
    home_page.move_to_element(home_page.SUBMIT_BUTTON)
    print("Scroll do formularza (submit button)")
    home_page.fill_contact_us_first_name()
    home_page.fill_contact_us_last_name()
    home_page.fill_contact_us_wrong_email("alicja.com")
    home_page.fill_contact_us_phone_number()
    home_page.fill_contact_us_message()
    print("Uzupełniono pola:\n-First Name,\n-Last Name,\n-Phone Number,\nEmail - z błędnym formatem email 'alicja.com'\n-Message")
    home_page.click_submit()
    print("Kliknięto Submit")
    error_message = home_page.catch_error_text_contact_us_for_email()
    assert error_message == ERROR_MESSAGE
    print(f"Walidacja pod polem Email się pokazała o treści: {ERROR_MESSAGE}")

#4. Test - weryfikacja poprawnie uzupełnionego formularza
def test_fill_form_correct(driver):
    print("TA04_Weryfikacja poprawnie uzupełnionego formularza")
    home_page = HomePage(driver)
    driver.get("https://candymapper.com/")
    print("Otwarta strona główna")
    home_page.close_pop_up()
    print("Zamknięto popup")
    home_page.move_to_element(home_page.SUBMIT_BUTTON)
    print("Scroll do formularza (submit button)")
    home_page.fill_contact_us_first_name()
    home_page.fill_contact_us_last_name()
    home_page.fill_contact_us_email()
    home_page.fill_contact_us_phone_number()
    home_page.fill_contact_us_message()
    print("Uzupełniono pola:\n-First Name,\n-Last Name,\n-Phone Number,\n-Email\n-Message")
    home_page.click_submit()
    print("Kliknięto Submit")
    confirmation = home_page.catch_thank_you_contuct_test()
    assert confirmation == THANK_YOU_MAIN_MSG
    print("Formularz poprawnie wysłany. Pokazała się Thank you page")

#5. Test - Thank you page weryfikacja tekstu
def test_thank_you_page_test_verification(driver):
    print("TA04_Weryfikacja poprawnie uzupełnionego formularza")
    home_page = HomePage(driver)
    driver.get("https://candymapper.com/")
    print("Otwarta strona główna")
    home_page.close_pop_up()
    print("Zamknięto popup")
    home_page.move_to_element(home_page.SUBMIT_BUTTON)
    print("Scroll do formularza (submit button)")
    home_page.fill_contact_us_email()
    print(f"Uzupełniono pole obowiązakowe email.")
    home_page.click_submit()
    print("Kliknięto Submit")
    time.sleep(5)
    title = home_page.catch_thank_you_title()
    header = home_page.catch_thank_you_header()
    text_msg = home_page.catch_thank_you_text_message()
    header_address = home_page.catch_thank_you_header_address()
    address_msg = home_page.catch_thank_you_address_message()
    phone_number = home_page.catch_thank_you_phone_and_email()
    hours_header = home_page.catch_thank_you_hours_header()

    assert title == THANK_YOU_TITLE
    assert header == THANK_YOU_HEADER_TITLE
    assert text_msg == THANK_YOU_TEXT_MSG
    assert header_address == THANK_YOU_HEADER_ADDRESS
    assert address_msg == THANK_YOU_ADDRESS
    assert phone_number == THANK_YOU_PHONE
    assert hours_header == THANK_YOU_HOURS_HEADER

    expected_hours = [
        "Monday - Friday: Closed",
        "Saturday: By appointment only",
        "Sunday: Rarely open.\nHalloween: 24-Hour fully staffed support line."
    ]

    actual_hours = home_page.get_contact_hours()

    for expected in expected_hours:
        assert expected in actual_hours, f"Nie znaleziono: {expected}"

    print(" Weryfikacja tekstów na stronie Thank you")