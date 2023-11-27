import numpy as np
from PIL import Image
from sklearn.datasets import load_digits
from scipy.spatial.distance import cdist

# Función para convertir valores entre 0 y 255 a valores entre 0 y 16
def convert_values(image):
    return (16 / 255) * image

# Cargar el conjunto de datos digits
digits = load_digits()

# Obtener las imágenes y las etiquetas
images = digits.images
labels = digits.target

# Ruta de la imagen con el número dibujado
image_path = 'numeros_paint/numero1_v3.png'  # Cambia esto a la ruta de tu imagen

# Cargar la imagen y convertirla a escala de grises
image = Image.open(image_path).convert('L')

# Redimensionar la imagen a 8x8
image_resized = image.resize((8, 8))

# Convertir la imagen a una matriz de píxeles
pixel_matrix = np.array(image_resized)

# Convertir valores entre 0 y 255 a valores entre 0 y 16
pixel_matrix = convert_values(pixel_matrix)

# Normalizar las matrices de píxeles del nuevo dígito y de los dígitos en el conjunto de datos
pixel_matrix_normalized = pixel_matrix.flatten() / 16.0
images_normalized = images.reshape(len(images), -1) / 16.0

'''
print("Matriz de píxeles normalizada del nuevo dígito:")
print(pixel_matrix_normalized)
'''

# Calcular las distancias euclidianas utilizando cdist
distances = cdist(pixel_matrix_normalized.reshape(1, -1), images_normalized, metric='euclidean')

'''
print("Matrices de píxeles normalizadas de los dígitos más cercanos:")
for i, idx in enumerate(np.argsort(distances.flatten())[:3]):
    print(images_normalized[idx].reshape(8, 8))

print("Matriz de distancias completa:")
print(distances)
'''
# Obtener los índices de los 3 dígitos más cercanos
closest_indices = np.argsort(distances.flatten())[:3]

print("Los 3 dígitos más cercanos son:")
for i, idx in enumerate(closest_indices):
    print(f"{i + 1}. Dígito: {labels[idx]}, Distancia Euclidiana: {distances[0][idx]}")
