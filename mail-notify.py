#!/usr/bin/python3

import imapclient
import logging
import imaplib
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMessageBox

def get_mail():

 # Задание переменных для подключения к серверу     
    mail_srv = "imap.rambler.ru"
    mail_port = 993
    mail_user = ""
    mail_pass = ""


#logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
#level=logging.DEBUG)

# Подключение к серверу
    server = imapclient.IMAPClient(mail_srv, mail_port, ssl=True)
    server.noop()
    try:
        server.login(mail_user, mail_pass)
    except  imapclient.exceptions.LoginError:
        print("Invalid login or password")
# Переход к папке с Входящими сообщениями
    server.select_folder('INBOX', readonly=True)
    UIDs = server.search(['UNSEEN'])
    lenth = len(UIDs)
# Проверяем кол-во не прочитанных сообщений больше 0 
    if lenth > 0:
# Создаем окно сообщения о наличии не прочитанных сообщений
        notify = QMessageBox()
        notify.setWindowTitle("Уведомление")
        notify.setText("У вас есть не прочитанные сообщения")
        notify.setIcon(QMessageBox.Information)
        notify.setEscapeButton(QMessageBox.Ok)
        notify.exec_()
# Закрываем соединение с сервером
    server.logout()

def main():
    app = QApplication(sys.argv)
    get_mail()
    
if __name__ == "__main__":
    main()
