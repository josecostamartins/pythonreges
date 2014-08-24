from __future__ import unicode_literals
# -*- coding: utf-8 -*-


# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


int1 = int(raw_input("Insira o primeiro número inteiro: "))
int2 = int(raw_input("Insira o segundo número inteiro: "))
float1 = float(raw_input("Insira o primeiro número real: "))

print "O dobro do primeiro com metade do segundo é: {}".format(int1*2*int2/2)
print "A soma do triplo do primeiro com o terceiro é: {}".format(int1*3+float1)
print "o terceiro elevado ao cubo é: {}".format(float1**3)
