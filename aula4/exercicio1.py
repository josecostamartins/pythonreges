# -*- coding: utf-8 -*-
periodo = raw_input("Informe o período do dia que estamos"\
                    ", \nM-matutino, \nV-vespertino, \nN-noturno: ")

if periodo == "M":
    print "Bom dia!"
elif periodo == "V":
    print "Boa tarde!"
elif periodo == "N":
    print "Boa noite!"
else:
    print "Valor inválido"
