# -*- coding: utf-8 -*-
# from __future__ import print_function

# Faça um programa que peça as 2 notas bimestrais, as duas notas dos trabalhos e calcule a média
# * prova * 7 (vale 70%)
# * trabalho * 3 (vale 30%)



var1 = raw_input("Informe a nota da primeira prova: ")
var2 = raw_input("Informe a nota da segunda prova: ")
var3 = raw_input("Informe a nota do primeiro trabalho: ")
var4 = raw_input("Informe a nota do segundo trabalho: ")
media_prova = (float(var1)+float(var2))/2
media_trabalho = (float(var3)+float(var4))/2
media = ((media_prova*7) + (media_trabalho*3))/10 #prova tem peso 7 e trabalhos tem peso 3

# print("A média é: {}".format(media))
print "A média é: {}".format(media)


