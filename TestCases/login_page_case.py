# coding:utf-8
import unittest
from selenium import webdriver
from PageObject.login_page import Login_page
from PageObject.buy_page import Buy_page
from Common.log_option import log, log_INFO, log_ERROR, log_DEBUG, log_WARNING
from selenium.webdriver.chrome.options import Options


class Login_page_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log_WARNING("类前执行一次")

    @classmethod
    def tearDownClass(cls):
        log_WARNING("类后执行一次")

    def setUp(self):
        log_WARNING("开始执行case")
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Chrome()
        self.login_page = Login_page(self.driver)
        self.buy_page = Buy_page(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        log_WARNING("结束执行case")

    def test_DLZC1(self):
        self.login_page.login_by_config_url()
        username_input_attribute_value = self.login_page.get_username_attribute_value()
        password_input_attribute_value = self.login_page.get_password_attribute_value()
        reset_btn_text = self.login_page.find_button_reset_password()
        login_btn_text = self.login_page.find_button_login()
        register_btn_text = self.login_page.find_button_register()
        self.assertEqual(username_input_attribute_value, "邮箱/手机号码")
        self.assertEqual(password_input_attribute_value, "密码")
        self.assertEqual(reset_btn_text, "忘记密码？")
        self.assertEqual(login_btn_text, "登录")
        self.assertEqual(register_btn_text, "注册")

    def test_DLZC2(self):
        self.login_page.login_by_config_url()
        self.login_page.click_reset_btn()
        reset_title = self.login_page.get_reset_page_title()
        self.assertEqual(reset_title, "找回密码")

    def test_DLZC3(self):
        self.login_page.login_by_config_url()
        self.login_page.click_register_btn()
        register_title = self.login_page.get_register_page_title()
        self.assertEqual(register_title, "注册")

    def test_DLZC4(self):
        self.login_page.login_by_config_url()
        self.login_page.click_login_btn()
        error_text = self.login_page.get_error_text()
        self.assertEqual(error_text, "帐号不能为空")

    def test_DLZC5(self):
        self.login_page.login_by_config_url()
        self.login_page.username_send_keys(1)
        self.login_page.click_login_btn()
        error_text = self.login_page.get_error_text()
        self.assertEqual(error_text, "密码不能为空")

    def test_DLZC6(self):
        self.login_page.login_by_config_url()
        self.login_page.username_send_keys("1")
        self.login_page.password_send_keys("1")
        self.login_page.click_login_btn()
        error_text = self.login_page.get_error_text()
        self.assertEqual(error_text, "账号不存在")

    def test_DLZC7(self):
        self.login_page.login_by_config_url()
        self.login_page.username_send_keys("13199044512")
        self.login_page.password_send_keys("1")
        self.login_page.click_login_btn()
        error_text = self.login_page.get_error_text()
        self.assertEqual(error_text, "密码错误")

    def test_DLZC8(self):
        self.login_page.login_by_config_url()
        self.login_page.username_send_keys("13199044512")
        self.login_page.password_send_keys("123")
        self.login_page.click_login_btn()
        btn_buy_text = self.buy_page.find_button_buy()
        print(btn_buy_text)
        self.assertEqual(btn_buy_text, "购买")

    def test_DLZC9(self):
        self.login_page.login_by_config_url()
        self.login_page.username_send_keys("test1@qq.com")
        self.login_page.password_send_keys("123")
        self.login_page.click_login_btn()
        btn_buy_text = self.buy_page.find_button_buy()
        print(btn_buy_text)
        self.assertEqual(btn_buy_text, "购买")


if __name__ == "__main__":
    login_page_case = Login_page_case()
    login_page_case.test_DLZC4()
