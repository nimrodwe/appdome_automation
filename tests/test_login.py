import allure
from playwright.sync_api import expect


@allure.epic("Login page")
@allure.feature("title - functionality")
@allure.story("Validating login functionality on fusion.appdome.com")
class TestLogin:

    @allure.epic("Login page")
    @allure.feature("Login test")
    @allure.story("Login with an already registered account")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, initialize):
        initialize.login_page.login(initialize.email, initialize.password)
        expect(initialize.login_page.login_welcome_text).to_be_visible()


