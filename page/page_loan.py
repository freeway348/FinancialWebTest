import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base import BasePage


class PageLoan(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 找到借款页面
        self.loan_choose = (By.CSS_SELECTOR, "li.ui-nav-item:nth-child(3) > a:nth-child(1)")
        self.loan = (By.LINK_TEXT, "个人借款")
        # 选中信用标进行借款
        self.loan_credit = (By.XPATH, "/html/body/div[2]/div/ul/li[1]/dl/dd[5]/a[contains(text(),'立即借款')]")
        # 填写相关借款表单信息
        self.loan_title = (By.CSS_SELECTOR, "[ng-model='borrow_loan.name'][name='name']")
        self.loan_use = (By.CSS_SELECTOR, "[ng-model='borrow_loan.use'][name='use']")
        self.loan_amount = (By.CSS_SELECTOR, "[ng-model='borrow_loan.amount'][name='amount']")
        self.loan_period = (By.CSS_SELECTOR, "[ng-model='borrow_loan.apr'][name='apr']") # 年利率
        self.loan_repay = (By.CSS_SELECTOR, ".bm-select.ng-pristine.ng-valid")
        self.loan_repay_time = (By.CSS_SELECTOR, "[ng-model='borrow_loan.period'][name='period']")
        self.loan_validate = (By.CSS_SELECTOR, "[ng-model='borrow_loan.validate'][name='validate']")
        self.loan_lowest_amount = (By.CSS_SELECTOR, "[ng-model='borrow_loan.tender_amount_min'][name='tender_amount_min']")
        self.loan_highest_amount = (By.CSS_SELECTOR, "[ng-model='borrow_loan.tender_amount_max'][name='tender_amount_max']")
        self.loan_describe = (By.CSS_SELECTOR, "[ng-model='borrow_loan.contents'][name='contents']")
        self.loan_vericode = (By.CSS_SELECTOR, "[ng-model='borrow_loan.valicode'][name='valicode']")
        self.loan_submit_btn = (By.CSS_SELECTOR, ".btn-submit.btn-md")
        self.loan_success_result = (By.CSS_SELECTOR, "[class='ng-binding'][target='_blank']")

    def loan_getin(self):
        """
        使用鼠标悬停操作进入借款页面
        :return:
        """
        action = ActionChains(self.driver)
        action.move_to_element(self.fd_element(self.loan_choose)).perform()
        self.base_click(self.loan)
        time.sleep(2)
    def loan_method_choose(self):
        """选择借款的标"""
        self.base_switch_handle(self.loan_credit).click()
        time.sleep(2)

    def loan_list(self, title, use_index, amount, period, repay_index, repay_time_index, validate_index, lowest_amount_index, highest_amount_index, describe, vericode):
        """
        填写借款表单信息
        :param title: 标题
        :param use_index: 用途索引
        :param amount: 金额
        :param period: 年利率
        :param repay_index: 还款方式索引
        :param repay_time_index: 还款时间索引
        :param validate_index: 验证码索引
        :param lowest_amount_index: 最低投资金额
        :param highest_amount_index: 最高投资金额
        :param describe: 描述
        :param vericode: 验证码
        :return:
        """
        self.base_input(self.loan_title, title)
        Select(self.fd_element(self.loan_use)).select_by_index(use_index)
        self.base_input(self.loan_amount, amount)
        self.base_input(self.loan_period, period)
        Select(self.fd_element(self.loan_repay)).select_by_index(repay_index)
        Select(self.fd_element(self.loan_repay_time)).select_by_index(repay_time_index)
        Select(self.fd_element(self.loan_validate)).select_by_index(validate_index)
        Select(self.fd_element(self.loan_lowest_amount)).select_by_index(lowest_amount_index)
        Select(self.fd_element(self.loan_highest_amount)).select_by_index(highest_amount_index)
        self.base_input(self.loan_describe, describe)
        self.base_input(self.loan_vericode, vericode)
        self.base_click(self.loan_submit_btn)
        time.sleep(2)

    def get_loan_success_result(self):
        """获取提交成功结果"""
        return self.fd_element(self.loan_success_result).text