import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin
from page.page_register import PageRegister
from page.page_open_account import PageOpenAccount
from page.page_credit_application import PageCreditApplication
from page.page_back_login import PageBackLogin
from page.page_credit_review import PageCreditReview

# ... existing code ...

@pytest.fixture()
def browser():
    """浏览器驱动fixture"""
    path = r"D:\AutoTestLearning\AutoTest\.venv\Scripts\chromedriver.exe"
    ser = Service(executable_path=path)
    driver = webdriver.Chrome(service=ser)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def a_login(browser):
    """登录页面对象"""
    page_login = PageLogin(browser)
    page_login.open_url()
    return page_login


@pytest.fixture()
def credit_application(a_login):
    """额度申请前置：登录后返回driver"""
    a_login.login("16666458455", "abc123")
    return a_login.driver


@pytest.fixture()
def register_page(browser):
    """注册页面对象"""
    page_register = PageRegister(browser)
    page_register.open_url()
    return page_register


@pytest.fixture()
def open_account_page(browser):
    """开户页面对象：先登录"""
    page_login = PageLogin(browser)
    page_login.open_url()
    page_login.login("13800002007", "Aa123456")
    page_open_account = PageOpenAccount(browser)
    return page_open_account


@pytest.fixture()
def back_login_page(browser):
    """后台登录页面对象"""
    page_back_login = PageBackLogin(browser)
    page_back_login.open_url()
    return page_back_login


@pytest.fixture()
def credit_review_page(back_login_page):
    """额度审核页面对象：后台登录后进入菜单"""
    back_login_page.back_login("admin", "HM_2025_test", "8888")
    page_credit_review = PageCreditReview(back_login_page.driver)
    page_credit_review.menu_manager()
    page_credit_review.search_record("13800001001")
    page_credit_review.select_record()
    return page_credit_review

@pytest.fixture()
def loan_page(a_login):
    """借款页面对象：登录后返回driver"""
    a_login.login("16666458455", "abc123")
    return a_login.driver
