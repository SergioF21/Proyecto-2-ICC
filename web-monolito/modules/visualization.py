from sklearn.datasets import load_digits
import numpy as np

# Cargar el conjunto de datos digits
DATASET_DIGITS = load_digits()

# Obtener las imágenes y las etiquetas
IMAGES = DATASET_DIGITS.images
LABELS = DATASET_DIGITS.target
DATASET_DIGITS = DATASET_DIGITS.data
# Crear una matriz para almacenar las imágenes promedio
AVERAGE_IMAGES = np.zeros((10, 8, 8))

# Calcular la imagen promedio para cada dígito
for i in range(10):
    DIGIT_IMAGES = IMAGES[LABELS == i]
    AVERAGE_IMAGES[i] = np.mean(DIGIT_IMAGES, axis=0)

