from playwright.sync_api import expect
import allure

@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate fuse page functionality")
class TestFuse:

    @allure.epic("Functionality")
    @allure.feature("App selection")
    @allure.story("Choose first app project from the apps container")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_app(self, initialize):
        initialize.login_page.login(initialize.email, initialize.password)
        initialize.fuse_page.click_first_app()
        expect(initialize.fuse_page.app_clicked_highlight).to_be_visible()

    @allure.epic("Functionality")
    @allure.feature("Build app")
    @allure.story("Build an app via ui")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_build_app(self, initialize):
        initialize.login_page.login(initialize.email, initialize.password)
        initialize.fuse_page.click_first_app()
        success = initialize.fuse_page.build_app()
        assert success, "Build app failed or button disabled."
        initialize.fuse_page.build_success.wait_for(state="visible", timeout=0)