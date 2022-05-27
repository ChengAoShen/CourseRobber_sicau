from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Robber:
    def __init__(self, User, Pwd, year, classKey) -> None:
        self.User = User
        self.Pwd = Pwd
        self.year = year
        self.classKey = classKey

    def initBrower(self, debug: bool = False):
        """对网页进行初始化"""
        options = EdgeOptions()
        options.add_experimental_option(
            "excludeSwitches", ['disable-automation', 'enable-logging'])
        if not debug:
            options.add_argument("headless")
        self.browser = Edge(service=Service("./Driver/msedgedriver.exe"),
                            options=options)
        self.browser.get("http://jiaowu.sicau.edu.cn/web/web/web/index.asp")

    def login(self):
        """进行账号的登录"""
        self.browser.find_element(value="txtUser").send_keys(self.User)
        self.browser.find_element(value="Userpwd").send_keys(self.Pwd)
        self.browser.find_element(value="lb").click()
        self.browser.find_element(by='name', value="submit").click()

    def loadTable(self):
        """加载开课目录"""
        self.browser.get(
            f"http://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xszhinan.asp?title_id1=9&xueqi={self.year}")
        self.browser.find_element(
            By.XPATH, "/html/body/div/table[1]/tbody/tr/td[3]/a").click()
        self.browser.find_element(
            By.XPATH, "/html/body/div/div/center/table[2]/tbody/tr[8]/td[2]/a").click()

    def searchClass(self):
        """搜索相应编号的课程"""
        self.browser.find_element(
            By.XPATH, "/html/body/div/center/table[1]/tbody/tr[2]/td[2]/select/option[2]").click()
        self.browser.find_element(By.NAME, 'ww').send_keys(
            self.classKey, Keys.ENTER)

    def selectCourse(self):
        """选择课程"""
        self.browser.find_element(
            By.XPATH, '/html/body/div/center/table[3]/tbody/tr[2]/td[28]/a').click()
        alert = self.browser.switch_to.alert
        alert.accept()