import time
from page.page_credit_application import PageCreditApplication
from script import log


class TestCreditApplication:

    def test_01_credit_application_success(self, credit_application):
        """测试额度申请成功"""
        page_credit = PageCreditApplication(credit_application)
        page_credit.switch_role()
        page_credit.click_application()
        page_credit.credit_application("10000", "测试额度", "8888")
        time.sleep(2)
        result = page_credit.get_success_result()
        log.info(f"额度申请:{result}")
        assert "10,000.00" == result

