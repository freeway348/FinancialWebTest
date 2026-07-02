from page.page_loan import PageLoan
from script import log


class TestLoan:
    def test_01_loan_success(self, loan_page):
        """测试借款成功"""
        # 创建页面对象
        page_loan = PageLoan(loan_page)

        # 进入借款页面
        page_loan.loan_getin()

        page_loan.loan_method_choose()
        # 填写借款信息
        # 参数说明：标题, 用途索引, 金额, 年利率, 还款方式索引, 还款时间索引, 验证码索引, 最低投资金额, 最高投资金额, 描述, 验证码
        page_loan.loan_list(
            "测试借款标题",
            1,
            "10000",
            "10",
            1,
            1,
            1,
            "1",
            "2",
            "这是一笔测试借款",
            "8888"
        )

        # 获取借款成功结果
        result = page_loan.get_loan_success_result()
        log.info(f"借款结果：{result}")

        # 断言验证
        assert "借款" in result