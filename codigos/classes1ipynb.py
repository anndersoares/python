# -*- coding: utf-8 -*-
"""classes1ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LTV9xQE9X-by6A1Gr0LmvkkibSI-BP6H
"""

class Carro:
  def __init__(self, nome, ano):
    self.nome = nome
    self.ano = ano
  
  def obterNome(self):
    return self.nome
  
  def obterAno(self):
    return self.ano

carro = Carro("Camaro", 2010)
print (carro.obterNome())
print (carro.obterAno())

#código com construtor fica mais simples.