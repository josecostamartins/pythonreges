# *-* coding: utf-8 *-*

'''
1. Classe Bola: Crie uma classe que modele uma bola:
    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
'''

class Bola(object):
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print self.cor
        return self.cor

