import cv2 
import numpy as np

img = cv2.imread('pika.png')
kernel = np.ones((5,5), np.uint8)

Canny = cv2.Canny(imagen, 225, 225)
Dialation = cv2.dilate(Canny, kernel, iterations=1)
Eroded = cv2.erode(Dialation,kernel,iterations=1)

i = cv2.resize(imagen,(200,250))
i_color = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
i_share = cv2.resize(imggris,(210,260))
i_dilation = cv2.resize(Dialation,(220,270))
i_rectangle =cv2.rectangle(imagen,(100,900),(500,300),(0,0,255))
i_gredr = cv2.resize(imgrec,(150,200))
i_canny = cv2.resize(Canny,(155,205))
i_eroded = cv2.resize(Eroded,(155,205))

cv2.imshow("Imagen", img)
cv2.imshow("Color Gris", imshare)
cv2.imshow("Borde", imgdilation)
cv2.imshow("Rectángulo", imgredr)
cv2.imshow("Canny", imgcanny)
cv2.imshow("Eroded", imgeroded)
cv2.waitKey(0)