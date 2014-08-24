from __future__ import unicode_literals
# -*- coding: utf-8 -*-


#Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58


altura = float(raw_input("Informe sua altura: "))
print "Seu peso deve ser de {}KG".format(72.7*altura-58)
