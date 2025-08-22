import logging
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.fuse_page import FusePage

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

class BaseClass:
    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        self.base_url = os.getenv("BASE_URL")
        self.login_path = os.getenv("LOGIN_PATH")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.login_page = LoginPage(self.page)
        self.fuse_page = FusePage(self.page)
