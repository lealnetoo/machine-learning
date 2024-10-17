from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Função para carregar a imagem do computador
def carregar_imagem(caminho):
    # Abre a imagem usando PIL
    imagem = Image.open(caminho)
    return imagem

# Função para converter imagem colorida em cinza
def converter_para_cinza(imagem):
    largura, altura = imagem.size
    imagem_cinza = Image.new('L', (largura, altura))  # 'L' para modo de tons de cinza

    for i in range(largura):
        for j in range(altura):
            r, g, b = imagem.getpixel((i, j))
            # Fórmula para converter para cinza: média ponderada
            cinza = int(0.299*r + 0.587*g + 0.114*b)
            imagem_cinza.putpixel((i, j), cinza)
    
    return imagem_cinza

# Função para converter a imagem em cinza para preto e branco (threshold)
def converter_para_preto_branco(imagem_cinza, threshold=128):
    largura, altura = imagem_cinza.size
    imagem_preto_branco = Image.new('1', (largura, altura))  # '1' para modo binário (preto e branco)

    for i in range(largura):
        for j in range(altura):
            cinza = imagem_cinza.getpixel((i, j))
            # Se o valor de cinza for maior que o limiar (threshold), converte para branco (255), senão para preto (0)
            pb = 255 if cinza > threshold else 0
            imagem_preto_branco.putpixel((i, j), pb)
    
    return imagem_preto_branco

# Função para exibir a imagem
def mostrar_imagem(imagem, titulo):
    plt.imshow(np.array(imagem), cmap='gray' if imagem.mode == 'L' or imagem.mode == '1' else None)
    plt.title(titulo)
    plt.axis('off')  # Para ocultar os eixos
    plt.show()

# Caminho da imagem 
caminho_imagem = '/home/jose-leal/Pictures/lena.png' 

# Carregar a imagem do computador
imagem_colorida = carregar_imagem(caminho_imagem)

# Mostrar a imagem colorida original
mostrar_imagem(imagem_colorida, 'Imagem Colorida Original')

# Converter para níveis de cinza
imagem_cinza = converter_para_cinza(imagem_colorida)
mostrar_imagem(imagem_cinza, 'Imagem em Níveis de Cinza')

# Converter para preto e branco
imagem_preto_branco = converter_para_preto_branco(imagem_cinza, threshold=128)
mostrar_imagem(imagem_preto_branco, 'Imagem em Preto e Branco')
