from __future__ import unicode_literals
# -*- coding: utf-8 -*-


lata = 18
preco = 80.
cobertura = 3.
metros = float(raw_input("Informe a quantidade de metros quadrados: "))

qtd_latas = metros/(cobertura*lata)
valor = qtd_latas*preco

print "você deve comprar {} latas".format(qtd_latas)
print "total da sua compra é: R${}".format(valor)