from __future__ import unicode_literals
# -*- coding: utf-8 -*-

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# • calcule os descontos e o salário líquido, conforme a tabela abaixo:
# • +SalárioBruto:R$ • -IR(11%):R$
# • - INSS (8%) :R$
# • -Sindicato(5%):R$



por_hora = float(raw_input("Informe quanto você ganha por hora: "))
horas = float(raw_input("Informe quantas horas você trabalha por mês: "))

bruto = por_hora*horas
inss = bruto*0.08
sind = bruto*0.05
liquido = bruto-inss-sind-bruto*0.11

print "Salário bruto: {}".format(bruto)
print "INSS: {}".format(inss)
print "Sidicato: {}".format(sind)
print "Salário Líquido: {}".format(liquido)