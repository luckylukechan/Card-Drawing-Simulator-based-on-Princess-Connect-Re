# -*- coding: utf-8 -*-

import sys
from time import sleep

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from chouka import Ui_Form
import random_ten
import random_one


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_background()

        self.setAutoFillBackground(True)
        self.load_gemstone_data()
        self.load_num_data()
        self.label_2_num()

        self.setup_progressBar()  # 使用新的方法名称

        self.ten.clicked.connect(self.on_ten_clicked)
        self.one.clicked.connect(self.on_one_clicked)
        self.jia.clicked.connect(self.on_jia_clicked)
        self.pushButton.clicked.connect(self.show_characters)

        self.jia_button_timer = None
        self.buttons_enabled = True

    def setup_progressBar(self):  # 修改方法名称
        self.progressBar.setAttribute(Qt.WA_TranslucentBackground)
        self.progressBar.setStyleSheet(
            "QProgressBar { border: 2px solid gray; border-radius: 5px; text-align: center; }"
            "QProgressBar::chunk { background: lightblue; width: 10px; }")
        self.progressBar.setRange(0, 100)

    def label_2_num(self):
        character_count = self.count_characters_in_ihave()
        label_2 = getattr(self, "label_2", None)
        if label_2:
            label_2.setText("")  # 清空文本
            label_2.setText(str(character_count))  # 将整数转换为字符串后设置

    def set_background(self):
        image_path = '../data/xz.jpg'
        self.background_image = QtGui.QPixmap(image_path)
        self.update_background()

    def update_background(self):
        scaled_image = self.background_image.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding,
                                                    QtCore.Qt.SmoothTransformation)
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(scaled_image))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def show_insufficient_gemstone_message(self, required):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("宝石不足")
        msg_box.setText(f"你的宝石不足，至少需要 {required} 个宝石。")
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def disable_buttons(self):
        self.ten.setEnabled(False)
        self.one.setEnabled(False)
        self.buttons_enabled = False

    def enable_buttons(self):
        self.ten.setEnabled(True)
        self.one.setEnabled(True)
        self.buttons_enabled = True

    def update_files_and_labels(self, gemstone_change, num_change):
        try:
            gemstone_file = '../docs/gemstone.data'
            with open(gemstone_file, 'r', encoding='utf-8') as file:
                gemstone_value = int(file.read().strip())

            num_file = '../docs/num.data'
            with open(num_file, 'r', encoding='utf-8') as file:
                num_value = int(file.read().strip())

            if gemstone_value + gemstone_change < 0:
                self.show_insufficient_gemstone_message(-gemstone_change)
                self.disable_buttons()
                return False

            new_gemstone_value = gemstone_value + gemstone_change
            new_num_value = num_value + num_change

            with open(gemstone_file, 'w', encoding='utf-8') as file:
                file.write(str(new_gemstone_value))

            with open(num_file, 'w', encoding='utf-8') as file:
                file.write(str(new_num_value))

            self.gemstone.setText(str(new_gemstone_value))
            self.num.setText(str(new_num_value))

            self.enable_buttons()
            return True

        except Exception as e:
            print(f"更新文件时出错: {e}")
            return False

    def on_ten_clicked(self):
        sleep(0.25)
        if not self.buttons_enabled:
            return

        if hasattr(self, 'ten_button_timer') and self.ten_button_timer.isActive():
            return

        self.ten_button_timer = QtCore.QTimer(self)
        self.ten_button_timer.setSingleShot(True)
        self.ten_button_timer.start(500)

        if not self.update_files_and_labels(-1500, 10):
            return

        draw_results, jdt = random_ten.random_ten()  # 从 random_ten.py 获取结果

        if jdt:
            for i in range(101):
                sleep(0.01)  # 模拟一些工作
                self.progressBar.setValue(i)  # 更新进度条值
            sleep(0.25)
            self.progressBar.setValue(0)


        # 定义显示图片的路径
        image_paths = {
            "金": "../data/jin.jpg",
            "银": "../data/yin.jpg",
        }

        # 显示图片到对应的标签
        for i, result in enumerate(draw_results):
            label = getattr(self, f"label{i + 1}", None)
            label2 = getattr(self, f"label1_{i + 1}", None)

            label2.setText(result)

            if label:
                if result in image_paths:
                    image_path = image_paths[result]  # 如果结果是“金”或“银”
                else:
                    image_path = "../data/cai.jpg"  # 结果既不是“金”也不是“银”
                pixmap = QtGui.QPixmap(image_path)
                label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

        character_count = self.count_characters_in_ihave()
        label_2 = getattr(self, "label_2", None)
        if label_2:
            label_2.setText("")  # 清空文本
            label_2.setText(str(character_count))  # 将整数转换为字符串后设置

    def on_one_clicked(self):
        sleep(0.25)
        if not self.buttons_enabled:
            return

        if hasattr(self, 'one_button_timer') and self.one_button_timer.isActive():
            return

        self.one_button_timer = QtCore.QTimer(self)
        self.one_button_timer.setSingleShot(True)
        self.one_button_timer.start(300)

        if not self.update_files_and_labels(-150, 1):
            return

        # 获取结果
        draw_results1, jdt = random_one.random_one()  # 从 random_one.py 获取结果

        if jdt:
            for i in range(101):
                sleep(0.01)  # 模拟一些工作
                self.progressBar.setValue(i)  # 更新进度条值
            sleep(0.25)
            self.progressBar.setValue(0)

        # 定义显示图片的路径
        image_paths = {
            "金": "../data/jin.jpg",
            "银": "../data/yin.jpg",
        }

        # 清空所有 label1_i 的文本
        for i in range(1, 11):  # 假设有 label1_1 到 label1_10
            label2 = getattr(self, f"label1_{i}", None)
            if label2:
                label2.setText("")  # 清空文本

        for i in range(1, 11):  # 假设有 label1 到 label10
            label = getattr(self, f"label{i}", None)
            if label:
                label.clear()  # 清空图片显示

        # 显示结果到第一个 label1_1
        if draw_results1:  # 确保有返回值
            result = draw_results1[0]  # 只取第一个结果
            label2 = self.label1_1  # 只更新 label1_1
            if label2:
                label2.setText(result)  # 更新文本

            # 更新图片标签
            label = self.label1  # 假设 label1 是对应的图片标签
            if label:
                image_path = image_paths.get(result, "../data/cai.jpg")  # 如果结果不在路径中则使用默认
                pixmap = QtGui.QPixmap(image_path)
                label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

        character_count = self.count_characters_in_ihave()
        label_2 = getattr(self, "label_2", None)
        if label_2:
            label_2.setText("")  # 清空文本
            label_2.setText(str(character_count))  # 将整数转换为字符串后设置

    def count_characters_in_ihave(self):
        try:
            ihave_file = '../docs/ihave.data'
            with open(ihave_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                character_count = len(lines)  # 计算行数
            return character_count - 2
        except Exception as e:
            print(f"读取 ihave 文件时出错: {e}")
            return 0

    def load_gemstone_data(self):
        try:
            gemstone_file = '../docs/gemstone.data'
            with open(gemstone_file, 'r', encoding='utf-8') as file:
                gemstone_value = file.read().strip()
                self.gemstone.setText(gemstone_value)
        except Exception as e:
            print(f"读取 gemstone 文件时出错: {e}")

    def load_num_data(self):
        try:
            num_file = '../docs/num.data'
            with open(num_file, 'r', encoding='utf-8') as file:
                num_value = file.read().strip()
                self.num.setText(num_value)
        except Exception as e:
            print(f"读取 num 文件时出错: {e}")

    def on_jia_clicked(self):
        if self.jia_button_timer is None or not self.jia_button_timer.isActive():
            self.jia_button_timer = QtCore.QTimer(self)
            self.jia_button_timer.setSingleShot(True)
            self.jia_button_timer.start(300)

            text, ok = QtWidgets.QInputDialog.getInt(self, "充值宝石", "请输入要充值的宝石数量:", 0, 0, 1000000)

            if ok:
                self.update_gemstone_data(text)
                self.enable_buttons()

    def update_gemstone_data(self, amount):
        try:
            gemstone_file = '../docs/gemstone.data'
            with open(gemstone_file, 'r', encoding='utf-8') as file:
                gemstone_value = int(file.read().strip())

            new_gemstone_value = gemstone_value + amount

            with open(gemstone_file, 'w', encoding='utf-8') as file:
                file.write(str(new_gemstone_value))

            self.gemstone.setText(str(new_gemstone_value))

        except Exception as e:
            print(f"更新 gemstone 数据时出错: {e}")

    def show_characters(self):
        try:
            ihave_file = '../docs/ihave.data'
            with open(ihave_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()[2:]  # 去掉前两行
                characters = ''.join(lines)  # 将剩余角色拼接为一个字符串

            # 创建一个对话框来显示角色
            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle("角色列表")
            dialog.setGeometry(100, 100, 400, 300)  # 设置对话框的大小

            # 创建一个文本框并设置角色文本
            text_edit = QtWidgets.QTextEdit(dialog)
            text_edit.setText(characters)
            text_edit.setReadOnly(True)  # 设置为只读
            text_edit.setGeometry(10, 10, 380, 280)  # 设置文本框的大小

            # 显示对话框
            dialog.exec_()

        except Exception as e:
            print(f"读取 ihave 文件时出错: {e}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
