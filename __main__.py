from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from views_mangers.main_manger import MainManager

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

        self.check_internet_connection()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager)  # 0

        # # install signals
        # main screen
        # self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda: self.setCurrentIndex(1))

    def handle_login(self):
        data = {"username": "searchUser",
                "password": "searchUser123"}
        response = requests.post("https://api.twiscope.net/api/auth/login", data=data)
        if response.status_code == 200:
            print("Login successful")
            self.main_manager.token = response.json().get("token")

    def check_internet_connection(self):
        manager = QNetworkAccessManager(self)
        request = QNetworkRequest(QUrl("http://www.google.com"))

        def handle_reply(reply):
            if not reply.error() == QNetworkReply.NoError:
                self.show_no_internet_message()

        manager.finished.connect(handle_reply)
        manager.get(request)

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
            self.close()


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = User_Analyser()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
