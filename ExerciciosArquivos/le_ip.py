# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)

file = open("ips.txt");
ips = file.readlines()
validos = []
invalidos = []
for index in range(len(ips)):
    if index == 1:



filew = open("novo_arquivo.txt", "w")
file.write("valido\n")
#escrvo os ips validos
file.write("invalidos\n")
