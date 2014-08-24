from __future__ import unicode_literals
# -*- coding: utf-8 -*-

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho = float(raw_input("Quanto você ganha por hora? \n"))
horas = int(raw_input("Quantas horas você trabalha por mês? \n"))

print "O seu salário total no final do mês é de: {}".format(ganho*horas)