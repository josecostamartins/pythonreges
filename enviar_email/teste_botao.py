# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()