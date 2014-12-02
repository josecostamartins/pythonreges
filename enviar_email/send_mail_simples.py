# # -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)
import smtplib
import getpass

class SendEmail(object):
    def __init__(self, sender="", receivers="", message="", passwd=""):
        self.sender = sender
        self.receivers = receivers
        self.message = message
        self.passwd = passwd

    def send_email(self):
        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        MIME-Version: 1.0
        Content-type: text/html
        Subject: SMTP HTML e-mail test

        This is an e-mail message to be sent in HTML format

        <b>This is HTML message.</b>
        <h1>This is headline.</h1>Tim#g44gl3*invictuS
        """

        try:
            # server = smtplib.SMTP('localhost', port=1025)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("josecostamartins@gmail.com", "Tim#g44gl3*invictuS")

            server.sendmail("josecostamartins@gmail.com", ["joseaugusto@jjmartins.com"], message)
            print "Successfully sent email"
        except smtplib.SMTPConnectError:
            print "Error connecting"
        except smtplib.SMTPSenderRefused:
            print  "Error: unable to send "


if __name__=="__main__":

    sender = raw_input("De: ")
    passwd = getpass.getpass()
    receivers = raw_input("Para: ").split(",")
    message = raw_input("Informe a mensagem: ")

    email = SendEmail()
    email.sender()
