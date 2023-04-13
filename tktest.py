#!/bin/env python3
import sys

from PySide6.QtCore import Qt, Signal, Slot, QThread, QRect, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QStyle, QTextEdit, QMessageBox

import sys
from untitled import Ui_Form


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r', encoding='UTF-8') as file:
            return file.read()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    # style_file = './index.qss'
    # style_sheet = QSSLoader.read_qss_file(style_file)
    # main.setStyleSheet(style_sheet)
    main.show()
    sys.exit(app.exec())
