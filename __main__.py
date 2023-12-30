from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from views_mangers.main_manger import MainManager


class User_Analyser(QtWidgets.QStackedWidget):
    def __init__(self):
        super(User_Analyser, self).__init__()
        self.resize(800, 650)
        # self.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/birdt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "User Analyzer "))

        self.main_manager = MainManager()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager)  # 0

        # # install signals
        # main screen
        # self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda: self.setCurrentIndex(1))

    # def about_me(self):
    #     try:
    #         msg = QtWidgets.QMessageBox()
    #         icon = QtGui.QIcon()
    #         icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         msg.setWindowIcon(icon)
    #         msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
    #
    #         msg.setWindowTitle(" About Us ")
    #         msg.setText(" Developed by : Abdel-Rahman Saied \n  Email : abdelrahmansaied080@gmail.com")
    #         msg.setIcon(QMessageBox.Information)
    #         msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
    #         msg.exec_()
    #     except Exception as e:
    #         print(e)


if __name__ == "__main__":
    # import qdarkstyle

    app = QtWidgets.QApplication([])
    w = User_Analyser()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
