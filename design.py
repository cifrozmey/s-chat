from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 440)

        self.setWindowIcon(QtGui.QIcon('logo.png')) 

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 370, 361))
        self.listWidget.setObjectName("listWidget")

        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(250, 380, 60, 25))
        self.button_send.setObjectName("button_send")

        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(320, 380, 60, 25))
        self.button_clear.setObjectName("button_clear")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 410, 100, 25))
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(120, 410, 150, 25))
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(260, 410, 150, 25))
        self.label3.setObjectName("label3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Similar Chat"))
        self.button_send.setText(_translate("MainWindow", "Send"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "By Cifrozmey"))
        self.label2.setText(_translate("MainWindow", "cifrozmey@gmail.com"))
        self.label3.setText(_translate("MainWindow", "https://t.me/cifrozmey"))