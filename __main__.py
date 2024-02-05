from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from views_mangers.main_manger import MainManager
from views_mangers.login_manger import LoginManager

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import requests


class User_Analyser(QtWidgets.QStackedWidget):
    def __init__(self):
        super(User_Analyser, self).__init__()
        self.resize(800, 650)
        # self.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/birdt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "User Analyzer "))

        self.main_manager = MainManager()
        self.login_manager = LoginManager()

        self.check_internet_connection()
        # self.handle_login()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.login_manager)  # 0
        self.addWidget(self.main_manager)  # 1

        # install signals
        self.login_manager.loginAcceptedSignal.connect(self.handle_login)

        # main screen
        # self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda: self.setCurrentIndex(1))

    def handle_login(self, token, first_name):
        self.main_manager.token = token
        self.main_manager.first_name = first_name
        self.setCurrentIndex(1)

    def check_internet_connection(self):
        manager = QNetworkAccessManager(self)
        request = QNetworkRequest(QUrl("http://www.google.com"))

        def handle_reply(reply):
            if not reply.error() == QNetworkReply.NoError:
                self.show_no_internet_message()

        manager.finished.connect(handle_reply)
        manager.get(request)

    def show_login_failed_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Login Failed Please Contact Abdel-Rahman.")
        msg.setWindowTitle("Connection Error")
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msg.buttonClicked.connect(self.handle_message_box_button)
        msg.exec_()

    def show_no_internet_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("No internet connection.")
        msg.setWindowTitle("Connection Error")
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msg.buttonClicked.connect(self.handle_message_box_button)
        msg.exec_()

    def handle_message_box_button(self, button):
        if button.text() == "Retry":
            self.check_internet_connection()
        elif button.text() == "Close":
            sys.exit()
            # self.close()


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = User_Analyser()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
