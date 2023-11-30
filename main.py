# main.py
import P2

def main():
    # Ruta de la imagen para probar
    image_path = "img/7.jpg"
    image_path = "static/uploaded-images/ba1eb5a3-c24b-4228-a836-14c9eaa91459.jpg"

    # Procesa la imagen de entrada
    img_procesada = P2.proceso(image_path)

    # Encuentra los dígitos más cercanos utilizando la distancia euclidiana
    closest_indices, closest_distances = P2.find_most_similar_digits(img_procesada, P2.dataset_digits)

    # Calcula la frecuencia de los dígitos más cercanos
    most_common_digit, max_count = P2.calculate_digit_frequencies(closest_indices, P2.labels)

    # Determina el dígito promedio más cercano
    closest_average_digit, min_distance_to_average = P2.calcular_distancia_a_promedios(img_procesada, P2.average_images)

    # Imprime los resultados de ambos métodos
    print(f"\nMétodo de Frecuencia Más Común: {most_common_digit}")
    print(f"Método de Distancia al Promedio Más Cercano: {closest_average_digit}")


if __name__ == "__main__":
    main()
