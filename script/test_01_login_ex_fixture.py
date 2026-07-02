import pytest

from page.page_login import PageLogin
from script import log
from tools import DriverTools, read_json


class TestLogin:

    @pytest.mark.parametrize("phone,password,expect", read_json("login_data.json"))
    def test_01_login(self,a_login, phone, password, expect):
        # 准备数据
        try:
            # 调用方法
            a_login.login(phone, password)
            # 获取结果
            if expect == phone:
                result = a_login.get_success_result()
            else:
                result = a_login.get_fail_result()
            # 打印日志
            log.debug(f"登录结果: {result} | 期望值: {expect}")
            # 断言
            assert expect in result
        except Exception as e:
            log.error(f"测试执行过程中发生异常: {e}")
            raise

