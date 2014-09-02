from __future__ import unicode_literals
# -*- coding: utf-8 -*-

tamanho = float(raw_input("Informe o tamanho do arquivo (MB): "))
velocidade = float(raw_input("Informe a velocidade de conexão (em Mbps): "))


print "O tempo de duração do seu download será de: {} minutos".format(tamanho/(velocidade/8)/60)