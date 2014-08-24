# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

def funcao_com_parametro(param1, param2):
    print(param1, " ", param2)

funcao_com_parametro("foo", "bar") #exemplo posicional
funcao_com_parametro(param2="foo", param1="bar") #exemplo nomeado