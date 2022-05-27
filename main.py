import PySide6
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from datetime import time

from Robber import Robber
from qt_material import apply_stylesheet


class Window:
    def __init__(self):
        super(Window, self).__init__()

        # 加载ui文件
        qfile = QFile("./windows.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 创建ui窗口对象
        self.ui = QUiLoader().load(qfile)
        self.ui.pushButton.clicked.connect(self.btnClick)

    def btnClick(self):
        user = self.ui.User.toPlainText()   # 获取文本信息
        pwd = self.ui.Pwd.toPlainText()
        year = self.ui.year.currentText()
        classKey = self.ui.classKey.toPlainText()
        if self.ui.checkBox.isChecked():
            t = self.ui.date.time()
            date = time(t.hour(), t.minute(), t.second())
            rob(user, pwd, year, classKey, date)
        else:
            rob(user, pwd, year, classKey)


def rob(User, Pwd, year, classKey, date=None):
    """抢课函数"""
    robber = Robber(User, Pwd, year, classKey, date)
    robber.initBrower(True)
    robber.login()
    robber.loadTable()
    robber.robCourse()


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = Window()
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    apply_stylesheet(app, theme='dark_red.xml')
    w.ui.show()
    app.exec()
