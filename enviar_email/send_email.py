# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)

import smtplib
from Tkinter import *

class Application(Frame):

    def sendPressed(self):
        email_sender = SendEmail(self.fromEntry.get(), self.toEntry.get().split(","),
                                 self.message.get("1.0",'end-1c'), "")
        email_sender.send_email()

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.columnconfigure(0, pad=1)
        self.columnconfigure(1, pad=1)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)


        self.fromLabel = Label(self, text="De:")
        self.fromLabel.grid(row=0, column=0)
        self.fromEntry = Entry(self)
        self.fromEntry.grid(row=0, column=1)

        self.toLabel = Label(self, text="Para:")
        self.toLabel.grid(row=1, column=0)
        self.toEntry = Entry(self)
        self.toEntry.grid(row=1, column=1)

        self.message = Text(self)
        self.message.configure(borderwidth=2, relief="sunken")
        self.message.grid(row=2, column=0, columnspan=4)



        send = Button(self, text="enviar", command=self.sendPressed)
        send.grid(row=3, column=0)

        self.pack()

        # widget = Entry(parent, show="*", width=15)




class SendEmail(object):
    def __init__(self, sender, receivers, message, gmail_passwd):
        self.sender = sender
        self.receivers = receivers
        self.message = message

    def send_email(self):
        # message = message
        #"""From: From Person <from@fromdomain.com>
        # To: To Person <to@todomain.com>
        # MIME-Version: 1.0
        # Content-type: text/html
        # Subject: SMTP HTML e-mail test

        # This is an e-mail message to be sent in HTML format

        # <b>This is HTML message.</b>
        # <h1>This is headline.</h1>
        # """

        try:
            # server = smtplib.SMTP('localhost', port=1025)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sender, "Tim#g44gl3*invictuS")

            server.sendmail(self.sender, self.receivers, self.message)
            print ("Successfully sent email")
        except smtplib.SMTPConnectError:
            print "Error connecting"
        except smtplib.SMTPSenderRefused:
            print "Error: unable to send "




app = Application()
app.master.geometry("600x500")
mainloop()