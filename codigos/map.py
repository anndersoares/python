# -*- coding: utf-8 -*-
"""map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpNMrK4115ifVokxNJGtADoT6V2DI2kw
"""

#map

def dobro(x):
  return x*2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)