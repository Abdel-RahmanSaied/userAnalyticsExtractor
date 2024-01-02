from PyQt5 import QtWidgets, QtCore, QtGui
from views import main_view
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog, QApplication
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *
import os
import openpyxl

from views_mangers.progressBar import WaitingScreen

import pandas as pd
import json
import requests
from urllib3.exceptions import InsecureRequestWarning

import csv

# Suppress only the InsecureRequestWarning from urllib3 needed for your case
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ApiWorkerSignals(QtCore.QObject):
    current_user = QtCore.pyqtSignal(str)
    msg_exec = QtCore.pyqtSignal(str, str)
    finished = QtCore.pyqtSignal()


class ApiWorker(QtCore.QRunnable):
    def __init__(self, base_url, src_path, exp_path):
        super(ApiWorker, self).__init__()
        self.base_url = base_url
        self.src_path = src_path
        self.exp_path = exp_path
        self.users_data_list = []
        self.params = {"tweet.fields": "public_metrics,referenced_tweets",
                       "start_time": "2023-01-01T00:00:00Z", "end_time": "2024-01-01T00:00:00Z", "max_results": "100"}
        self.headers = {"Authorization": "Token b6d39cc1c56cf18b1a96c2128f0c50c54aa2b0d5e32806f3bd518ac143dfca74"}
        self.signals = ApiWorkerSignals()

    def run(self):
        df = self.handle_df()
        if df is None:
            self.signals.msg_exec.emit("Error", "Can't read the file")
            return False

        users_list = self.handle_users_list(df)
        if not users_list:
            self.signals.msg_exec.emit("Error", "No users found")
            return False

        running_state = self.automate_running(users_list)
        if not running_state:
            self.signals.msg_exec.emit("Success", "Not All users has been finished yet \n Please edit the original "
                                                  "file to keep the users not finished yet \n and run again after 15 "
                                                  "minutes")
        else:
            self.signals.msg_exec.emit("Success", "Successfully Done")

        self.xlsx_writer(self.users_data_list, self.exp_path)
        self.signals.finished.emit()

    def automate_running(self, users_list):
        count = 0
        try:
            for user_name in users_list:
                response = self.handle_user_data_jsonRequest(user_name)
                userJsonData, _ = self.check_response_status(response)
                if not _:
                    print(userJsonData)
                    self.signals.msg_exec.emit("Error",
                                               f"Error in {user_name} : {userJsonData.get('errors').get('errors')}")
                    return False
                user_data = self.get_user_data(userJsonData)
                if not user_data:
                    return False
                    # return False
                self.users_data_list.append(user_data)
                self.signals.current_user.emit(f"{user_name} is done")
                count += 1

            print(count)
            print(len(users_list))
            if count == len(users_list):
                return True
            return False
        except Exception as e:
            print(e)
            self.signals.msg_exec.emit("Error", f"Error in {user_name} : {e}")
            return False

    def handle_df(self):
        src_file_path = self.src_path
        df = pd.read_excel(src_file_path)
        return df

    def handle_users_list(self, df):
        users_list = df.iloc[:, 2].tolist()
        if not users_list:
            return None
        return users_list

    def handle_user_data_jsonRequest(self, user_name):
        params = self.params
        if not user_name:
            return False
        params.update({"username": user_name})
        response = requests.get(url=self.base_url, params=params, headers=self.headers, verify=False)
        return response

    def check_response_status(self, response):
        if response.status_code != 200:
            return response.json(), False
        return response.json(), True

    def get_user_data(self, userJsonData):
        data = userJsonData.get("data")
        name = data.get("user_data").get("name")
        username = data.get("user_data").get("username")
        total_posts = data.get("public_metrics").get("total_results")
        total_engagement = data.get("public_metrics").get("total_engagement")
        user_data = {"name": name, "username": username, "total_posts": total_posts,
                     "total_engagement": total_engagement}
        return user_data

    def xlsx_writer(self, userslists, file_path):
        count = 1
        file_name = os.path.splitext(os.path.basename(self.src_path))[0]
        file_path_to_save = os.path.join(file_path, f"{file_name}_result.xlsx")

        while os.path.exists(file_path_to_save):
            file_path_to_save = os.path.join(file_path, f"{file_name}_result" + str(count) + ".xlsx")
            count += 1

        try:
            # Create a new Excel workbook and add a worksheet
            workbook = openpyxl.Workbook()
            worksheet = workbook.active

            # Specify the column headers
            fieldnames = ['name', 'username', 'total_posts', 'total_engagement']
            worksheet.append(fieldnames)

            # Write the data to the Excel file
            for user_data_row in userslists:
                row_data = [user_data_row[field] for field in fieldnames]
                worksheet.append(row_data)

            # Save the workbook to the specified file path
            workbook.save(file_path_to_save)

            print("Successfully in xlsx")
            return True
        except Exception as e:
            print(e)
            return False

    # def csv_writer(self, userslists, file_path):
    #     # Open the CSV file in append mode ('a' or 'ab' for binary mode)
    #     count = 1
    #     file_name = self.src_path.split("/")[-1].split(".")[0]
    #     file_path_to_save = os.path.join(file_path, f"{file_name}.csv")
    #     if os.path.exists(file_path_to_save):
    #         file_path_to_save = os.path.join(file_path, f"{file_name}" + str(count) + ".csv")
    #
    #     while os.path.exists(file_path_to_save):
    #         file_path_to_save = os.path.join(file_path, f"{file_name}" + str(count) + ".csv")
    #         count += 1
    #
    #     try:
    #         with open(file_path_to_save, 'a', newline='', encoding='utf-8') as csvfile:
    #             # Specify the field names
    #             fieldnames = ['name', 'username', 'total_posts', "total_engagement"]
    #
    #             # Create a CSV DictWriter object
    #             csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #             # If the file is empty, write the header first
    #             if csvfile.tell() == 0:
    #                 csv_writer.writeheader()
    #
    #             # Write the new row to the CSV file
    #             for user_data_row in userslists:
    #                 print(user_data_row)
    #                 csv_writer.writerow(user_data_row)
    #                 print("Row added successfully.")
    #         print("successfully in csv")
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False


class MainManager(QtWidgets.QWidget, main_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(MainManager, self).__init__()
        self.setupUi(self)

        self.base_url = "https://api.twiscope.net/api/v3/twitter-analysis/userAnalysis/profile_analysis/"
        self.threadpool = QtCore.QThreadPool()

        self.selectSrcPath_btn.clicked.connect(self.select_src_path)
        self.selectExpPath_btn.clicked.connect(self.select_path_to_save)

        self.start_btn.clicked.connect(self.run)

        self.src_file_path = None
        self.exp_path = None

        self.msg = QtWidgets.QMessageBox()
        # self.msg.setStyleSheet("min-width: 50cm; ")

        self.tableWidget.setRowCount(0)
        table_headers = ['Name', 'Username', 'Status']
        self.tableWidget.setHorizontalHeaderLabels(table_headers)

        self.loading = None

    def run(self):
        worker = ApiWorker(self.base_url, self.src_file_path, self.exp_path)
        worker.setAutoDelete(True)
        self.loading = WaitingScreen()

        self.start_btn.setText("Running...")
        self.start_btn.setDisabled(True)
        self.start_btn.setStyleSheet("""color: rgb(255, 255, 255);
                                        background-color: rgb(255, 0, 0);;
                                        font: 22pt ".AppleSystemUIFont";
                                         border-radius: 9px;
                                        """)
        self.loading.show()

        worker.signals.current_user.connect(self.update_current_user_lbl)
        worker.signals.msg_exec.connect(self.msg_box)
        worker.signals.finished.connect(self.finished)
        self.threadpool.start(worker)

    def finished(self):
        self.loading.close()
        self.start_btn.setStyleSheet("""color: rgb(255, 255, 255);
                                        background-color: rgb(20,  190, 120);
                                        font: 22pt ".AppleSystemUIFont";
                                         border-radius: 9px;
                                        """)
        self.start_btn.setText("Start")
        self.start_btn.setDisabled(False)

    def msg_box(self, title, text):
        self.msg.setWindowTitle(title)
        self.msg.setText(text)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.exec_()

    def update_current_user_lbl(self, username):
        self.current_user_lbl.setText(username)

    def select_src_path(self, event):
        self.src_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '',
                                                                      'Files (*.xlsx)')
        if not self.src_file_path:
            self.msg.critical(self, "Error", "Please choose a file")
            self.src_path_lbl.setText("source file path ..........")
        else:
            self.src_path_lbl.setText(self.src_file_path)

    def select_path_to_save(self):
        self.exp_path = QFileDialog.getExistingDirectory(self, 'Hey! Select a path', f"{os.getcwd()}")
        if not self.exp_path:
            self.msg.critical(self, "Error", "Please select path")
            self.exp_path_lbl.setText("exported file path ..........")
        else:
            self.exp_path_lbl.setText(self.exp_path)


if __name__ == "__main__":
    # import qdarkstyle

    app = QtWidgets.QApplication([])
    w = MainManager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
