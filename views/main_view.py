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
        Form.resize(1292, 986)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("QGroupBox {\n"
"    width: 550px;\n"
"    height: 650px;\n"
"    border-radius: 8px;\n"
"    background:rgba(255, 255, 255, 50) ;\n"
"    box-shadow: 2px 2px 10px 1px #63636340;\n"
"    padding:1% 1% 10% 10%;\n"
"    position: static;\n"
"    margin-top: 8%;\n"
"    animation: _ngcontent-gyf-c3_container .7s linear 1 normal;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 18px;\n"
"    padding: 10px 10px 10px 5px;\n"
"    display: block;\n"
"    width: 100%;\n"
"    border: none;\n"
"    border-bottom: 1px solid #757575;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"font-weight: 400;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"QLabel {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"width: 374px;\n"
"height: 41px;\n"
"border-radius: 5px;\n"
"background : #00aced;\n"
"color: #FFF;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"\n"
"}")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
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
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.selectSrcPath_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.selectSrcPath_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.selectSrcPath_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/touchscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectSrcPath_btn.setIcon(icon)
        self.selectSrcPath_btn.setObjectName("selectSrcPath_btn")
        self.gridLayout.addWidget(self.selectSrcPath_btn, 0, 0, 1, 1)
        self.src_path_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.src_path_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.src_path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.src_path_lbl.setObjectName("src_path_lbl")
        self.gridLayout.addWidget(self.src_path_lbl, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selectExpPath_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.selectExpPath_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.selectExpPath_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.selectExpPath_btn.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.selectExpPath_btn.setIcon(icon)
        self.selectExpPath_btn.setObjectName("selectExpPath_btn")
        self.gridLayout_2.addWidget(self.selectExpPath_btn, 0, 0, 1, 1)
        self.exp_path_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.exp_path_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.exp_path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.exp_path_lbl.setObjectName("exp_path_lbl")
        self.gridLayout_2.addWidget(self.exp_path_lbl, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(444, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 5, 0, 1, 1)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setMinimumSize(QtCore.QSize(297, 50))
        self.start_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.start_btn.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"\n"
"width: 374px;\n"
"height: 41px;\n"
"border-radius: 5px;\n"
"background : #00aced;\n"
"color: #FFF;\n"
"font-size: 16px;\n"
"font-weight: 700;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(20,  190, 120);\n"
"font: 22pt \".AppleSystemUIFont\";\n"
" border-radius: 9px;\n"
"\n"
"}\n"
"")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_4.addWidget(self.start_btn, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(443, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem5, 6, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 400))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(501, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 0, 1, 1)
        self.current_user_lbl = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_user_lbl.sizePolicy().hasHeightForWidth())
        self.current_user_lbl.setSizePolicy(sizePolicy)
        self.current_user_lbl.setMaximumSize(QtCore.QSize(901, 50))
        self.current_user_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.current_user_lbl.setObjectName("current_user_lbl")
        self.gridLayout_5.addWidget(self.current_user_lbl, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(503, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox, 7, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("font-size:25px;\n"
"color: rgb(255, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 8, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:400;\">Welcome in</span><span style=\" font-size:36pt;\"/><span style=\" font-size:36pt; color:#0f80ff;\">TwiScope</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "Select source excel file that contain the users"))
        self.selectSrcPath_btn.setText(_translate("Form", "Select"))
        self.src_path_lbl.setText(_translate("Form", "source file path ...."))
        self.groupBox_4.setTitle(_translate("Form", "Select the path to save the files"))
        self.selectExpPath_btn.setText(_translate("Form", "Select"))
        self.exp_path_lbl.setText(_translate("Form", "exported path ..."))
        self.start_btn.setText(_translate("Form", "Start"))
        self.current_user_lbl.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Working on </span><span style=\" font-size:18pt; font-weight:600; color:#0f80ff;\">USER NAME </span></p></body></html>"))
        self.label_7.setText(_translate("Form", "سيب البرنامج يشتغل براحته و متجيش جمبه الله يباركلك، لو في مشكله هو هيقولك لوحده :)"))
import app_resources_rc
