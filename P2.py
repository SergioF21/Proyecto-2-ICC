import numpy as np
from PIL import Image
from sklearn.datasets import load_digits
from scipy.spatial.distance import cdist
import cv2
import numpy as np
from sklearn import datasets

# ----------------------
#   ITEM C
# ----------------------

print("\nEste es el listado de todas las imágenes aplanadas: \n")
digitos = datasets.load_digits()
dataset_digits = digitos.data

print(dataset_digits)

def proceso(image):
    # Leer la imagen en escala de grises
    img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # Reducción de tamaño a 8x8
    new_img = cv2.resize(img_array, (8, 8))

    # Invertir valores y escalar a la escala de 0 a 16
    new_img = (new_img * -1 + 255) * 16 / 255

    new_img = new_img.astype(int)

    return new_img

# Ruta de la imagen proporcionada
image = "img/7.jpg"

# Preprocesa la imagen de entrada
img_procesada = proceso(image)

print("\nImagen procesada : \n")
print(img_procesada)

'''

# Calcular las distancias euclidianas utilizando cdist
distances = cdist(pixel_matrix_normalized.reshape(1, -1), images_normalized, metric='euclidean')


print("Matrices de píxeles normalizadas de los dígitos más cercanos:")
for i, idx in enumerate(np.argsort(distances.flatten())[:3]):
    print(images_normalized[idx].reshape(8, 8))

print("Matriz de distancias completa:")
print(distances)

# Obtener los índices de los 3 dígitos más cercanos
closest_indices = np.argsort(distances.flatten())[:3]

print("Los 3 dígitos más cercanos son:")
for i, idx in enumerate(closest_indices):
    print(f"{i + 1}. Dígito: {labels[idx]}, Distancia Euclidiana: {distances[0][idx]}")
'''