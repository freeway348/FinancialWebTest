from page.page_register import PageRegister
from script import log


class TestRegister:

    def test_01_register_success(self, register_page):
        """测试注册成功"""
        register_page.register("13800002008", "Aa123456", "8888", "6666666")
        result = register_page.get_success_result()
        log.info(f"注册结果：{result}")
        assert "注册成功" in result

    def test_02_register_fail_phone_exist(self, register_page):
        """测试手机号已存在"""
        register_page.register("13800002004", "Aa123456", "8888", "6666666")
        result = register_page.get_fail_result()
        log.info(f"注册结果：{result}")
        assert "注册" in result

