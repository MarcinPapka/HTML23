import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.login_page import LoginPage, ProjectPage


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("administrator@testarena.pl", "sumXQQ72$L")
    yield browser
    browser.quit()


def test_full_home_work_exercise(browser):
    assert browser.find_element(By.CSS_SELECTOR, '[title=Wyloguj]').is_displayed() is True
    project_page = ProjectPage(browser)
    project_page.create_project("4testersMP", "MP4testers")


def test_full_home_work_exercise2(browser):
    # Check if the logout button is displayed
    assert browser.find_element(By.CSS_SELECTOR, '[title=Wyloguj]').is_displayed() is True

    # Click the tools button
    browser.find_element(By.CSS_SELECTOR, ".icon_tools ").click()
    browser.find_element(By.CSS_SELECTOR, 'a.button_link').click()

    # Go to the projects page and search for the project
    browser.find_element(By.CSS_SELECTOR, '.icon_puzzle_alt').click()
    browser.find_element(By.CSS_SELECTOR, '#search').send_keys('4testersMP')
    browser.find_element(By.CSS_SELECTOR, '#j_searchButton').click()

    # Check if the project is displayed in the results
    prefix = browser.find_element(By.CSS_SELECTOR, '.t_number')
    assert prefix.is_displayed() is True
    assert prefix.text == "MP4tes"

    # Check if the project name is displayed correctly
    name = browser.find_element(By.LINK_TEXT, '4testersMP')
    assert name.is_displayed() is True
    assert name.text == "4testersMP"
