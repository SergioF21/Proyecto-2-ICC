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
        for i in range(10):
            mostrar_average_image(i)
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
