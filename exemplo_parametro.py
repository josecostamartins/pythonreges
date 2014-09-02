from __future__ import unicode_literals
# -*- coding: utf-8 -*- 
__author__ = 'josecostamartins'


"1. Faça um programa," \
    "com uma função que necessite de três argumentos,"\
    "e que forneça a soma desses três argumentos."

"2. Faça um programa,"\
    "com uma função que necessite de um argumento."\
    "A função retorna o valor de caractere ‘P’,"\
    "se seu argumento for positivo, e ‘N’,"\
    "se seu argumento for zero ou negativo"

def funcao_espuria():
    print "to sobrando"

def exemplo_parametro(parametro1="bom dia", parametro2="boa noite"):
    print parametro1, parametro2


exemplo_parametro()
exemplo_parametro("foo", "bar")
funcao_espuria()