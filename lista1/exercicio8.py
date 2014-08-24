from __future__ import unicode_literals
# -*- coding: utf-8 -*-

#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura
# em graus Celsius. C = (5 * (F-32) / 9).

faren = float(raw_input("Informe a temperatura em Farenheit: "))
celsius = 5 * (faren-32)/9

print "O equivalente a {} Farenheit é {} Celsius".format(faren, celsius)