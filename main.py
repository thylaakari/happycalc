# Form implementation generated from reading ui file 'makeup.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 360, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(208, 208, 208);\n"
                                        "color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(0, 320, 150, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("background-color: rgb(223, 39, 255);")
        self.btn0.setObjectName("btn0")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 320, 150, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(0, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(255, 216, 56);")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(100, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(200, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(0, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color: rgb(170, 0, 127);")
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(200, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("background-color: rgb(50, 32, 255);")
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(100, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                "background-color: rgb(85, 255, 0);")
        self.btn5.setObjectName("btn5")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(0, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                "background-color: rgb(255, 85, 0);")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(100, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("background-color: rgb(115, 14, 11);")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(200, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                "background-color: rgb(85, 170, 127);")
        self.btn9.setObjectName("btn9")
        self.btn3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_2.setGeometry(QtCore.QRect(300, 50, 60, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn3_2.setFont(font)
        self.btn3_2.setStyleSheet("background-color: rgb(255, 142, 169);")
        self.btn3_2.setObjectName("btn3_2")
        self.btn3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_3.setGeometry(QtCore.QRect(300, 140, 60, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn3_3.setFont(font)
        self.btn3_3.setStyleSheet("background-color: rgb(255, 51, 51);")
        self.btn3_3.setObjectName("btn3_3")
        self.btn3_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_4.setGeometry(QtCore.QRect(300, 230, 60, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn3_4.setFont(font)
        self.btn3_4.setStyleSheet("background-color: rgb(38, 173, 81);")
        self.btn3_4.setObjectName("btn3_4")
        self.btn3_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3_5.setGeometry(QtCore.QRect(300, 320, 60, 90))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn3_5.setFont(font)
        self.btn3_5.setStyleSheet("background-color: rgb(255, 190, 116);")
        self.btn3_5.setObjectName("btn3_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_fncs()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn3_2.setText(_translate("MainWindow", "+"))
        self.btn3_3.setText(_translate("MainWindow", "-"))
        self.btn3_4.setText(_translate("MainWindow", "*"))
        self.btn3_5.setText(_translate("MainWindow", "/"))

    def add_fncs(self):
        self.btn0.clicked.connect(lambda: self.write_number(self.btn0.text()))
        self.btn1.clicked.connect(lambda: self.write_number(self.btn1.text()))
        self.btn2.clicked.connect(lambda: self.write_number(self.btn2.text()))
        self.btn3.clicked.connect(lambda: self.write_number(self.btn3.text()))
        self.btn4.clicked.connect(lambda: self.write_number(self.btn4.text()))
        self.btn5.clicked.connect(lambda: self.write_number(self.btn5.text()))
        self.btn6.clicked.connect(lambda: self.write_number(self.btn6.text()))
        self.btn7.clicked.connect(lambda: self.write_number(self.btn7.text()))
        self.btn8.clicked.connect(lambda: self.write_number(self.btn8.text()))
        self.btn9.clicked.connect(lambda: self.write_number(self.btn9.text()))

        self.btn3_2.clicked.connect(lambda: self.write_number(self.btn3_2.text()))
        self.btn3_3.clicked.connect(lambda: self.write_number(self.btn3_3.text()))
        self.btn3_4.clicked.connect(lambda: self.write_number(self.btn3_4.text()))
        self.btn3_5.clicked.connect(lambda: self.write_number(self.btn3_5.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == '0' or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        self.label_result.setText(str(eval(self.label_result.text())))
        self.is_equal = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
