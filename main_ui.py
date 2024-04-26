# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollBar,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 772)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(12)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.main_path = QLineEdit(self.frame)
        self.main_path.setObjectName(u"main_path")
        self.main_path.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.main_path)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_4)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.frame1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)


        self.verticalLayout_10.addWidget(self.frame1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame2 = QFrame(self.groupBox)
        self.frame2.setObjectName(u"frame2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.frame2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_12 = QLineEdit(self.frame2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.lineEdit_12.setFont(font1)
        self.lineEdit_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_12)

        self.center = QDoubleSpinBox(self.frame2)
        self.center.setObjectName(u"center")
        self.center.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(10)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.center.sizePolicy().hasHeightForWidth())
        self.center.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.center.setFont(font2)
        self.center.setStyleSheet(u"")
        self.center.setWrapping(False)
        self.center.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.center.setDecimals(0)
        self.center.setMinimum(-250.000000000000000)
        self.center.setMaximum(250.000000000000000)
        self.center.setValue(0.000000000000000)

        self.horizontalLayout_10.addWidget(self.center)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_8 = QLineEdit(self.frame2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setFont(font1)
        self.lineEdit_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_8)

        self.width = QDoubleSpinBox(self.frame2)
        self.width.setObjectName(u"width")
        sizePolicy4.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy4)
        self.width.setFont(font2)
        self.width.setStyleSheet(u"")
        self.width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.width.setDecimals(0)
        self.width.setMinimum(1.000000000000000)
        self.width.setValue(30.000000000000000)

        self.horizontalLayout_11.addWidget(self.width)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_9 = QLineEdit(self.frame2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy5)
        self.lineEdit_9.setFont(font1)
        self.lineEdit_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_9)

        self.height = QDoubleSpinBox(self.frame2)
        self.height.setObjectName(u"height")
        sizePolicy4.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy4)
        self.height.setFont(font2)
        self.height.setStyleSheet(u"")
        self.height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.height.setDecimals(0)
        self.height.setMinimum(10.000000000000000)
        self.height.setMaximum(500.000000000000000)
        self.height.setValue(300.000000000000000)

        self.horizontalLayout_12.addWidget(self.height)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_10 = QLineEdit(self.frame2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy5.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy5)
        self.lineEdit_10.setFont(font1)
        self.lineEdit_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_10)

        self.smooth_n = QDoubleSpinBox(self.frame2)
        self.smooth_n.setObjectName(u"smooth_n")
        sizePolicy4.setHeightForWidth(self.smooth_n.sizePolicy().hasHeightForWidth())
        self.smooth_n.setSizePolicy(sizePolicy4)
        self.smooth_n.setFont(font2)
        self.smooth_n.setStyleSheet(u"")
        self.smooth_n.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.smooth_n.setDecimals(0)
        self.smooth_n.setMinimum(1.000000000000000)
        self.smooth_n.setMaximum(31.000000000000000)
        self.smooth_n.setSingleStep(2.000000000000000)
        self.smooth_n.setValue(5.000000000000000)

        self.horizontalLayout_13.addWidget(self.smooth_n)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)


        self.horizontalLayout.addWidget(self.frame2)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_11 = QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font1)
        self.lineEdit_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: None")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_11)

        self.top_num = QLineEdit(self.layoutWidget)
        self.top_num.setObjectName(u"top_num")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        self.top_num.setFont(font3)
        self.top_num.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_4.addWidget(self.top_num)

        self.splitter.addWidget(self.layoutWidget)
        self.verticalScrollBar_top = QScrollBar(self.splitter)
        self.verticalScrollBar_top.setObjectName(u"verticalScrollBar_top")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.verticalScrollBar_top.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar_top.setSizePolicy(sizePolicy6)
        self.verticalScrollBar_top.setMaximumSize(QSize(135, 201))
        self.verticalScrollBar_top.setStyleSheet(u"border: None")
        self.verticalScrollBar_top.setMinimum(0)
        self.verticalScrollBar_top.setMaximum(150)
        self.verticalScrollBar_top.setValue(0)
        self.verticalScrollBar_top.setOrientation(Qt.Vertical)
        self.splitter.addWidget(self.verticalScrollBar_top)

        self.horizontalLayout.addWidget(self.splitter)


        self.verticalLayout_10.addWidget(self.groupBox)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.appprox_dataframe = QFrame(self.frame)
        self.appprox_dataframe.setObjectName(u"appprox_dataframe")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.appprox_dataframe.sizePolicy().hasHeightForWidth())
        self.appprox_dataframe.setSizePolicy(sizePolicy7)
        self.verticalLayout_9 = QVBoxLayout(self.appprox_dataframe)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.appprox_dataframe)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"Noto Sans"])
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_11 = QLabel(self.appprox_dataframe)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.label_12 = QLabel(self.appprox_dataframe)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_12)


        self.horizontalLayout_7.addWidget(self.appprox_dataframe)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy8)
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.approx_y0 = QLabel(self.widget)
        self.approx_y0.setObjectName(u"approx_y0")
        sizePolicy7.setHeightForWidth(self.approx_y0.sizePolicy().hasHeightForWidth())
        self.approx_y0.setSizePolicy(sizePolicy7)
        self.approx_y0.setFont(font3)
        self.approx_y0.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.approx_y0)

        self.approx_mt = QLabel(self.widget)
        self.approx_mt.setObjectName(u"approx_mt")
        self.approx_mt.setFont(font3)
        self.approx_mt.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.approx_mt)

        self.approx_A = QLabel(self.widget)
        self.approx_A.setObjectName(u"approx_A")
        self.approx_A.setFont(font3)
        self.approx_A.setStyleSheet(u"border: none\n"
"")

        self.verticalLayout_8.addWidget(self.approx_A)


        self.horizontalLayout_7.addWidget(self.widget)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.pushButton_save_val = QPushButton(self.frame)
        self.pushButton_save_val.setObjectName(u"pushButton_save_val")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_save_val.sizePolicy().hasHeightForWidth())
        self.pushButton_save_val.setSizePolicy(sizePolicy9)
        font5 = QFont()
        font5.setFamilies([u"Noto Sans"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.pushButton_save_val.setFont(font5)
        self.pushButton_save_val.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pushButton_save_val)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.path_for_save = QLineEdit(self.frame)
        self.path_for_save.setObjectName(u"path_for_save")
        self.path_for_save.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_5.addWidget(self.path_for_save)

        self.pushButton_save_massive = QPushButton(self.frame)
        self.pushButton_save_massive.setObjectName(u"pushButton_save_massive")
        self.pushButton_save_massive.setFont(font5)
        self.pushButton_save_massive.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.pushButton_save_massive)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_theme = QComboBox(self.frame)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        self.comboBox_theme.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.comboBox_theme)

        self.pushButton_clear_massive = QPushButton(self.frame)
        self.pushButton_clear_massive.setObjectName(u"pushButton_clear_massive")
        self.pushButton_clear_massive.setFont(font5)
        self.pushButton_clear_massive.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_clear_massive)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_9.addWidget(self.frame)

        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.verticalLayout_11 = QVBoxLayout(self.frame3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ffwidget_plot = QWidget(self.frame3)
        self.ffwidget_plot.setObjectName(u"ffwidget_plot")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(7)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.ffwidget_plot.sizePolicy().hasHeightForWidth())
        self.ffwidget_plot.setSizePolicy(sizePolicy10)

        self.verticalLayout_11.addWidget(self.ffwidget_plot)

        self.comment_for_person = QLabel(self.frame3)
        self.comment_for_person.setObjectName(u"comment_for_person")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.comment_for_person.sizePolicy().hasHeightForWidth())
        self.comment_for_person.setSizePolicy(sizePolicy11)
        self.comment_for_person.setFont(font3)
        self.comment_for_person.setStyleSheet(u"border: none\n"
"")
        self.comment_for_person.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.comment_for_person)


        self.horizontalLayout_9.addWidget(self.frame3)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCT imaging system OCP930SR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.main_path.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"N(smooth)", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"Top", None))
#if QT_CONFIG(whatsthis)
        self.top_num.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043e\u043a\u043d\u0430</p><p><span style=\" text-decoration: underline;\">\u0430\u0430\u0430</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.top_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0430\u043f\u043f\u0440\u043e\u043a\u0438\u043c\u0430\u0446\u0438\u0438</span></p><p>y = y<span style=\" vertical-align:sub;\">0 </span>+A*e<span style=\" vertical-align:super;\">-z*\u03bc</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>y<span style=\" vertical-align:sub;\">0 </span>=</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u03bc<span style=\" vertical-align:sub;\">t </span>=</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>A =</p></body></html>", None))
        self.approx_y0.setText(QCoreApplication.translate("MainWindow", u"_____________", None))
        self.approx_mt.setText(QCoreApplication.translate("MainWindow", u"_____________", None))
        self.approx_A.setText(QCoreApplication.translate("MainWindow", u"_____________", None))
        self.pushButton_save_val.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.path_for_save.setText("")
        self.pushButton_save_massive.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u0430\u0441\u0441\u0438\u0432", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))

        self.pushButton_clear_massive.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043c\u0430\u0441\u0441\u0438\u0432", None))
        self.comment_for_person.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0433\u043e \u043a\u043e\u0434\u0430 \u043d\u0430 Mathcad: \u0411\u0430\u0448\u043a\u0430\u0442\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432\u0438\u0447 \u0438 \u0413\u0435\u043d\u0438\u043d\u0430 \u042d\u043b\u0438\u043d\u0430 \u0410\u043b\u0435\u043a\u0441\u0435\u0435\u0432\u043d\u0430. \u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a GUI: \u0415\u0440\u043c\u043e\u043b\u0438\u043d\u0441\u043a\u0438\u0439 \u041f\u0435\u0442\u0440 \u0411\u043e\u0440\u0438\u0441\u043e\u0432\u0438\u0447.", None))
    # retranslateUi

