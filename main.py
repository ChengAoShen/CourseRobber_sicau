import PySide6
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon

from collections import namedtuple
from Robber import Robber
from qt_material import apply_stylesheet


class Window:
    def __init__(self):
        super(Window, self).__init__()

        # 加载ui文件
        qfile = QFile("static/windows.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 创建ui窗口对象
        self.ui = QUiLoader().load(qfile)
        self.ui.pushButton.clicked.connect(self.btnClick)
        self.ui.loginButton.clicked.connect(self.login)

        self.robber = None

        self.output=self.ui.OutputText

    def login(self):
        user = self.ui.User.toPlainText()   # 获取文本信息
        pwd = self.ui.Pwd.toPlainText()
        self.robber = Robber(user, pwd)
        if self.ui.EdgeWindows.isChecked():
            self.robber.initBrower(False)
        else:
            self.robber.initBrower(True)
        self.output.append(f"开始登录，用户名为{user},密码为{pwd}")
        self.robber.login()
        self.output.append(f"登录成功")

    def btnClick(self):
        year = self.ui.year.currentText()
        classKey = self.ui.classKey.toPlainText()
        if len(classKey)==0:
            self.output.append('没有填写课程号')
            return
        date = None
        if self.ui.checkBox.isChecked():
            t = self.ui.date.time()
            Date = namedtuple('Date', 'hour minute second')
            date = Date(t.hour(), t.minute(), t.second())
        if self.robber is None:
            self.login()
            self.robber.refresh_item(year, classKey,date)
        else:
            self.robber.refresh_item(year, classKey,date)
        self.rob()

    def rob(self):
        """抢课函数"""
        try:
            self.robber.loadTable()
        except:
            self.output.append(f"注意：{self.robber.year}课表还未开放,请等待")
            self.output.append("如果目的是为了测试可以切换到上一学期的进行")
            return
        self.robber.robCourse()


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon("./static/cat.ico"))
    w = Window()
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    apply_stylesheet(app, theme='dark_red.xml')
    w.ui.show()
    app.exec()
