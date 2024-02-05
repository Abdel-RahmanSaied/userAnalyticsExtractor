# from PyQt5 import QtWidgets, QtCore, QtGui
#
#
# class WaitingScreen(QtWidgets.QWidget):
#     def __init__(self):
#         super(WaitingScreen, self).__init__()
#         self.setWindowTitle("Waiting Screen")
#         self.resize(300, 200)
#         self.progress_dialog = QtWidgets.QProgressDialog(self)
#         self.progress_dialog.setCancelButton(None)
#         self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
#         self.progress_dialog.setWindowTitle("Please Wait...")
#         self.progress_dialog.setLabelText("Processing...")
#         self.progress_dialog.setRange(0, 0)  # Indeterminate progress
#
#     def show(self):
#         self.centerOnScreen()
#         self.progress_dialog.show()
#
#     def close(self):
#         self.progress_dialog.close()
#
#     def centerOnScreen(self):
#         desktop = QtWidgets.QApplication.desktop()
#         screen_rect = desktop.availableGeometry(self)
#         self.move(screen_rect.center() - self.rect().center())
from PyQt5 import QtWidgets, QtCore

class WaitingScreen(QtWidgets.QProgressDialog):
    def __init__(self):
        super(WaitingScreen, self).__init__()
        self.setWindowTitle("Please Wait...")
        self.setLabelText("Processing...")
        self.setCancelButton(None)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setRange(0, 0)  # Indeterminate progress
        self.centerOnScreen()

    def centerOnScreen(self):
        desktop = QtWidgets.QApplication.desktop()
        screen_rect = desktop.screenGeometry(self)
        center_point = screen_rect.center()
        self.move(center_point.x() - self.width() // 2, center_point.y() - self.height() // 2)
