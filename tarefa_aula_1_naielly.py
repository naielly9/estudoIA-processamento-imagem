# -*- coding: utf-8 -*-
"""Tarefa Aula 1_Naielly.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-EnD7aqGucw5QW5L0OsFeDS4CYGI-bCA

Ex: 1

# Nova seção
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
from google.colab import files

uploaded = files.upload()
img = cv2.imread('/content/sample_data/img1.jpg.JPG')

plt.imshow(img)
print("\nImagem original")
plt.show()

imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(imgrgb)
print("\nImagem RGB")
plt.show()

print('Largura em pixels:(x) ', end='')
print(img.shape[1]) #Largura da img
print('Altura em pixels: (y)', end='')
print(img.shape[0]) #Altura da img
print('Quantidade de canais: ', end='')
print(img.shape[2])

"""Ex: 2

a)
"""

img1 = cv2.imread('/content/sample_data/img1.jpg.JPG')
img2 = cv2.imread('/content/sample_data/img2.jpg')
img3 = cv2.imread('/content/sample_data/img3.jpg')
img4 = cv2.imread('/content/sample_data/img4.jpg')

print('Largura em pixels:(x) ', end='')
print(img1.shape[1]) #Largura da img
print('Altura em pixels: (y)', end='')
print(img1.shape[0]) #Altura da img
print("-----------------------------")
print('Largura em pixels:(x) ', end='')
print(img2.shape[1]) #Largura da img
print('Altura em pixels: (y)', end='')
print(img2.shape[0]) #Altura da img
print("-----------------------------")
print('Largura em pixels:(x) ', end='')
print(img3.shape[1]) #Largura da img
print('Altura em pixels: (y)', end='')
print(img3.shape[0]) #Altura da img
print("-----------------------------")
print('Largura em pixels:(x) ', end='')
print(img4.shape[1]) #Largura da img
print('Altura em pixels: (y)', end='')
print(img4.shape[0]) #Altura da img

"""B)"""

img1rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1gray = cv2.cvtColor(img1rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(img1gray, cmap= 'gray')
plt.title("Imagem niveis de cinza")
plt.show()

img2rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2gray = cv2.cvtColor(img2rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(img2gray, cmap= 'gray')
plt.title("Imagem niveis de cinza")
plt.show()

img3rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img3gray = cv2.cvtColor(img3rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(img3gray, cmap= 'gray')
plt.title("Imagem niveis de cinza")
plt.show()

img4rgb = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img4gray = cv2.cvtColor(img4rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(img4gray, cmap= 'gray')
plt.title("Imagem niveis de cinza")
plt.show()



"""c)"""

img1HSV = cv2.cvtColor(img1rgb, cv2.COLOR_RGB2HSV)
img2HSV = cv2.cvtColor(img2rgb, cv2.COLOR_RGB2HSV)
img3HSV = cv2.cvtColor(img3rgb, cv2.COLOR_RGB2HSV)
img4HSV = cv2.cvtColor(img4rgb, cv2.COLOR_RGB2HSV)

plt.imshow(img1HSV)
print("\nImagem HSV")
plt.show()
plt.imshow(img2HSV)
print("\nImagem HSV")
plt.show()
plt.imshow(img3HSV)
print("\nImagem HSV")
plt.show()
plt.imshow(img4HSV)
print("\nImagem HSV")
plt.show()

"""d)"""

vermelho1, verde1, azul1 = cv2.split(img1rgb)
vermelho2, verde2, azul2 = cv2.split(img2rgb)
vermelho3, verde3, azul3 = cv2.split(img3rgb)
vermelho4, verde4, azul4 = cv2.split(img4rgb)

plt.imshow(vermelho1, cmap='Reds_r')
plt.title("Canal vermelho")
plt.show()
plt.imshow(verde1, cmap='Greens_r')
plt.title("Canal verde")
plt.show()
plt.imshow(azul1, cmap='Blues_r')
plt.title("Canal azul")
plt.show()

plt.imshow(vermelho2, cmap='Reds_r')
plt.title("Canal vermelho")
plt.show()
plt.imshow(verde2, cmap='Greens_r')
plt.title("Canal verde")
plt.show()
plt.imshow(azul2, cmap='Blues_r')
plt.title("Canal azul")
plt.show()

plt.imshow(vermelho3, cmap='Reds_r')
plt.title("Canal vermelho")
plt.show()
plt.imshow(verde3, cmap='Greens_r')
plt.title("Canal verde")
plt.show()
plt.imshow(azul3, cmap='Blues_r')
plt.title("Canal azul")
plt.show()

plt.imshow(vermelho4, cmap='Reds_r')
plt.title("Canal vermelho")
plt.show()
plt.imshow(verde4, cmap='Greens_r')
plt.title("Canal verde")
plt.show()
plt.imshow(azul4, cmap='Blues_r')
plt.title("Canal azul")
plt.show()

"""e)"""

h1, s1, v1 = cv2.split(img1HSV)
h2, s2, v2 = cv2.split(img2HSV)
h3, s3, v3 = cv2.split(img3HSV)
h4, s4, v4 = cv2.split(img4HSV)

plt.imshow(h1)
plt.title("Hue")
plt.show()
plt.imshow(s1)
plt.title("Saturation")
plt.show()
plt.imshow(v1)
plt.title("Value")
plt.show()

plt.imshow(h2)
plt.title("Hue")
plt.show()
plt.imshow(s2)
plt.title("Saturation")
plt.show()
plt.imshow(v2)
plt.title("Value")
plt.show()

plt.imshow(h3)
plt.title("Hue")
plt.show()
plt.imshow(s3)
plt.title("Saturation")
plt.show()
plt.imshow(v3)
plt.title("Value")
plt.show()

plt.imshow(h4)
plt.title("Hue")
plt.show()
plt.imshow(s4)
plt.title("Saturation")
plt.show()
plt.imshow(v4)
plt.title("Value")
plt.show()