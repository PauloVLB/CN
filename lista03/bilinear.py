import cv2
import numpy as np

L = 480
C = 640

m = np.zeros((L, C, 3), np.uint8)

v = np.array(((255, 55, 5), (10, 20, 50), (50, 220, 80), (255, 205, 215)))

q12 = v[0]
q22 = v[1]
q11 = v[2]
q21 = v[3]

for i in range(L):
	for j in range(C):
		x = j / (C-1)
		y = i / (L-1)
		
		r = (1 - x) * (1 - y) * q12[0] + x * (1 - y) * q22[0] + (1 - x) * y * q11[0] + x * y * q21[0]
		g = (1 - x) * (1 - y) * q12[1] + x * (1 - y) * q22[1] + (1 - x) * y * q11[1] + x * y * q21[1]
		b = (1 - x) * (1 - y) * q12[2] + x * (1 - y) * q22[2] + (1 - x) * y * q11[2] + x * y * q21[2]
        
		m[i][j] = (r, g, b)

cv2.imshow('janela', m)
cv2.waitKey(0)
