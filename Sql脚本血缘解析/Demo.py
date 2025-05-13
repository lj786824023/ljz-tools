import os
import re
import sys

import chardet
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QFileDialog
from Highlighter import Highlighter
from Sql脚本血缘解析.FileBloodUI import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        """需要修改原始tbw_1、tbw_2、tbw_3的类名MyTableWidget.CleverTableWidget()"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.highlighter_file_content = Highlighter(self.ui.edt_file_content.document())  # 文本文件内容高亮
        self.ui.lsw_blood.itemClicked.connect(self.show_file_content)  # 血缘文件清单项目点击
        self.ui.btn_dir_blood.clicked.connect(self.choose_dir_blood)  # 血缘选择目录按钮点击
        self.ui.edt_file_content.textChanged.connect(self.show_file_blood)  # 血缘文件内容文本改变

        # 设置血缘页左右比例
        self.ui.splitter.setStretchFactor(0, 3)
        self.ui.splitter.setStretchFactor(1, 5)
        self.ui.splitter.setStretchFactor(2, 2)

    def choose_dir_blood(self):
        """选择并设置工作目录"""
        directory = QFileDialog.getExistingDirectory(None, "选择目录", os.getcwd())  # 获取目录
        if not directory:  # 如果没有选择目录
            return
        self.ui.edt_dir_blood.setText(directory)
        file_list = os.listdir(directory)  # 获取文件列表
        file_list.sort()  # 升序
        # 添加lsw
        self.ui.lsw_blood.clear()
        self.ui.lsw_blood.addItems(file_list)

    def show_file_content(self, item: QListWidgetItem = None) -> None:
        """显示文件内容"""
        file_name = item.text()
        file_path = self.ui.edt_dir_blood.text() + "/" + file_name
        if not is_text_file(file_path):
            print(f"{file_path}不是一个文本文件！")
            return
        # 打开文件
        with open(file_path, 'rb') as f:  # 获取编码
            data = f.read()
            file_encoding = chardet.detect(data)["encoding"]
        with open(file_path, encoding=file_encoding) as f:
            file_content = f.read()
        # 显示
        self.ui.lab_file_name.setText(file_name)
        self.ui.edt_file_content.setText(file_content)

    def show_file_blood(self):
        """显示文件血缘"""
        text = self.ui.edt_file_content.toPlainText()
        tab_list = pars_text(text)
        bloods = "".join(tab + "\n" for tab in tab_list)
        self.ui.edt_file_blood.setText(bloods)

def is_text_file(file_path: str = "") -> bool:
    """检查文件是否是文本文件"""
    # 判断文件
    if os.path.isdir(file_path):
        print("选中到是一个目录！")
        return False
    # 检查文件扩展名是否常见的文本文件扩展名
    text_extensions = {'txt', 'css', 'html', 'js', 'json', 'py', 'md', 'csv', 'xml', 'sql', 'proc'}
    file_extension = os.path.splitext(file_path)[1].strip('.').lower()
    if file_extension in text_extensions:
        return True
    # 尝试检测文件编码
    with open(file_path, 'rb') as f:
        data = f.read()
    # 使用chardet检测编码
    import chardet
    result = chardet.detect(data)
    if result['confidence'] > 0.8:  # 置信度高于80%的情况下，认为是文本文件
        return True
    return False


def pars_text(text: str = "") -> list:
    """解析存储过程文本，提出血缘表，返回列表"""
    """
    1.过滤注释内容
    2.转成单行文本
    3.按分号转成多行文本
    4.提取有用的sql
    5.逐句处理
      处理规则：
        遇到from、join就换行
        from后面匹配表名，join on之间匹配表名
    """
    tab_list = []
    text = re.sub(r"--.*|/\*[\s\S]*?\*/|['|]+", '', text)  # 去掉--和/* */注释的内容
    text = re.sub(r"\n", '', text)  # 转成单行文本
    text = re.sub(r"[\t ]+", ' ', text)  # 精简内容，去掉不必要的空白内容
    text = re.sub(r";", ';\n', text)  # 按;转成多行文本
    sql_lines = re.findall(r"select .*? from .*?;|insert .*?;|delete .*?;|update .*?;", text, re.I)  # 提取含有增删改查的行
    # 逐句处理
    for sql_line in sql_lines:
        lines = re.sub(r"(from|join)", "\n\\1", sql_line, 0, re.I).splitlines()  # 遇到from join就换行，返回列表
        # 逐行处理
        for line in lines:
            # 注意理解(?<=from\s) (?:[\w_${}]+\.)的含义
            tabs = re.findall(r"(?<=from\s)(?:[\w_${}]+\.)?[\w_]+|(?<=join\s)(?:[\w_${}]+\.)?[\w_]+", line, re.I)
            tab_list += tabs
    return sorted(list(set(tab_list)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec())
