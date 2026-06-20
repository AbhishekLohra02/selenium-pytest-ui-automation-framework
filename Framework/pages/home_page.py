from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    name_feild = (By.XPATH, "//label[text()='Name']")
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.NAME, "email")
    password_input = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    student_radio = (By.ID, "inlineRadio1")
    employed_radio = (By.ID, "inlineRadio2")
    birthday_input = (By.NAME, "bday")
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")
    success_message = (By.CSS_SELECTOR, ".alert-success")
    name_error_message = (By.CSS_SELECTOR, ".alert-danger")
    shop_link = (By.LINK_TEXT, "Shop")

    def enter_name(self, name):
        self.enter_text(self.name_input, name)

    def enter_email(self, email):
        self.enter_text(self.email_input, email)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_checkbox(self):
        self.click_element(self.checkbox)

    def select_gender(self, gender):
        self.select_dropdown_by_text(self.gender_dropdown, gender)

    def click_student_radio(self):
        self.click_element(self.student_radio)

    def click_employed_radio(self):
        self.click_element(self.employed_radio)

    def enter_birthday(self, birthday):
        self.enter_text(self.birthday_input, birthday)

    def fill_practice_form(self, name, email, password, gender, birthday):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_checkbox()
        self.select_gender(gender)
        self.click_student_radio()
        self.enter_birthday(birthday)

    def click_submit(self):
        self.click_element(self.submit_button)

    def get_success_message(self):
        return self.get_text(self.success_message)

    def get_name_error_message(self):
        return self.get_text(self.name_error_message)

    def click_shop_link(self):
        self.click_element(self.shop_link)
