import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from 数据库表结构转换.ui.DataTypeTransUI import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        """需要修改原始tbw_1、tbw_2、tbw_3的类名MyTableWidget.CleverTableWidget()"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec())
