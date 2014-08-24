from __future__ import unicode_literals
# -*- coding: utf-8 -*-


from math import ceil

metros = float(raw_input("Informe a quantidade de metros quadrados: "))

lata = 18
preco_lata = 80.

galao = 3.6
preco_galao = 25.

qtd = round((metros/6)*1.1)


if qtd//lata >= 1 and qtd%lata == 0:
    print "Você precisa de {} lata(s)".format(qtd//lata)
    val_lata = (qtd//lata)*preco_lata
    print "Você vai gastar R${}".format(val_lata)
elif qtd//lata >= 1 and qtd%lata != 0:
    gl = (qtd%lata)/galao
    val_lata = (qtd//lata)*preco_lata
    val_gal = ceil(gl)*preco_galao
    print "Você precisa de {} lata(s) e {} galão(ões)".format(qtd//lata, ceil(gl))
    print "Você vai gastar R${}".format(val_lata+val_gal)
elif qtd//lata < 1:
    gl = qtd/galao
    val_gal = ceil(gl)*preco_galao
    print "Você precisa {} galões".format(ceil(gl))
    print "Você vai gastar R${}".format(val_gal)