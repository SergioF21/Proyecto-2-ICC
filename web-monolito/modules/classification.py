import numpy as np

def euclidean_distance(img1, img2):
    # Calcular la distancia euclidiana entre dos imágenes
    return np.sqrt(np.sum((img1 - img2) ** 2))

# ----------------------
#   ITEM F
# ----------------------

def calculate_digit_frequencies(closest_indices, labels):
    # Diccionario para almacenar las frecuencias de los dígitos
    digit_frequencies = {}

    # Contar y actualizar frecuencias de los dígitos
    for idx in closest_indices:
        label = labels[idx]
        digit_frequencies[label] = digit_frequencies.get(label, 0) + 1

    # Buscar el dígito que se repite más
    most_common = max(digit_frequencies, key=digit_frequencies.get)
    max_count = digit_frequencies[most_common]

    return most_common, max_count

def find_closest_digit_by_distance(closest_distances, closest_indices, labels):
    # Buscar el dígito con la distancia euclidiana más pequeña
    min_distance = min(closest_distances)
    min_distance_index = closest_distances.index(min_distance)
    closest_digit = labels[closest_indices[min_distance_index]]

    return closest_digit

# ----------------------
#   ITEM G
# ----------------------
    
          
def calcular_distancia_a_promedios(new_digit, average_images):
    min_distance = float('inf')
    closest_average_digit = None

    for i in range(10):
        # print("Tipo de datos de 'average_images[i]':", average_images[i].dtype)  # Agregar este print
        distance = euclidean_distance(new_digit.flatten(), average_images[i].flatten())
        if distance < min_distance:
            min_distance = distance
            closest_average_digit = i

    return closest_average_digit, min_distance

def find_most_similar_digits(new_digit, dataset_digits):
    # Inicializar una lista para almacenar las distancias y los índices de los dígitos
    distances = []
    new_flat = new_digit.flatten()

    # Calcular la distancia euclidiana para cada dígito en el dataset
    for i, digit in enumerate(dataset_digits):
        # print("Tipo de datos de 'digit':", type(digit))  # Agregar este print
        distance = euclidean_distance(new_flat, digit)
        distances.append((distance, i))

    # Ordenar la lista de distancias de menor a mayor
    distances.sort()

    # Obtener los índices de los 3 dígitos más cercanos
    closest_indices = [index for _, index in distances[:3]]

    return closest_indices, [distance for distance, _ in distances[:3]]


