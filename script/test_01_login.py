from page.page_login import PageLogin
from script import log


class TestLogin:

    def test_01_login_success(self, a_login):
        """测试登录成功"""
        a_login.login("13800001001", "Aa123456")
        result = a_login.get_success_result()
        log.info(f"登录结果:{result}")
        assert "13800001001" == result

    def test_02_login_fail_pwd_error(self, a_login):
        """测试密码错误"""
        a_login.login("13800001001", "123456")
        result = a_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "密码错误" in result

    def test_03_login_fail_username_error(self, a_login):
        """测试用户名错误"""
        a_login.login("13800008001", "Aa123456")
        result = a_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "不存在" in result

    def test_04_login_fail_pwd_none(self, a_login):
        """测试密码为空"""
        a_login.login("13800008001", "")
        result = a_login.get_fail_result()
        log.info(f"登录结果:{result}")
        assert "不能为空" in result

