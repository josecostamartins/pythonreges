# -*- coding: utf-8 -*-
# from __future__ import (unicode_literals, nested_scopes, generators, division,
#                         absolute_import, with_statement, print_function)

import datetime
import math

class Funcionario(object):

    def __init__(self, nome = "Albert", sobrenome = "Einstein", idade = 29, salario = 2000, cargo = "Chefe"):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo

        print "criou"



nome = raw_input("digite seu nome: ")
sobrenome = raw_input("digite seu sobrenome: ")
idade = raw_input("digite seu idade: ")
salario = raw_input("digite seu salario: ")
cargo = raw_input("digite seu cargo: ")

# class Programador(Funcionario):
#     cargo = "Programador"
#
#
# class Professor(Funcionario):
#     cargo = "Professor"
#
# class Doido(Programador, Professor):
#     cargo = "Programador e Professor"
# # fim das classes
#
adriano = Funcionario(nome, sobrenome, idade, salario) #crio uma instância de uma classe
print adriano.nome
print adriano.sobrenome
print adriano.idade
print adriano.salario
print adriano.cargo

# adriano.especializacao = "PHP" #crio um atributo fora do escopo da classe
# print "NOME: ", adriano.nome
# print funcionario.sobrenome
# print funcionario.cargo
# print funcionario.salario
#
#
#
# marcos = Funcionario()
# print marcos.sobrenome
# print marcos.nome

#
# programador = Programador()
# print programador.sobrenome
# print programador.cargo
# print programador.salario


# print type([])
# print type((1,))

# print type(Usuario)
# print type(usuario)
# print Funcionario.__dict__
# print Funcionario.__bases__
