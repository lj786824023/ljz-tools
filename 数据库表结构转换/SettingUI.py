# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(662, 429)
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.wid1 = QWidget(Dialog)
        self.wid1.setObjectName(u"wid1")
        self.wid1.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.wid1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.wid1)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_del = QPushButton(self.wid1)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_del)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.wid1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_3.addWidget(self.wid1)

        self.wid2 = QWidget(Dialog)
        self.wid2.setObjectName(u"wid2")
        self.verticalLayout_2 = QVBoxLayout(self.wid2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(self.wid2)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.wid2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.horizontalLayout_3.addWidget(self.wid2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e", None))
        self.btn_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u6e90\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u76ee\u6807\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u957f\u5ea6\u8f6c\u6362\u89c4\u5219", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u957f\u5ea6\u8f6c\u6362\u503c", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u7cbe\u5ea6\u8f6c\u6362\u89c4\u5219", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u7cbe\u5ea6\u8f6c\u6362\u503c", None));
    # retranslateUi

