# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)

string1 = raw_input("informe a primeira string: ")
string2 = raw_input("informe a segunda string: ")

tamanho1 = len(string1)
tamanho2 = len(string2)

if len(string1) == len(string2):
    print "As duas strings possuem o mesmo tamanho"
else:
    print "As duas strings possuem o tamanhos diferentes"

if string1 == string2:
    print "As duas strings possuem conteúdos iguais"
else:
    print "As duas strings possuem conteúdos diferentes"