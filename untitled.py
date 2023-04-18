# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 900)
        Form.setMinimumSize(QSize(1440, 900))
        Form.setMaximumSize(QSize(1440, 900))
        Form.setStyleSheet(u"#Form{\n"
"background: rgba(26, 28, 41, 1);\n"
"}")
        self.meun_box = QWidget(Form)
        self.meun_box.setObjectName(u"meun_box")
        self.meun_box.setGeometry(QRect(0, 0, 234, 900))
        self.meun_box.setMinimumSize(QSize(0, 0))
        self.meun_box.setMaximumSize(QSize(234, 900))
        self.meun_box.setStyleSheet(u"#meun_box{\n"
"background: rgba(42, 43, 61, 1);\n"
"}")
        self.layoutWidget = QWidget(self.meun_box)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 100, 176, 147))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.meun_button = QPushButton(self.layoutWidget)
        self.meun_button.setObjectName(u"meun_button")
        self.meun_button.setMinimumSize(QSize(174, 39))
        self.meun_button.setMaximumSize(QSize(174, 39))
        self.meun_button.setStyleSheet(u".QWidget .QPushButton{\n"
"border-radius: 6px;\n"
"background: rgba(91, 133, 253, 1);\n"
"padding: 10px 16px 10px 16px;\n"
"font-size: 16px;\n"
"font-weight: 500;\n"
"color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
".QWidget .QPushButton:hover{\n"
"border-radius: 6px;\n"
"background: rgb(84, 171, 255);\n"
"padding: 10px 16px 10px 16px;\n"
"}")

        self.verticalLayout.addWidget(self.meun_button)

        self.meun_button_2 = QPushButton(self.layoutWidget)
        self.meun_button_2.setObjectName(u"meun_button_2")
        self.meun_button_2.setMinimumSize(QSize(174, 39))
        self.meun_button_2.setMaximumSize(QSize(174, 39))
        self.meun_button_2.setStyleSheet(u".QWidget .QPushButton{\n"
"border-radius: 6px;\n"
"background: rgba(91, 133, 253, 1);\n"
"padding: 10px 16px 10px 16px;\n"
"font-size: 16px;\n"
"font-weight: 500;\n"
"color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
".QWidget .QPushButton:hover{\n"
"border-radius: 6px;\n"
"background: rgb(84, 171, 255);\n"
"padding: 10px 16px 10px 16px;\n"
"}")

        self.verticalLayout.addWidget(self.meun_button_2)

        self.meun_button_3 = QPushButton(self.layoutWidget)
        self.meun_button_3.setObjectName(u"meun_button_3")
        self.meun_button_3.setMinimumSize(QSize(174, 39))
        self.meun_button_3.setMaximumSize(QSize(174, 39))
        self.meun_button_3.setStyleSheet(u".QWidget .QPushButton{\n"
"border-radius: 6px;\n"
"background: rgba(91, 133, 253, 1);\n"
"padding: 10px 16px 10px 16px;\n"
"font-size: 16px;\n"
"font-weight: 500;\n"
"color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
".QWidget .QPushButton:hover{\n"
"border-radius: 6px;\n"
"background: rgb(84, 171, 255);\n"
"padding: 10px 16px 10px 16px;\n"
"}")

        self.verticalLayout.addWidget(self.meun_button_3)

        self.header_box = QWidget(Form)
        self.header_box.setObjectName(u"header_box")
        self.header_box.setGeometry(QRect(0, 0, 1440, 80))
        self.header_box.setMaximumSize(QSize(1440, 80))
        self.header_box.setStyleSheet(u"#header_box{\n"
"background: rgba(42, 43, 61, 1);\n"
"\n"
"}")
        self.header_title = QLabel(self.header_box)
        self.header_title.setObjectName(u"header_title")
        self.header_title.setGeometry(QRect(80, 26, 101, 31))
        self.header_title.setStyleSheet(u"#header_title{\n"
"font-size: 24px;\n"
"font-weight: 700;\n"
"color: rgba(255, 255, 255, 1);\n"
"}")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(270, 110, 1146, 760))
        self.stackedWidget.setStyleSheet(u"")
        self.Jzpage = QWidget()
        self.Jzpage.setObjectName(u"Jzpage")
        self.Jzpage.setStyleSheet(u"#Jzpage{\n"
"border-radius: 16px;\n"
"background: rgba(42, 43, 61, 1);\n"
"}")
        self.tableWidget = QTableWidget(self.Jzpage)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(100, 290, 961, 441))
        self.tableWidget.setStyleSheet(u"background: rgba(26, 28, 41, 1);\n"
"color:rgb(255,255,255);\n"
"font-size:16px")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.pushButton = QPushButton(self.Jzpage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 150, 120, 40))
        self.pushButton.setStyleSheet(u"background: rgb(79, 233, 160);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_2 = QPushButton(self.Jzpage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 210, 120, 40))
        self.pushButton_2.setStyleSheet(u"background: rgb(170, 170, 170);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.layoutWidget1 = QWidget(self.Jzpage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(480, 30, 330, 46))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 40))
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);\n"
"font-size:16px")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.layoutWidget1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(240, 40))
        self.comboBox_2.setStyleSheet(u"background: rgba(26, 28, 41, 1);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.layoutWidget2 = QWidget(self.Jzpage)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(100, 30, 330, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 40))
        self.label.setStyleSheet(u"color:rgb(255,255,255);\n"
"font-size:16px")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(240, 40))
        self.lineEdit.setStyleSheet(u"background: rgba(26, 28, 41, 1);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.layoutWidget3 = QWidget(self.Jzpage)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(100, 80, 330, 46))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 40))
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);\n"
"font-size:16px")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(240, 40))
        self.comboBox.setStyleSheet(u"background: rgba(26, 28, 41, 1);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.layoutWidget4 = QWidget(self.Jzpage)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(480, 80, 330, 46))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 40))
        self.label_4.setStyleSheet(u"color:rgb(255,255,255);\n"
"font-size:16px")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.layoutWidget4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(240, 40))
        self.comboBox_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"padding-left:12px;\n"
"border:1px solid rgb(150, 150, 150);\n"
"color:rgb(255, 255, 255);\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"font-size:18px;\n"
"line-height:14px;\n"
"border-radius:8px;\n"
"background:rgb(26, 28, 41)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"height:30px;\n"
"color:#131313;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"font-size:18px;\n"
"line-height:12px;\n"
"border: 1px solid #FAFAFB;\n"
"} \n"
"\n"
"QComboBox::down-arrow{\n"
"image:url(:/liveClientStudent/Resources/images/down_normal.png);\n"
"} \n"
"\n"
"QComboBox::drop-down{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 33px;\n"
"border-width: 1px;\n"
"padding-left:12px;\n"
"}\n"
"\n"
"QListView::item{\n"
"padding-left:6px;\n"
"}\n"
"\n"
"QListView::item:selected{\n"
"color:#FFFFFF;\n"
"background:rgb(26, 28, 41);\n"
"}")

        self.horizontalLayout_4.addWidget(self.comboBox_3)

        self.layoutWidget5 = QWidget(self.Jzpage)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(100, 140, 373, 122))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 118))
        self.label_5.setBaseSize(QSize(0, 0))
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);\n"
"font-size:16px")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.textEdit = QTextEdit(self.layoutWidget5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(300, 120))
        self.textEdit.setMaximumSize(QSize(300, 120))
        self.textEdit.setStyleSheet(u"background: rgba(26, 28, 41, 1);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px")

        self.horizontalLayout_5.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.Jzpage)
        self.Bbpage = QWidget()
        self.Bbpage.setObjectName(u"Bbpage")
        self.Bbpage.setStyleSheet(u"#Bbpage{\n"
"border-radius: 16px;\n"
"background: rgba(42, 43, 61, 1);\n"
"}")
        self.stackedWidget.addWidget(self.Bbpage)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.meun_button.setText(QCoreApplication.translate("Form", u"\u8bb0\u8d26", None))
        self.meun_button_2.setText(QCoreApplication.translate("Form", u"\u8bb0\u8d26", None))
        self.meun_button_3.setText(QCoreApplication.translate("Form", u"\u8bb0\u8d26", None))
        self.header_title.setText(QCoreApplication.translate("Form", u"\u8bb0\u8d26\u8f6f\u4ef6", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u6536/\u652f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u65b9\u5f0f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"1", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u6536\u5165", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u652f\u51fa", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6536\u652f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u6536\u5165", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u652f\u51fa", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u65b9\u5f0f", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u6536\u5165", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u652f\u51fa", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
    # retranslateUi

