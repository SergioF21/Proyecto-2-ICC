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

# ----------------------
#   ITEM D
# ----------------------

def euclidean_distance(img1, img2):
    # Calcular la distancia euclidiana entre dos imágenes
    return np.sqrt(np.sum((img1 - img2) ** 2))

def find_most_similar_digits(new_digit, dataset_digits):
    # Inicializar una lista para almacenar las distancias y los índices de los dígitos
    distances = []
    new_flat = new_digit.flatten()

    # Calcular la distancia euclidiana para cada dígito en el dataset
    for i, digit in enumerate(dataset_digits):
        distance = euclidean_distance(new_flat, digit)
        distances.append((distance, i))

    # Ordenar la lista de distancias de menor a mayor
    distances.sort()

    # Obtener los índices de los 3 dígitos más cercanos
    closest_indices = [index for _, index in distances[:3]]

    return closest_indices

closest_indices = find_most_similar_digits(img_procesada, dataset_digits)


# ----------------------
#   ITEM E
# ----------------------

print("\nLos 3 dígitos más parecidos del dataset digits:")
for i, index in enumerate(closest_indices):
    print(f"Índice {i + 1}: {index}, Etiqueta: {digitos.target[index]}")
    print(digitos.images[index].reshape((8, 8)))  # Mostrar la imagen
    print("-" * 40)










'''import numpy as np
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
image_path = 'img/7.jpg'  # Cambia esto a la ruta de tu imagen

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

print("Matriz de píxeles normalizada del nuevo dígito:")
print(pixel_matrix_normalized)


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