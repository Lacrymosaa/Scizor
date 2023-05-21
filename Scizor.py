import cv2
import os
import numpy as np

def cortar_cartas(imagem):
    # Carrega a imagem
    img = cv2.imread(imagem)

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplica uma limiarização para converter os espaços brancos em preto e as cartas em branco
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Encontra os contornos das cartas
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Cria uma pasta para armazenar as cartas cortadas
    if not os.path.exists('cartas'):
        os.makedirs('cartas')

    # Corta e salva cada carta como um arquivo separado
    for i, contour in enumerate(contours):
        # Obtém as coordenadas do retângulo que contém a carta
        x, y, w, h = cv2.boundingRect(contour)

        # Corta a carta da imagem original
        carta = img[y:y+h, x:x+w]

        # Salva a carta como um arquivo PNG
        cv2.imwrite(f'cartas/carta{i+1}.png', carta)

    print("Cartas cortadas e salvas com sucesso!")

# Chama a função para cortar as cartas da imagem
cortar_cartas('srcs/tarot.png')
