from config import *
from script import log


class TestOpenAccount:

    def test_01_open_account_success(self, open_account_page):
        """测试开户成功"""
        open_account_page.open_account(NAME, CARD)
        result = open_account_page.get_success_result()
        log.info(f"开户结果：{result}")
        assert "OK" in result

