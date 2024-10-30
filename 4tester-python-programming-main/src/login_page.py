from datetime import time

from selenium.webdriver.common.by import By


class LoginPage:
    URL = 'http://demo.testarena.pl/zaloguj'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, login, password):
        self.browser.find_element(By.CSS_SELECTOR, "#email").send_keys(login)
        self.browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#login").click()


class ProjectPage:
    def __init__(self, browser):
        self.browser = browser

    def create_project(self, project_name, project_prefix):
        self.browser.find_element(By.CSS_SELECTOR, ".icon_tools").click()
        self.browser.find_element(By.CSS_SELECTOR, 'a.button_link').click()
        self.browser.find_element(By.CSS_SELECTOR, '#name').send_keys(project_name)
        self.browser.find_element(By.CSS_SELECTOR, '#prefix').send_keys(project_prefix)
        self.browser.find_element(By.CSS_SELECTOR, '#save').click()

    def search_project(self, project_name):
        self.browser.find_element(By.CSS_SELECTOR, '.icon_puzzle_alt').click()
        self.browser.find_element(By.CSS_SELECTOR, '#search').send_keys(project_name)
        self.browser.find_element(By.CSS_SELECTOR, '#j_searchButton').click()

    def verify_project_exists(self, project_prefix):
        prefix = self.browser.find_element(By.CSS_SELECTOR, '.t_number')
        assert prefix.is_displayed() is True
        assert prefix.text == project_prefix

