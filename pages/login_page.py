import logging
import allure
from pages.base_page import BasePage


# login page functions

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("login to the system")
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = logging.getLogger(__name__)
        self.work_email_field = page.locator('input[name="email"]')
        self.password_field = page.locator('input[type="password"][placeholder="Enter a Password"]')
        self.login_button = page.locator('#sign-in-password')
        self.login_welcome_text = page.locator('div.greeting')

    def login(self, work_email: str, password: str):
        self.logger.info(f"Logging in with user: {work_email}")
        self.fill(self.work_email_field, work_email)
        self.fill(self.password_field, password)
        self.click(self.login_button)
        self.logger.info("Login submitted successfully.")