#!/usr/bin/python3

import os
import sys
import datetime
import socket
import ssl
import telebot

sites = ["врач.здоровьедона.рф", "doctor.tm26.ru", "tmk.kuzdrav.ru", \
          "tele-med.spb.ru", "tmc.medkhv.ru", "newtmk.kuban-online.ru", \
          "tmc.chitazdrav.ru", "telemed.mzio.ru", "tmkportal.polarmed.ru", \
          "telemed.kurskzdrav.ru", "gw.chel.mnogomed.ru", ]

token = ''

bot = telebot.TeleBot(token)


def send_notification(chat_id, text): 
         bot.send_message(chat_id='', text=text)
    
def check_ssl_date(hostname: str, port: str = '443'):
    context = ssl.create_default_context()
    try:
      with socket.create_connection((hostname, port)) as sock:
        try:
          with context.wrap_socket(sock, server_hostname=hostname) as ssock:
              ssl_info = ssock.getpeercert()
              expiry_date = datetime.datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
              global delta
              delta = expiry_date - datetime.datetime.utcnow()
              if delta.days < 7:
                 print(f'{hostname} expires in {delta.days} day(s)')
                 global text
                 text = hostname + ' ' + 'expire in' + ' ' +str(delta.days) + ' ' + 'days'
                 send_notification(hostname, text)    
                 return delta.days, hostname
        except:
                 
                 send_notification(hostname, text)
    except:    
        conn_refuse =    'Connection refused' + ' ' + hostname 
        send_notification(hostname, conn_refuse)       

def main():
     for site in sites:
         check_ssl_date(site)

if __name__ == '__main__':
    main()
      