import cv2
import numpy as np
def proceso(image):
    # Leer la imagen en escala de grises
    img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    print("img_array", img_array)
    
    # Reducción de tamaño a 8x8
    new_img = cv2.resize(img_array, (8, 8))
    print("new_img", new_img)
    
    # print("Tipo de datos de 'new_img':", new_img.dtype)  # Print para depuración
    # Invertir valores y escalar a la escala de 0 a 16
    new_img = (new_img * -1 + 255) * 16 / 255

    print("new_img invertido", new_img)
    new_img = new_img.astype(np.uint8)  # Conversión a uint8
    return new_img
