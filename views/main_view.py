# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 945)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("")
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 9, 1, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 4, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 59, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_6.addItem(spacerItem4, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 5, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 4, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("font-size:25px;\n"
"color: rgb(255, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 8, 1, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 7, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-weight:Bold;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setMinimumSize(QtCore.QSize(900, 0))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem9, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 3, 0, 1, 1)
        self.selectExpPath_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.selectExpPath_btn.setMinimumSize(QtCore.QSize(297, 0))
        self.selectExpPath_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/touchscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectExpPath_btn.setIcon(icon)
        self.selectExpPath_btn.setObjectName("selectExpPath_btn")
        self.gridLayout_3.addWidget(self.selectExpPath_btn, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 3, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 4, 1, 1, 1)
        self.exp_path_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.exp_path_lbl.setMinimumSize(QtCore.QSize(270, 0))
        self.exp_path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.exp_path_lbl.setObjectName("exp_path_lbl")
        self.gridLayout_3.addWidget(self.exp_path_lbl, 5, 0, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 6, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem14 = QtWidgets.QSpacerItem(17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(285, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem15, 2, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 3, 0, 1, 1)
        self.selectSrcPath_btn = QtWidgets.QPushButton(self.groupBox)
        self.selectSrcPath_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.selectSrcPath_btn.setIcon(icon)
        self.selectSrcPath_btn.setObjectName("selectSrcPath_btn")
        self.gridLayout.addWidget(self.selectSrcPath_btn, 3, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 3, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 4, 1, 1, 1)
        self.src_path_lbl = QtWidgets.QLabel(self.groupBox)
        self.src_path_lbl.setMinimumSize(QtCore.QSize(500, 0))
        self.src_path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.src_path_lbl.setObjectName("src_path_lbl")
        self.gridLayout.addWidget(self.src_path_lbl, 5, 0, 1, 3)
        spacerItem19 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 2, 1, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 139, 152,0);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.current_user_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.current_user_lbl.setMaximumSize(QtCore.QSize(901, 650))
        self.current_user_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.current_user_lbl.setObjectName("current_user_lbl")
        self.gridLayout_7.addWidget(self.current_user_lbl, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem20, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 6, 1, 1, 3)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setMinimumSize(QtCore.QSize(297, 50))
        self.start_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.start_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(20,  190, 120);\n"
"font: 22pt \".AppleSystemUIFont\";\n"
" border-radius: 9px;\n"
"")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_6.addWidget(self.start_btn, 4, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "سيب البرنامج يشتغل براحته و متجيش جمبه الله يباركلك، لو في مشكله هو هيقولك لوحده :)"))
        self.label_2.setText(_translate("Form", "Twitter User Analyzer"))
        self.groupBox_2.setTitle(_translate("Form", "exported file"))
        self.label_4.setText(_translate("Form", "Select the path to save the files"))
        self.selectExpPath_btn.setText(_translate("Form", "Select"))
        self.exp_path_lbl.setText(_translate("Form", "exported path .........."))
        self.groupBox.setTitle(_translate("Form", "source file"))
        self.label.setText(_translate("Form", "Select source excel file that contain the users"))
        self.selectSrcPath_btn.setText(_translate("Form", "Select"))
        self.src_path_lbl.setText(_translate("Form", "source file path .........."))
        self.current_user_lbl.setText(_translate("Form", "Working on {{ USER NAME }} ......"))
        self.start_btn.setText(_translate("Form", "Start"))
import app_resources_rc
