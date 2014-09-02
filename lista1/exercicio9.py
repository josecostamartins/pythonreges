from __future__ import unicode_literals
# -*- coding: utf-8 -*-


# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(raw_input("Informe a temperatura em Celsius: "))
faren = celsius/5*9+32

print "O equivalente a {} Celsius é {} Farenheit".format(celsius, faren)