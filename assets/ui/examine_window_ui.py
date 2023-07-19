# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examine_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_examine_window(object):
    def setupUi(self, examine_window):
        if not examine_window.objectName():
            examine_window.setObjectName(u"examine_window")
        examine_window.resize(825, 532)
        icon = QIcon()
        icon.addFile(u"assets/icons/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        examine_window.setWindowIcon(icon)
        self.setting_action = QAction(examine_window)
        self.setting_action.setObjectName(u"setting_action")
        self.return_home_action = QAction(examine_window)
        self.return_home_action.setObjectName(u"return_home_action")
        self.quit_action = QAction(examine_window)
        self.quit_action.setObjectName(u"quit_action")
        self.about_app_action = QAction(examine_window)
        self.about_app_action.setObjectName(u"about_app_action")
        self.check_update = QAction(examine_window)
        self.check_update.setObjectName(u"check_update")
        self.donate_action = QAction(examine_window)
        self.donate_action.setObjectName(u"donate_action")
        self.app_version_action = QAction(examine_window)
        self.app_version_action.setObjectName(u"app_version_action")
        self.centralwidget = QWidget(examine_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.question_order = QSpinBox(self.widget)
        self.question_order.setObjectName(u"question_order")
        self.question_order.setReadOnly(False)
        self.question_order.setMinimum(1)
        self.question_order.setMaximum(25)

        self.horizontalLayout.addWidget(self.question_order)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.clock_minute = QLCDNumber(self.widget)
        self.clock_minute.setObjectName(u"clock_minute")
        self.clock_minute.setMinimumSize(QSize(0, 30))
        self.clock_minute.setMaximumSize(QSize(16777215, 30))
        self.clock_minute.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.clock_minute)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.clock_second = QLCDNumber(self.widget)
        self.clock_second.setObjectName(u"clock_second")
        self.clock_second.setMinimumSize(QSize(0, 30))
        self.clock_second.setMaximumSize(QSize(16777215, 30))
        self.clock_second.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.clock_second)


        self.verticalLayout_5.addWidget(self.widget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.question = QLabel(self.frame)
        self.question.setObjectName(u"question")

        self.verticalLayout.addWidget(self.question)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.image_question = QLabel(self.frame)
        self.image_question.setObjectName(u"image_question")

        self.horizontalLayout_2.addWidget(self.image_question)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.first_answer = QRadioButton(self.groupBox)
        self.first_answer.setObjectName(u"first_answer")

        self.verticalLayout_2.addWidget(self.first_answer)

        self.second_answer = QRadioButton(self.groupBox)
        self.second_answer.setObjectName(u"second_answer")

        self.verticalLayout_2.addWidget(self.second_answer)

        self.third_answer = QRadioButton(self.groupBox)
        self.third_answer.setObjectName(u"third_answer")

        self.verticalLayout_2.addWidget(self.third_answer)

        self.fourth_answer = QRadioButton(self.groupBox)
        self.fourth_answer.setObjectName(u"fourth_answer")

        self.verticalLayout_2.addWidget(self.fourth_answer)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.previous_question = QPushButton(self.frame)
        self.previous_question.setObjectName(u"previous_question")
        icon1 = QIcon()
        icon1.addFile(u"../icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_question.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.previous_question)

        self.submit = QPushButton(self.frame)
        self.submit.setObjectName(u"submit")
        icon2 = QIcon()
        icon2.addFile(u"../icons/submit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.submit.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.submit)

        self.next_question = QPushButton(self.frame)
        self.next_question.setObjectName(u"next_question")
        icon3 = QIcon()
        icon3.addFile(u"../icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_question.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.next_question)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.frame)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(310, 280))
        self.widget_3.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.groupBox_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.not_answer_question = QLabel(self.widget_2)
        self.not_answer_question.setObjectName(u"not_answer_question")
        self.not_answer_question.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.not_answer_question)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.question_13 = QPushButton(self.groupBox_2)
        self.question_13.setObjectName(u"question_13")

        self.gridLayout.addWidget(self.question_13, 2, 2, 1, 1)

        self.question_12 = QPushButton(self.groupBox_2)
        self.question_12.setObjectName(u"question_12")

        self.gridLayout.addWidget(self.question_12, 2, 1, 1, 1)

        self.question_8 = QPushButton(self.groupBox_2)
        self.question_8.setObjectName(u"question_8")

        self.gridLayout.addWidget(self.question_8, 1, 2, 1, 1)

        self.question_19 = QPushButton(self.groupBox_2)
        self.question_19.setObjectName(u"question_19")

        self.gridLayout.addWidget(self.question_19, 3, 3, 1, 1)

        self.question_10 = QPushButton(self.groupBox_2)
        self.question_10.setObjectName(u"question_10")

        self.gridLayout.addWidget(self.question_10, 1, 4, 1, 1)

        self.question_9 = QPushButton(self.groupBox_2)
        self.question_9.setObjectName(u"question_9")

        self.gridLayout.addWidget(self.question_9, 1, 3, 1, 1)

        self.question_4 = QPushButton(self.groupBox_2)
        self.question_4.setObjectName(u"question_4")

        self.gridLayout.addWidget(self.question_4, 0, 3, 1, 1)

        self.question_7 = QPushButton(self.groupBox_2)
        self.question_7.setObjectName(u"question_7")

        self.gridLayout.addWidget(self.question_7, 1, 1, 1, 1)

        self.question_16 = QPushButton(self.groupBox_2)
        self.question_16.setObjectName(u"question_16")

        self.gridLayout.addWidget(self.question_16, 3, 0, 1, 1)

        self.question_5 = QPushButton(self.groupBox_2)
        self.question_5.setObjectName(u"question_5")

        self.gridLayout.addWidget(self.question_5, 0, 4, 1, 1)

        self.question_17 = QPushButton(self.groupBox_2)
        self.question_17.setObjectName(u"question_17")

        self.gridLayout.addWidget(self.question_17, 3, 1, 1, 1)

        self.question_18 = QPushButton(self.groupBox_2)
        self.question_18.setObjectName(u"question_18")

        self.gridLayout.addWidget(self.question_18, 3, 2, 1, 1)

        self.question_6 = QPushButton(self.groupBox_2)
        self.question_6.setObjectName(u"question_6")

        self.gridLayout.addWidget(self.question_6, 1, 0, 1, 1)

        self.question_11 = QPushButton(self.groupBox_2)
        self.question_11.setObjectName(u"question_11")

        self.gridLayout.addWidget(self.question_11, 2, 0, 1, 1)

        self.question_14 = QPushButton(self.groupBox_2)
        self.question_14.setObjectName(u"question_14")

        self.gridLayout.addWidget(self.question_14, 2, 3, 1, 1)

        self.question_1 = QPushButton(self.groupBox_2)
        self.question_1.setObjectName(u"question_1")

        self.gridLayout.addWidget(self.question_1, 0, 0, 1, 1)

        self.question_3 = QPushButton(self.groupBox_2)
        self.question_3.setObjectName(u"question_3")

        self.gridLayout.addWidget(self.question_3, 0, 2, 1, 1)

        self.question_20 = QPushButton(self.groupBox_2)
        self.question_20.setObjectName(u"question_20")

        self.gridLayout.addWidget(self.question_20, 3, 4, 1, 1)

        self.question_2 = QPushButton(self.groupBox_2)
        self.question_2.setObjectName(u"question_2")

        self.gridLayout.addWidget(self.question_2, 0, 1, 1, 1)

        self.question_15 = QPushButton(self.groupBox_2)
        self.question_15.setObjectName(u"question_15")

        self.gridLayout.addWidget(self.question_15, 2, 4, 1, 1)

        self.question_21 = QPushButton(self.groupBox_2)
        self.question_21.setObjectName(u"question_21")

        self.gridLayout.addWidget(self.question_21, 4, 0, 1, 1)

        self.question_22 = QPushButton(self.groupBox_2)
        self.question_22.setObjectName(u"question_22")

        self.gridLayout.addWidget(self.question_22, 4, 1, 1, 1)

        self.question_23 = QPushButton(self.groupBox_2)
        self.question_23.setObjectName(u"question_23")

        self.gridLayout.addWidget(self.question_23, 4, 2, 1, 1)

        self.question_24 = QPushButton(self.groupBox_2)
        self.question_24.setObjectName(u"question_24")

        self.gridLayout.addWidget(self.question_24, 4, 3, 1, 1)

        self.question_25 = QPushButton(self.groupBox_2)
        self.question_25.setObjectName(u"question_25")

        self.gridLayout.addWidget(self.question_25, 4, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.widget_3)

        examine_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(examine_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 825, 22))
        self.menuCh_c_n_ng = QMenu(self.menubar)
        self.menuCh_c_n_ng.setObjectName(u"menuCh_c_n_ng")
        self.menuTh_ng_tin = QMenu(self.menubar)
        self.menuTh_ng_tin.setObjectName(u"menuTh_ng_tin")
        examine_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(examine_window)
        self.statusbar.setObjectName(u"statusbar")
        examine_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCh_c_n_ng.menuAction())
        self.menubar.addAction(self.menuTh_ng_tin.menuAction())
        self.menuCh_c_n_ng.addAction(self.setting_action)
        self.menuCh_c_n_ng.addAction(self.return_home_action)
        self.menuCh_c_n_ng.addAction(self.quit_action)
        self.menuTh_ng_tin.addAction(self.about_app_action)
        self.menuTh_ng_tin.addAction(self.check_update)
        self.menuTh_ng_tin.addAction(self.app_version_action)
        self.menuTh_ng_tin.addAction(self.donate_action)

        self.retranslateUi(examine_window)

        QMetaObject.connectSlotsByName(examine_window)
    # setupUi

    def retranslateUi(self, examine_window):
        examine_window.setWindowTitle(QCoreApplication.translate("examine_window", u"S\u00e1t h\u1ea1ch l\u00e1i xe b\u1eb1ng A1", None))
        self.setting_action.setText(QCoreApplication.translate("examine_window", u"C\u00e0i \u0111\u1eb7t", None))
        self.return_home_action.setText(QCoreApplication.translate("examine_window", u"Tr\u1edf v\u1ec1 m\u00e0n h\u00ecnh ch\u00ednh", None))
        self.quit_action.setText(QCoreApplication.translate("examine_window", u"Tho\u00e1t ch\u01b0\u01a1ng tr\u00ecnh", None))
        self.about_app_action.setText(QCoreApplication.translate("examine_window", u"V\u1ec1 \u1ee9ng d\u1ee5ng n\u00e0y", None))
        self.check_update.setText(QCoreApplication.translate("examine_window", u"Ki\u1ec3m tra c\u1eadp nh\u1eadt", None))
        self.donate_action.setText(QCoreApplication.translate("examine_window", u"Gi\u00fap \u0111\u1ee1 t\u00e1c gi\u1ea3", None))
        self.app_version_action.setText(QCoreApplication.translate("examine_window", u"Th\u00f4ng tin phi\u00ean b\u1ea3n", None))
        self.label.setText(QCoreApplication.translate("examine_window", u"B\u1ea1n \u0111ang l\u00e0m c\u00e2u", None))
        self.label_2.setText(QCoreApplication.translate("examine_window", u"Th\u1eddi gian c\u00f2n l\u1ea1i:", None))
        self.label_3.setText(QCoreApplication.translate("examine_window", u":", None))
        self.question.setText(QCoreApplication.translate("examine_window", u"C\u00e2u h\u1ecfi", None))
        self.image_question.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("examine_window", u"\u0110\u00e1p \u00e1n", None))
        self.first_answer.setText(QCoreApplication.translate("examine_window", u"A", None))
        self.second_answer.setText(QCoreApplication.translate("examine_window", u"B", None))
        self.third_answer.setText(QCoreApplication.translate("examine_window", u"C", None))
        self.fourth_answer.setText(QCoreApplication.translate("examine_window", u"D", None))
#if QT_CONFIG(tooltip)
        self.previous_question.setToolTip(QCoreApplication.translate("examine_window", u"C\u00e2u tr\u01b0\u1edbc \u0111\u00f3", None))
#endif // QT_CONFIG(tooltip)
        self.previous_question.setText(QCoreApplication.translate("examine_window", u"C\u00e2u tr\u01b0\u1edbc", None))
#if QT_CONFIG(tooltip)
        self.submit.setToolTip(QCoreApplication.translate("examine_window", u"K\u1ebft th\u00fac l\u00e0m b\u00e0i v\u00e0 n\u1ed9p b\u00e0i", None))
#endif // QT_CONFIG(tooltip)
        self.submit.setText(QCoreApplication.translate("examine_window", u"N\u1ed9p b\u00e0i", None))
#if QT_CONFIG(tooltip)
        self.next_question.setToolTip(QCoreApplication.translate("examine_window", u"C\u00e2u ti\u1ebfp theo", None))
#endif // QT_CONFIG(tooltip)
        self.next_question.setText(QCoreApplication.translate("examine_window", u"C\u00e2u ti\u1ebfp", None))
        self.label_4.setText(QCoreApplication.translate("examine_window", u"<html><head/><body><p><span style=\" font-weight:700;\">L\u01b0u \u00fd</span>: C\u00e1c c\u00e2u tr\u1ea3 l\u1eddi r\u1ed3i s\u1ebd hi\u1ec3n th\u1ecb m\u00e0u xanh l\u00e1.<br/>C\u00e1c c\u00e2u ch\u01b0a ho\u00e0n th\u00e0nh s\u1ebd hi\u1ec3n th\u1ecb m\u00e0u \u0111en.</p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("examine_window", u"C\u00e1c c\u00e2u h\u1ecfi", None))
        self.label_5.setText(QCoreApplication.translate("examine_window", u"B\u1ea1n c\u00f2n", None))
        self.not_answer_question.setText(QCoreApplication.translate("examine_window", u"25", None))
        self.label_6.setText(QCoreApplication.translate("examine_window", u"c\u00e2u ch\u01b0a ho\u00e0n th\u00e0nh", None))
        self.question_13.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 13", None))
        self.question_12.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 12", None))
        self.question_8.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 8", None))
        self.question_19.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 19", None))
        self.question_10.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 10", None))
        self.question_9.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 9", None))
        self.question_4.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 4", None))
        self.question_7.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 7", None))
        self.question_16.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 16", None))
        self.question_5.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 5", None))
        self.question_17.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 17", None))
        self.question_18.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 18", None))
        self.question_6.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 6", None))
        self.question_11.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 11", None))
        self.question_14.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 14", None))
        self.question_1.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 1", None))
        self.question_3.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 3", None))
        self.question_20.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 20", None))
        self.question_2.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 2", None))
        self.question_15.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 15", None))
        self.question_21.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 21", None))
        self.question_22.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 22", None))
        self.question_23.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 23", None))
        self.question_24.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 24", None))
        self.question_25.setText(QCoreApplication.translate("examine_window", u"C\u00e2u 25", None))
        self.menuCh_c_n_ng.setTitle(QCoreApplication.translate("examine_window", u"Ch\u1ee9c n\u0103ng", None))
        self.menuTh_ng_tin.setTitle(QCoreApplication.translate("examine_window", u"Th\u00f4ng tin", None))
    # retranslateUi

