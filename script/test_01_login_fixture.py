from page.page_login import PageLogin
from script import log
from tools import DriverTools


class TestLogin:

    def test_01_login_success(self,a_login):
        # 调用方法
        a_login.login("13800001001","Aa123456")
        # 打印日志
        result = a_login.get_success_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        # 断言
        assert "13800001001" == result

    def test_02_login_fail_pwd_error(self,a_login):
        # 调用方法
        a_login.login("13800001001", "123456")
        # 打印日志
        result = a_login.get_fail_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        # 断言
        assert "密码错误" in result

    def test_03_login_fail_username_error(self,browser):
        # 创建对象
        self.page_login = PageLogin(browser)
        # 调用方法
        self.page_login.open_url()
        # 调用方法
        self.page_login.login("13800008001", "Aa123456")
        # 打印日志
        result = self.page_login.get_fail_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        # 断言
        assert "不存在" in result

    def test_04_login_fail_pwd_none(self,browser):
        # 创建对象
        self.page_login = PageLogin(browser)
        # 调用方法
        self.page_login.open_url()
        # 调用方法
        self.page_login.login("13800008001", "")
        # 打印日志
        result = self.page_login.get_fail_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        # 断言
        assert "不能为空" in result
