# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)


nome = raw_input("Informe seu nome: ")

for index in reversed(range(len(nome))):
    print nome[:index+1]