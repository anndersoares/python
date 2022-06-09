# -*- coding: utf-8 -*-
"""multi-graficos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NJwqq-R4oEyWuj6SWDSNeSlPRWT81zho
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1, 100)

y1 = 2*x
y2 = x**2
y3 = x**3
y4 = np.sin(x)

fig, janela = plt.subplots(2,2)

janela[0,0].plot(x, y1, ".")
janela[0,1].plot(x, y2, ".r")
janela[1,0].plot(x, y3, ".y")
janela[1,1].plot(x, y4, ".g")

fig.legend(["Reta", "Parabóla", "Cúbica", "Sin"])
plt.show()