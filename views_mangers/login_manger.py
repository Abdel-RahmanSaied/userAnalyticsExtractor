from PyQt5 import QtWidgets, QtCore
from views import login_view
import json
import requests
import os


class LoginManager(QtWidgets.QWidget, login_view.Ui_login_Form):
    loginAcceptedSignal = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super(LoginManager, self).__init__()
        self.setupUi(self)

        self.login_btn.clicked.connect(self.handle_login)
        self.base_url = "https://api.twiscope.net/api/auth/login/"

    def handle_login(self):
        msg = QtWidgets.QMessageBox()
        username = self.username_lin.text()
        password = self.password_lin.text()
        if len(username) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif len(password) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        else:
            data = {
                "username": username,
                "password": password
            }
            try:
                user_check = requests.post(self.base_url, data=data)
                json_response = user_check.json()
                json_statusCode = user_check.status_code
            except (requests.ConnectionError, requests.Timeout) as exception:
                print(exception)
                msg.setWindowTitle("Warning")
                msg.setText("No internet connection.")
                msg.exec_()
            except Exception as error:
                print(error)
            try:
                if json_statusCode == 200:
                    userToken = json_response['token']
                    user = json_response.get('user')
                    first_name = user.get("first_name")
                    self.loginAcceptedSignal.emit(userToken, first_name)

                elif json_statusCode == 400:
                    msg.setWindowTitle("Warning")
                    msg.setText("username or password was incorrect")
                    msg.exec_()
                else:
                    msg.setWindowTitle("Warning")
                    msg.setText(str(json_response['detail']))
                    msg.exec_()

            except Exception as x:
                msg.setWindowTitle("Warning")
                msg.setText(str(x))
                msg.exec_()

    def clear(self):
        self.username_lin.setText("")
        self.password_lin.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = LoginManager()
    w.show()
    app.exec_()
