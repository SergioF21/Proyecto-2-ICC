import base64
from PIL import Image
import io
import numpy as np

def generate_data_uri_from_numpy_array(numpy_array):
    # Convierte la matriz NumPy en una imagen PIL
    image = Image.fromarray(numpy_array.astype('uint8'))

    # Crea un objeto BytesIO para guardar la imagen en memoria
    image_buffer = io.BytesIO()

    # Guarda la imagen en formato PNG en el objeto BytesIO
    image.save(image_buffer, format='PNG')

    # Codifica la imagen en base64 y genera el URI de datos
    data_uri = 'data:image/png;base64,' + base64.b64encode(image_buffer.getvalue()).decode()

    return data_uri
