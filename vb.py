# ------------------------------
# PROGRAMA DE BACKGROUND VIRTUAL
# ------------------------------

# IMPORTS
import cv2
import numpy

# WEBCAM VIDEO CAPTURE CATCH
cap = cv2.VideoCapture('/dev/video0')

# FRAME LOOP
# while True:
success,frame = cap.read()


# CONFIGURATION CAMERA
height, width = 720, 1280 # Tamanho da Tela
cap.set(cv2.CAP_PROP_FRAME_WIDTH ,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS, 60) # 60 FPS


# BACKGROUND IMAGE
#background = cv2.imread("image/medieval_city.jpg")

# ======
# TESTES
# ======
# Teste que tira foto da imagem da câmera
# comente o while do frame e desindente abaixo
#success,frame = cap.read()
cv2.imwrite("teste.jpg",frame)

