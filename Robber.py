from lib2to3.pgen2 import driver
from re import T
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class Robber:
    def __init__(self, User: str, Pwd: str, year: str = None, classKey=None, date=None):
        """初始化

        Args:
            User (str): 用户名
            Pwd (str): 用户密码
            year (str): 选择的学年，如'2021-2022-2'
            classKey (_type_): 课程编号，可以是列表或者单个编号
            date (str): 选择的具体时间
        """
        self.User = User
        self.Pwd = Pwd
        self.year = year
        self.classKey = classKey
        self.date = date

    def initBrower(self, debug: bool = False):
        """对网页进行初始化"""
        options = Options()
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
        flag=False
        try:
            alter=self.browser.switch_to.alert
            alter.accept()
            flag=True
        except:
            ...
        if flag:
            raise RuntimeError(alter.text)

        self.browser.find_element(
            By.XPATH, "/html/body/div/table[1]/tbody/tr/td[3]/a").click()
        self.browser.find_element(
            By.XPATH, "/html/body/div/div/center/table[2]/tbody/tr[8]/td[2]/a").click()

    def robCourse(self):
        """抢课函数"""
        if self.date:
            self._robCourseByTime()
        else:
            self._justRobCourse()

    def _robCourseByTime(self):
        """使用定时器进行抢课"""
        while self.date.hour >= time.localtime().tm_hour and self.date.minute > time.localtime().tm_min:
            ...
        self._justRobCourse()

    def _justRobCourse(self):
        """进行普通的抢课"""
        if type(self.classKey) == list:
            for key in self.classKey:
                self._searchClass(key)
                self._selectCourse()
        elif type(self.classKey) == str:
            self._searchClass(self.classKey)
            self._selectCourse()

    def _searchClass(self, key):
        """搜索相应编号的课程"""
        self.browser.find_element(
            By.XPATH, "/html/body/div/center/table[1]/tbody/tr[2]/td[2]/select/option[2]").click()
        self.browser.find_element(By.NAME, 'ww').send_keys(
            key, Keys.ENTER)

    def _selectCourse(self):
        """选择课程"""
        self.browser.find_element(
            By.XPATH, '/html/body/div/center/table[3]/tbody/tr[2]/td[28]/a').click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def refresh_item(self,year,classKey,date=None):
        self.year=year
        self.classKey=classKey
        self.date=date
