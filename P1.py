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
