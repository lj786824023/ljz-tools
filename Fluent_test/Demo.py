import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget

from Fluent_test.untitled import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        """需要修改原始tbw_1、tbw_2、tbw_3的类名MyTableWidget.CleverTableWidget()"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Pivot.currentItemChanged.connect(lambda k: self.ui.stackedWidget.setCurrentWidget(self.findChild(QWidget, k)))
        self.ui.Pivot.currentItemChanged.connect(lambda k: print(k))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec())