import numpy
import cv2
from matplotlib import pyplot as plt

def main ():

	#Cargar Imagen
	img = cv2.imread("Home/Pictures/carro.jpg")

	#Cargar Imagen a escala de grises
	img = cv2.imread("Home/Pictures/carro.jpg", cv2.IMREAD_GRAYSCALE)

	#Guardar Imagen
	cv2.imwrite('carrow.png',img)

	#Mostrar la imagen, esperar tecla para cerrar y destruir ventanas
	cv2.imshow('image carro',img)
	cv2.waitKey(0)
	cv2.destroyAllWIndows()

	
	matploit()
	
	return
