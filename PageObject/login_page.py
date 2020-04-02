# coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver


# 封装速涡手游加速器登录页面操作对象及各个元素及操作方法
class Login_page(Base):

    def login_by_config_url(self):
        """
            从配置文件config.ini获取登录地址
        @return: 登录地址
        """
        return super().login_by_config_url()

    def get_home_page_url(self, url):
        """
            登录测试地址URL
        @param url: 登录页面URL
        """
        self.get_url(url)

    def get_username_attribute_value(self):
        """
            获得账号输入框的placeholder值
        @return: 获得账号输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "Username"))

    def get_password_attribute_value(self):
        """
            获得密码输入框的placeholder值
        @return:获得密码输入框的placeholder值
        """
        return super().get_placeholder((By.NAME, "Password"))

    def find_button_reset_password(self):
        """
            查找忘记密码按钮
        @return:忘记密码按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "GoResetPassword"))

    def find_button_login(self):
        """
            查找登录按钮
        @return:登录按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "LoginBtn"))

    def find_button_register(self):
        """
            查找注册按钮
        @return: 注册按钮文本值
        """
        return super().get_text((By.CLASS_NAME, "InputWarningA"))

    def click_login_btn(self):
        """
            点击登录按钮
        """
        super().click_btn((By.CLASS_NAME, "LoginBtn"))

    def click_reset_btn(self):
        """
            点击忘记密码按钮
        """
        super().click_btn((By.CLASS_NAME, "GoResetPassword"))

    def click_register_btn(self):
        """
            点击注册按钮
        """
        super().click_btn((By.CLASS_NAME, "InputWarningA"))

    def get_reset_page_title(self):
        """
            获得找回密码页面的title
        @return:title
        """
        return super().get_text((By.CLASS_NAME, "InputTitleText"))

    def get_register_page_title(self):
        """
            获得注册页面的title
        @return:title
        """
        return super().get_text((By.CLASS_NAME, "InputTitleText"))

    def get_error_text(self):
        """
            获得输入框输入错误的返回信息
        @return: 获得输入框输入错误的返回信息
        """
        return super().get_text((By.XPATH, "/html/body/div[2]/form/div[1]/span"))

    def username_send_keys(self, value):
        """
            输入账号输入框的值
        @param value: value
        """
        super().send_key((By.NAME, "Username"), value)

    def password_send_keys(self, value):
        """
            输入密码输入框的值
        @param value: value
        """
        super().send_key((By.NAME, "Password"), value)


if __name__ == "__main__":
    home_page = Login_page(webdriver.Chrome())
    home_page.login_by_config_url()
    print(home_page.find_button_login())
