import time

from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL


class PageRegister(BasePage):


    def __init__(self,driver):
        """设置页面实例属性（元素定位）"""
        super().__init__(driver)
        # 页面元素定位
        self.phone = (By.ID,"phone")
        self.pwd = (By.ID,"password")
        self.img_code = (By.ID,"verifycode")
        self.phone_click = (By.ID,"get_phone_code")
        self.phone_code = (By.ID,"phone_code")
        self.reg = (By.CLASS_NAME,"lg-btn")
        # 成功结果元素定位
        self.success_result =(By.CSS_SELECTOR, "div.reg-step-last > h1")
        # 失败结果元素定位 #reg_form > div.reg-title
        self.fail_result = (By.CSS_SELECTOR, "#reg_form > div.reg-title")

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/common/member/reg")
    def register(self, phone, pwd, img_code, phone_code):
        # 输入手机号
        self.base_input(self.phone, phone)
        # 输入密码
        self.base_input(self.pwd, pwd)
        # 输入图片验证码
        self.base_input(self.img_code, img_code)
        # 点击获取手机验证码
        self.base_click(self.phone_click)
        time.sleep(2)
        # 输入手机验证码
        self.base_input(self.phone_code, phone_code)
        # 点击注册
        self.base_click(self.reg)

    def get_success_result(self):
        """获取注册成功信息"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取注册失败信息"""
        return self.fd_element(self.fail_result).text