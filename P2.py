import cv2
import numpy as np
from sklearn import datasets

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits


# Cargar el conjunto de datos digits
digitos = load_digits()

# Obtener las imágenes y las etiquetas
images = digitos.images
labels = digitos.target

# Crear una matriz para almacenar las imágenes promedio
average_images = np.zeros((10, 8, 8))

# Calcular la imagen promedio para cada dígito
for i in range(10):
    digit_images = images[labels == i]
    average_images[i] = np.mean(digit_images, axis=0)


# Función para mostrar la imagen promedio de un dígito
def mostrar_average_image(digito):
    plt.imshow(average_images[digito], cmap='gray')
    plt.title(f'Imagen promedio del dígito {digito}')
    plt.show()

# Menú para el usuario
while True:
    print("1. Mostrar imágenes promedio de todos los dígitos.")
    print("2. Mostrar imagen promedio de un dígito específico.")
    print("3. Salir")

    choice = input("Ingrese su elección (1, 2 o 3): ")

    if choice == '1':
        # Mostrar imágenes promedio de todos los dígitos
        fig, axs = plt.subplots(2, 5, figsize=(10,5))

        for digit in range(10):
            row = digit // 5
            col = digit % 5
            ax = axs[row, col]
            im = ax.imshow(average_images[digit], cmap='gray', vmin=0, vmax=16)
            ax.set_title(f'Promedio #{digit}')
        cbar = fig.colorbar(im, ax=axs, orientation='vertical', ticks=np.arange(0, 17, 1))
        cbar.set_label('Valor')
        plt.show()

    elif choice == '2':
        # Solicitar al usuario el dígito específico
        digito = int(input("Ingrese el dígito (0-9): "))
        if 0 <= digito <= 9:
            # Mostrar la imagen promedio del dígito especificado
            mostrar_average_image(digito)
        else:
            print("Entrada inválida. Por favor, ingrese un número entre 0 y 9.")
    elif choice == '3':
        break
    else:
        print("Entrada inválida. Por favor, ingrese 1, 2 o 3.")

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

    return closest_indices, [distance for distance, _ in distances[:3]]

closest_indices, closest_distances = find_most_similar_digits(img_procesada, dataset_digits)


# ----------------------
#   ITEM E
# ----------------------

print("\nLos 3 dígitos más parecidos del dataset digits:")
for i, index in enumerate(closest_indices):
    print(f"Índice {i + 1}: {index}, Etiqueta: {digitos.target[index]}")
    print(digitos.images[index].reshape((8, 8)))  # Mostrar la imagen
    print("-" * 40)


# ----------------------
#   ITEM F
# ----------------------

# diccionario para almacenar las frecuencias de los digitos
digit_frequencies = {}

# contar y actualizar frecuencias de los digitos
for idx in closest_indices:
    label = labels[idx]
    if label in digit_frequencies:
        digit_frequencies[label] += 1
    else:
        digit_frequencies[label] = 1

# buscar el que se repite mas
most_common = 0
max_count = 0
for label, count in digit_frequencies.items():
    if count > max_count:
        most_common = label
        max_count = count
      
#si 2 o 3 son iguales
if max_count >= 2: 
    print("\n Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número" , most_common)
else:
  # Busca el que tenga la distancia eclidiana mas pequenia
    min_distance = min(closest_distances)
    min_distance_index = closest_distances.index(min_distance)
    closest_digit = labels[closest_indices[min_distance_index]]
    print("\n Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número", closest_digit)

#imprimir
closest_digit = labels[min_distance_index]
print("\n Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número", closest_digit)
      
# ----------------------
#   ITEM G
# ----------------------
    
          
def calcular_distancia_a_promedios(new_digit, average_images):
    min_distance = float('inf')
    closest_average_digit = None

    for i in range(10):
        distance = euclidean_distance(new_digit.flatten(), average_images[i].flatten())
        if distance < min_distance:
            min_distance = distance
            closest_average_digit = i

    return closest_average_digit, min_distance

closest_average_digit, min_distance_to_average = calcular_distancia_a_promedios(img_procesada, average_images)
print(f"\nSoy la inteligencia artificial versión 2, y he
detectado que el dígito ingresado corresponde al número {closest_average_digit}”, donde {closest_average_digit} es 
un número entre 0 y 9.")

            







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