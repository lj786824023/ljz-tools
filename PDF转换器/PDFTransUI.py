# -*- coding: utf-8 -*-
import sys

from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'PDFTransUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, RadioButton,
                            TextEdit)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(648, 604)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edt_pdf = LineEdit(Form)
        self.edt_pdf.setObjectName(u"edt_pdf")

        self.horizontalLayout.addWidget(self.edt_pdf)

        self.btn_choose_pdf = PushButton(Form)
        self.btn_choose_pdf.setObjectName(u"btn_choose_pdf")

        self.horizontalLayout.addWidget(self.btn_choose_pdf)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbtn_word = RadioButton(Form)
        self.rbtn_word.setObjectName(u"rbtn_word")
        self.rbtn_word.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rbtn_word)

        self.rbtn_ppt = RadioButton(Form)
        self.rbtn_ppt.setObjectName(u"rbtn_ppt")

        self.horizontalLayout_2.addWidget(self.rbtn_ppt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edt_outfile = LineEdit(Form)
        self.edt_outfile.setObjectName(u"edt_outfile")

        self.horizontalLayout_3.addWidget(self.edt_outfile)

        self.btn_choose_outfile = PushButton(Form)
        self.btn_choose_outfile.setObjectName(u"btn_choose_outfile")

        self.horizontalLayout_3.addWidget(self.btn_choose_outfile)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_trans = PrimaryPushButton(Form)
        self.btn_trans.setObjectName(u"btn_trans")

        self.verticalLayout.addWidget(self.btn_trans)

        self.edt_log = TextEdit(Form)
        self.edt_log.setObjectName(u"edt_log")

        self.verticalLayout.addWidget(self.edt_log)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PDF\u8f6c\u6362", None))
        self.btn_choose_pdf.setText(QCoreApplication.translate("Form", u"\u9009\u62e9PDF\u6587\u4ef6", None))
        self.rbtn_word.setText(QCoreApplication.translate("Form", u"\u8f6cword\uff08.docx\uff09", None))
        self.rbtn_ppt.setText(QCoreApplication.translate("Form", u"\u8f6cppt\uff08.pptx\uff09", None))
        self.btn_choose_outfile.setText(
            QCoreApplication.translate("Form", u"\u9009\u62e9\u5bfc\u51fa\u8def\u5f84", None))
        self.btn_trans.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.edt_log.setHtml(QCoreApplication.translate("Form",
                                                        u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "hr { height: 1px; border-width: 0; }\n"
                                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                                        "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                        None))
    # retranslateUi


if __name__ == "__main__":
    # os.environ["QT_FONT_DPI"] = "AUTO"
    app = QtWidgets.QApplication(sys.argv)
    w = QWidget() # 定义一个窗口
    ui = Ui_Form() # 定义设计好的ui
    ui.setupUi(w) # 用设计好的ui去刷新w窗口
    w.show() # 显示w窗口
    # ui.check_enable()  # 检查可用性
    sys.exit(app.exec())  # pyside6
