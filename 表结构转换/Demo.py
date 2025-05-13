import os
import sys

from PySide6 import QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidgetItem, QTableWidgetItem, QComboBox
from loguru import logger
from openpyxl.reader.excel import load_workbook
from qfluentwidgets import InfoBar, InfoBarPosition, ComboBox, LineEdit

from 表结构转换.ConfigFile import ConfigFile
from 表结构转换.TableTransUI import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        """需要修改原始tbw_1、tbw_2、tbw_3的类名MyTableWidget.CleverTableWidget()"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setting_file = f"{os.path.dirname(sys.argv[0])}/_internal/aaa_etc/表结构转换规则.xlsx"
        self.workbook = load_workbook(
            f"{os.path.dirname(sys.argv[0])}/_internal/aaa_etc/表结构转换规则.xlsx")  # excel对象
        self.settings = []  # 配置清单
        self.column_types = (
            'bigint', 'blob', 'char', 'clob', 'date', 'datetime', 'decimal', 'float', 'int', 'integer', 'longtext',
            'number', 'nvarchar', 'text', 'time', 'timestamp', 'varchar', 'varchar2')  # 类型列表
        self.column_x_rule = ("长度不变", "长度固定", "长度扩长n倍")  # 长度规则
        self.column_y_rule = ("精度不变", "精度固定", "精度扩长n倍")  # 精度规则

        self.ui.Pivot.currentItemChanged.connect(
            lambda k: self.ui.stackedWidget.setCurrentWidget(self.findChild(QWidget, k)))
        self.ui.btn_add_setting.clicked.connect(self.add_setting)  # 新增配置
        self.ui.btn_del_setting.clicked.connect(self.del_setting)  # 删除配置
        self.ui.lsw_setting.itemClicked.connect(self.show_setting)  # 显示配置
        self.ui.lsw_setting.itemChanged.connect(self.rename_setting)  # 重命名配置
        self.ui.btn_save_setting.clicked.connect(self.save_setting)  # 保存配置

        self.init_ui()

    def abc(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def add_setting(self):
        """新增配置"""
        setting_name = '配置'
        db_list = []

        for i in range(1, 100):
            setting_name = f"配置{i}"
            if setting_name not in self.settings:
                break
        self.settings.append(setting_name)  # 变量新增
        # ii = ListWidgetItem("可编辑项")
        item = QListWidgetItem(setting_name)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.lsw_setting.addItem(item)  # 列表新增
        self.ui.cbb_setting.addItem(setting_name)  # 下拉框新增

        sheet = self.workbook['配置清单']
        sheet.cell(row=sheet.max_row + 1, column=1).value = setting_name

        # self.workbook.create_sheet(setting_name)
        # 复制默认配置
        source = self.workbook['默认配置']
        target = self.workbook.copy_worksheet(source)
        target.title = setting_name

        self.workbook.save(self.setting_file)

    def createErrorInfoBar(self, text):
        w = InfoBar.error(
            title='ERROR',
            content=text,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM,
            duration=2000,
            parent=self
        )
        # w.addWidget(PushButton('Action'))
        w.show()

    def createInfoInfoBar(self, text):
        w = InfoBar.info(
            title='INFO',
            content=text,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM,
            duration=2000,
            parent=self
        )
        # w.addWidget(PushButton('Action'))
        w.show()

    def createSuccessInfoBar(self, text):
        InfoBar.success(
            title='SUCCESS',
            content=text,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

    def del_setting(self):
        """删除配置"""
        item = self.ui.lsw_setting.currentItem()
        if not item:
            return

        if item.text() == '默认配置':
            self.createInfoInfoBar("默认配置不可删除！")
            return

        row = self.ui.lsw_setting.currentRow()
        text = item.text()
        self.ui.lsw_setting.takeItem(row)  # 从列表框中移除
        for i in range(self.ui.cbb_setting.count()):  # 从下拉框中移除
            if self.ui.cbb_setting.itemText(i) == text:
                self.ui.cbb_setting.removeItem(i)
                break
        self.settings.remove(text)  # 从变量中移除

        sheet = self.workbook["配置清单"]
        # sheet.delete_rows(1,sheet.max_row)
        for i in range(1, sheet.max_row + 1):
            cell = sheet.cell(row=i, column=1)
            if cell.value == text:
                sheet.delete_rows(cell.row, 1)  # 从某行开始删1行
                break
        del self.workbook[text]  # 删除工作表
        self.workbook.save(self.setting_file)

    def init_ui(self):
        """初始化ui"""

        # 读取配置清单
        # self.wb = load_workbook(self.setting_file)
        st = self.workbook["配置清单"]
        self.settings = [row[0] for row in st.iter_rows(min_row=1, max_col=1, values_only=True)]

        # 初始化配置清单
        self.ui.lsw_setting.clear()
        for setting in self.settings:
            item = QListWidgetItem(setting)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.lsw_setting.addItem(item)

        # 初始化下拉框
        self.ui.cbb_setting.clear()
        for setting in self.settings:
            self.ui.cbb_setting.addItem(setting)

        self.ui.tbw_table.tbw_table.setRowCount(100)
        self.ui.tbw_table.tbw_table.setColumnCount(9)
        self.ui.tbw_table.tbw_table.setHorizontalHeaderLabels(('表英文名','表中文名','字段英文名','字段中文名','字段类型','长度','精度','转换后长度','转换后精度'))

        self.ui.tbw_setting.setRowCount(len(self.column_types))

    def rename_setting(self, item: QListWidgetItem):
        """重命名配置"""
        text = item.text()
        row = self.ui.lsw_setting.currentRow()

        self.ui.cbb_setting.setItemText(row, text)  # 重命名下拉框数据

        sheet = self.workbook['配置清单']
        sheet.cell(row=row + 1, column=1).value = text  # 重命名配置清单

        self.workbook[self.settings[row]].title = text  # 重命名配置明细
        self.settings[row] = text  # 重命名变量

        self.workbook.save(self.setting_file)

    def save_setting(self):
        """保存配置"""
        item = self.ui.lsw_setting.currentItem()
        if not item:
            self.createInfoInfoBar("未选中配置！")
            return

        sheet = self.workbook[item.text()]
        sheet.delete_rows(2, sheet.max_row)  # 清空

        for row in range(self.ui.tbw_setting.rowCount()):
            text1 = self.ui.tbw_setting.item(row, 0).text()
            text2 = self.ui.tbw_setting.cellWidget(row, 1).currentText()
            text3 = self.ui.tbw_setting.cellWidget(row, 2).currentText()
            text4 = self.ui.tbw_setting.item(row, 3).text()
            text5 = self.ui.tbw_setting.cellWidget(row, 4).currentText()
            text6 = self.ui.tbw_setting.item(row, 5).text()
            line = (text1, text2, text3, text4, text5, text6)
            # logger.info(line)
            sheet.append(line)

        self.workbook.save(self.setting_file)

        try:
            self.workbook.save(self.setting_file)
            self.createSuccessInfoBar('保存成功！')
        except:
            self.createErrorInfoBar('保存失败！文件可能已经打开')

    def show_setting(self, item: QListWidgetItem):
        """
        配置点击
        查找所有sheet，如果有直接读取数据，如果没有创建新的sheet
        """
        setting = item.text()
        sheet = self.workbook[setting]
        excel_data = list(sheet.values)[1:]
        self.ui.tbw_setting.clearContents()
        for row in range(len(excel_data)):
            # for col in range(len(excel_data[row])):
            #     data = QTableWidgetItem(str(excel_data[row][col] or ""))
            #     combo = ComboBox()
            #     combo.addItems(('int', 'varchar', 'date'))
            #     combo.setCurrentIndex(col % 2)
            #     # self.ui.tbw_setting.setItem(row, col, data)
            #     self.ui.tbw_setting.setCellWidget(row, col, combo)

            data = QTableWidgetItem(str(excel_data[row][0] or ""))  # 第1列
            self.ui.tbw_setting.setItem(row, 0, data)
            combo = ComboBox()  # 第2列
            combo.addItems(self.column_types)
            combo.setCurrentIndex(self.column_types.index(excel_data[row][1]))
            self.ui.tbw_setting.setCellWidget(row, 1, combo)
            combo = ComboBox()  # 第3列
            combo.addItems(self.column_x_rule)
            combo.setCurrentIndex(self.column_x_rule.index(excel_data[row][2]))
            self.ui.tbw_setting.setCellWidget(row, 2, combo)
            # data = QTableWidgetItem(str(excel_data[row][3] or ""))  # 第4列
            # self.ui.tbw_setting.setItem(row, 3, data)
            data = LineEdit()  # 第6列
            data.setText(str(excel_data[row][3] or ""))
            self.ui.tbw_setting.setCellWidget(row, 3, data)
            combo = ComboBox()  # 第5列
            combo.addItems(self.column_y_rule)
            combo.setCurrentIndex(self.column_y_rule.index(excel_data[row][4]))
            self.ui.tbw_setting.setCellWidget(row, 4, combo)
            # data = QTableWidgetItem(str(excel_data[row][5] or ""))  # 第6列
            # self.ui.tbw_setting.setItem(row, 5, data)
            data = LineEdit()  # 第6列
            data.setText(str(excel_data[row][5] or ""))
            self.ui.tbw_setting.setCellWidget(row, 5, data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec())
