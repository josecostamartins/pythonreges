from __future__ import unicode_literals
# -*- coding: utf-8 -*-


from math import ceil

metros = float(raw_input("Informe a quantidade de metros quadrados: "))

lata = 18
preco_lata = 80.

galao = 3.6
preco_galao = 25.

qtd = round((metros/6)*1.1)


'''
        ATENÇÃO ATENÇÃO ATENÇÃO
        ATENÇÃO ATENÇÃO ATENÇÃO

        o lambda é uma função não importante para o objetivo do exercício, porém,
        o primeiro que descobrir o que ela faz, ganha 0.5 ponto
        Tem que falar:
            qual o objetivo de uma função lambda
            o que a função lambda deste arquivo faz

        A data limite é até dia anterior à primeira prova de Tópicos Especiais em Sistemas I

    '''
if qtd//lata >= 1 and qtd%lata == 0:

    print "Você precisa de {} {lata}".format(qtd//lata, lata=(lambda x: "latas" if x>1 else "lata")(qtd//lata))
    val_lata = (qtd//lata)*preco_lata
    print "Você vai gastar R${}".format(val_lata)
elif qtd//lata >= 1 and qtd%lata != 0:
    gl = (qtd%lata)/galao
    val_lata = (qtd//lata)*preco_lata
    val_gal = ceil(gl)*preco_galao
    print "Você precisa de {} {lata} e {} {galao}".format(qtd//lata, ceil(gl),
                                                          lata=(lambda x: "latas" if x>1 else "lata")(qtd//lata),
                                                          galao=(lambda x: "galões" if x>1 else "galão")(ceil(gl)))
    print "Você vai gastar R${}".format(val_lata+val_gal)
else:
    gl = qtd/galao
    val_gal = ceil(gl)*preco_galao
    print "Você precisa {} {suffix}".format(ceil(gl), suffix=(lambda x: "galões" if ceil(x)>1 else "galão")(gl))
    print "Você vai gastar R${}".format(val_gal)