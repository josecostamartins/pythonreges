# -*- coding: utf-8 -*-
from __future__ import print_function
import math

x1 = int(raw_input("Digite o valor de x1: "))
print(x1)
x2 = int(raw_input("Digite o valor de x2: "))
print(x2)
y1 = int(raw_input("Digite o valor de y1: "))
print(y1)
y2 = int(raw_input("Digite o valor de y2: "))
print(y2)

distancia = math.sqrt((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))
print(distancia)


