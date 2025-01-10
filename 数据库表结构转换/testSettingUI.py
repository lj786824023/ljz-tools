import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget


class subw(QDialog):
    def __init__(self, parent=None):
        super.__init__(parent)
        self.setWindowTitle("dialog")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        b = QPushButton(self, "open")
        b.setText("open")
        b.clicked.connect(self.zi)
        # self..connect(lambda: print(555))
        self.show()

    def zi(self):
        print(666)
        self.w = QWidget()
        self.w.show()

        self.setDisabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec())
