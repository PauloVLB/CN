import cv2
import numpy as np
import math
import time

def desenha_quadrado(L, graus_rotacao, img, cor):
    centro = (img.shape[0]//2, img.shape[1]//2)
    angulo = math.radians(graus_rotacao)

    # Define as coordenadas dos pontos do quadrado não-rotacionado
    p1 = (centro[0]-L//2, centro[1]-L//2)
    p2 = (centro[0]+L//2, centro[1]-L//2)
    p3 = (centro[0]+L//2, centro[1]+L//2)
    p4 = (centro[0]-L//2, centro[1]+L//2)

    # Aplica a rotação em cada ponto
    cos_angulo = math.cos(angulo)
    sin_angulo = math.sin(angulo)

    p1_rot = (int((p1[0]-centro[0])*cos_angulo - (p1[1]-centro[1])*sin_angulo + centro[0]), int((p1[0]-centro[0])*sin_angulo + (p1[1]-centro[1])*cos_angulo + centro[1]))
    p2_rot = (int((p2[0]-centro[0])*cos_angulo - (p2[1]-centro[1])*sin_angulo + centro[0]), int((p2[0]-centro[0])*sin_angulo + (p2[1]-centro[1])*cos_angulo + centro[1]))
    p3_rot = (int((p3[0]-centro[0])*cos_angulo - (p3[1]-centro[1])*sin_angulo + centro[0]), int((p3[0]-centro[0])*sin_angulo + (p3[1]-centro[1])*cos_angulo + centro[1]))
    p4_rot = (int((p4[0]-centro[0])*cos_angulo - (p4[1]-centro[1])*sin_angulo + centro[0]), int((p4[0]-centro[0])*sin_angulo + (p4[1]-centro[1])*cos_angulo + centro[1]))

    # Desenha as linhas do quadrado
    cv2.line(img, p1_rot, p2_rot, cor, 2)
    cv2.line(img, p2_rot, p3_rot, cor, 2)
    cv2.line(img, p3_rot, p4_rot, cor, 2)
    cv2.line(img, p4_rot, p1_rot, cor, 2)


img = np.zeros((500, 500, 3), np.uint8)

img.fill(0)
desenha_quadrado(100, 0, img, (0, 255, 0))
desenha_quadrado(100, 45, img, (0, 0, 255))
cv2.putText(img, f'k = 0', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.imshow('quadrado', img)
cv2.waitKey(0)

for k in np.arange(0, 1.001, 0.01):
    img.fill(0)

    desenha_quadrado(100 * (k + 1), 0, img, (0, 255, 0))
    desenha_quadrado(100 * (1 - k/2), 45, img, (0, 0, 255))
    cv2.putText(img, f'k = {k}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow('quadrado', img)
    cv2.waitKey(30)

cv2.waitKey(0)

k = 3 * math.sqrt(2) - 4
img.fill(0)
desenha_quadrado(100 * (k + 1), 0, img, (0, 255, 0))
desenha_quadrado(100 * (1 - k/2), 45, img, (0, 0, 255))
cv2.putText(img, f'k = {k}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow('quadrado', img)
cv2.waitKey(0)