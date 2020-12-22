import os
import sys
import socket
import design
import threading
import win32gui, win32con
from PyQt5.QtCore import QSize 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

SERVER_ADDRESS = ('тут ip локального сервера', 8125)
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto(('User1 зашел в чат').encode('utf-8'), SERVER_ADDRESS)

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        def reading_socket():
            while True:
                data = sor.recv(1024)
                self.listWidget.addItem(data.decode('utf-8'))

        potok = threading.Thread(target=reading_socket)
        potok.start()
        
        self.line = QLabel(self)
        self.line = QLineEdit(self)
        self.line.resize(230, 25)
        self.line.move(10, 380)

        self.button_send.clicked.connect(self.send_message)
        self.button_clear.clicked.connect(self.clear_message)

    def send_message(self):
        message = "User1: " + self.line.text()
        self.listWidget.addItem(message)
        sor.sendto((message).encode('utf-8'), SERVER_ADDRESS)
        self.line.clear()

    def clear_message(self):
        self.listWidget.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()