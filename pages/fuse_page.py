import logging
import allure
from pages.base_page import BasePage


class FusePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.apps_container = page.locator("app-app-row")
        self.app_clicked_highlight = page.locator(".ng-star-inserted.active.selected")
        # Locator for the Build My App button by classes, excluding 'disabled' for check later
        self.build_button = page.locator("app-button.split-btn.big-45.button.success")
        self.build_success = page.locator("div.title", has_text="Success!")

    def click_first_app(self):
        self.click(self.apps_container.nth(0))

    def build_app(self):
        classes = self.build_button.get_attribute("class")
        if "disabled" not in classes:
            self.click(self.build_button)
            logging.info("Clicked on Build My App button.")
            return True
        else:
            logging.info("Build My App button is disabled. Cannot click.")
            return False


