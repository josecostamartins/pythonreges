# -*- coding: utf-8 -*-
from __future__ import print_function
import random


nomes = ["Adriano", "Juliano", "Edson", "Wesley", "Giovani", "Edivaldo",
         "Marcos", "Edivaldo", "Jéssica Cristina", "Marcelo",
         "Benício", "Jéssica Fernanda", "Nicholas", "Mario"  ]

nomes_ordenados = sorted(nomes)

for nome in nomes_ordenados:
    rand = random.randint(1, 100)
    if rand % 2 == 0:
        print("{nome} fará os pares".format(nome=nome), file=open("resultado.txt", "a+w+b"))
        print(nome, " fará os pares")
    else:
        print("{nome} fará os ímpares".format(nome=nome), file=open("resultado.txt", "a+w+b"))
        print(nome, " fará os ímpares")
