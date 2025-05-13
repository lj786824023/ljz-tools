import io
import os.path
import re
import sys
import threading
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from qfluentwidgets import MessageBox

from PDFTransUI import Ui_Form


class PDFTrans(QWidget, Ui_Form):
    # def __init__(self, parent=None):
    #     # super().__init__()
    #     super().__init__(parent)
    #     self.setupUi(self)
    #     self.initUI()
    def __init__(self):
        # super().__init__()
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        sys.stdout = self
        sys.stderr = self

        self.btn_choose_pdf.clicked.connect(self.choose_pdf_file)
        self.btn_choose_outfile.clicked.connect(self.choose_outfile)
        self.btn_trans.clicked.connect(self.trans)
        self.rbtn_word.clicked.connect(self.choose_target_type)
        self.rbtn_ppt.clicked.connect(self.choose_target_type)

    def write(self, text):
        self.edt_log.moveCursor(QTextCursor.End)
        self.edt_log.insertPlainText(text)
        self.edt_log.moveCursor(QTextCursor.End)

    def choose_target_type(self, *args, **kwargs):
        object = self.sender()
        outfile = self.edt_outfile.text()
        if object.objectName() == "rbtn_word":
            outfile = re.sub(r".(docx|pptx)", r".docx", outfile)
        elif object.objectName() == "rbtn_ppt":
            outfile = re.sub(r".(docx|pptx)", r".pptx", outfile)
        else:
            pass
        self.edt_outfile.setText(outfile)

    def choose_pdf_file(self):
        file_name, _ = QFileDialog.getOpenFileName(None, "选择PDF文件", "", "PDF文档 (*.pdf)")
        self.edt_pdf.setText(file_name or "???")
        if self.rbtn_word.isChecked():
            outfile = re.sub(r".(pdf|docx|pptx)", r".docx", file_name)
        elif self.rbtn_ppt.isChecked():
            outfile = re.sub(r".(pdf|docx|pptx)", r".pptx", file_name)
        else:
            pass
        self.edt_outfile.setText(outfile)

    def choose_outfile(self):
        file_name, _ = QFileDialog.getSaveFileName(None,
                                                   "保存文件",
                                                   # "data.pdf",  # 默认文件名
                                                   os.path.basename(self.edt_pdf.text().replace(".pdf", ".docx")),
                                                   # 默认文件名
                                                   "Word文档(.docx);;PPT文档(.pptx)")
        self.edt_outfile.setText(file_name or "???")

    def trans(self):
        # self.edt_log.setText("日志信息：\n")
        self.edt_log.setText("")
        pdf_file = self.edt_pdf.text()
        outifle = self.edt_outfile.text()
        if not (pdf_file and outifle):
            print("未选择文件！")
            return

        if self.rbtn_word.isChecked():
            t = threading.Thread(target=pdf_to_word, args=[pdf_file, outifle])
        elif self.rbtn_ppt.isChecked():
            # pdf_to_ppt(pdf_file, outifle)
            t = threading.Thread(target=pdf_to_ppt, args=[pdf_file, outifle])
        else:
            pass
        t.start()

    def check_enable(self):
        """检查工具是否到期"""
        current_date = datetime.now().date()  # 获取当前日期
        enable_date = datetime.strptime("2025-12-31", "%Y-%m-%d").date()  # 工具有效期
        if current_date > enable_date:
            # QMessageBox.information(None, "消息", "已到使用有效期！", QMessageBox.Close)
            w = MessageBox("消息", "已到使用有效期！", self)
            if w.exec():
                self.close()
                sys.exit()
            else:
                self.close()
                sys.exit()
def pdf_to_word(pdf_file, docx_file):
    from pdf2docx import parse
    # convert pdf to docx
    parse(pdf_file, docx_file)


def pdf_to_ppt(pdf_file, pptx_file):
    from pdf2pptx import convert_pdf2pptx
    convert_pdf2pptx(pdf_file, pptx_file, 288, 0, None, False)  # resolution参数越大越清晰，默认72


if __name__ == "__main__":
    #   pyinstaller -F -i C:\Users\lojn\PycharmProjects\tool\img\App.ico -n pdf_tool .\Demo.py -w
    # 环境变量 dpi
    os.environ["QT_FONT_DPI"] = "AUTO"
    app = QtWidgets.QApplication(sys.argv)
    ui = PDFTrans()
    ui.show()
    ui.check_enable()  # 检查可用性
    sys.exit(app.exec())  # pyside6

