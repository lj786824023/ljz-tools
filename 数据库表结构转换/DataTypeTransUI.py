# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataTypeTransUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout,
    QWidget)

from MyWidget.TableWidget import TableWidget
from qfluentwidgets import (ComboBox, PushButton)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = ComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = PushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = PushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = PushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = PushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = TableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(20)

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u8868\u7ed3\u6784\u8f6c\u6362", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u914d\u7f6e1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u914d\u7f6e2", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--\u9009\u62e9\u914d\u7f6e\u6587\u4ef6--", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u914d\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u9875\u9762", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210DDL", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8868\u82f1\u6587\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8868\u4e2d\u6587\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bb5\u82f1\u6587\u540d", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bb5\u4e2d\u6587\u540d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bb5\u7c7b\u578b", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u7cbe\u5ea6", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u540e\u7c7b\u578b", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u540e\u957f\u5ea6", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u540e\u7cbe\u5ea6", None));
    # retranslateUi

