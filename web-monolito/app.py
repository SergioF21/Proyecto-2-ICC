import base64
from flask import Flask, jsonify, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from PIL import Image as PILImage
from io import BytesIO

from modules.classification import find_most_similar_digits, calculate_digit_frequencies, calcular_distancia_a_promedios
from modules.processing import proceso
from modules.visualization import DATASET_DIGITS, AVERAGE_IMAGES, LABELS
from modules.htmlUtilities import generate_data_uri_from_numpy_array
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

# Modelo
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    prediction_method_1 = db.Column(db.String(200)) 
    prediction_method_2 = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Image {self.id}>'

def create_tables():
    db.create_all()

with app.app_context():
    create_tables()

# Endpoints

@app.route('/')
def home():
    
    # Genera las imágenes promedio (supongamos que tienes AVERAGE_IMAGES correctamente definidas)
    average_images_html = ""
    for i in range(len(AVERAGE_IMAGES)):
        image_data_uri = generate_data_uri_from_numpy_array(AVERAGE_IMAGES[i])  # Implementa esta función
        average_images_html += f'<div class="col-md-1"><img src="{image_data_uri}" alt="Average Image {i}" class="img-fluid"></div>'

    
    return render_template('home.html', average_images_html=average_images_html)


# analizar y guardar una imagen
@app.route('/analyze', methods=['POST'])
def analyze():
    image_base64 = request.form.get('image')

    if image_base64:
        try:
            # Decodifica la imagen base64 en datos binarios
            image_data = base64.b64decode(image_base64.split(",")[1])  # Ignora el encabezado "data:image/png;base64,"
            
            # Genera un nombre de archivo único usando UUID
            filename = str(uuid.uuid4())
            # Define la ruta donde se guardará la imagen en formato .png
            filepath = os.path.join('static/uploaded-images', filename + '.jpg')

            # Guarda la imagen binaria en el servidor como .png
            with open(filepath, 'wb') as f:
                f.write(image_data)

            # Crea un registro en la base de datos con la ruta del archivo .png
            new_image = Image(file_path=filepath)
            db.session.add(new_image)
            db.session.commit()
            
            

            # Procesar la imagen y obtener predicciones
            processed_image = proceso(filepath)
            print("processed_img", processed_image)
            closest_indices, _ = find_most_similar_digits(processed_image, DATASET_DIGITS)
            most_common_digit, _ = calculate_digit_frequencies(closest_indices, LABELS)
            closest_average_digit, _ = calcular_distancia_a_promedios(processed_image, AVERAGE_IMAGES)

            # Actualizar registro en la base de datos con los resultados
            new_image.prediction_method_1 = str(most_common_digit)
            new_image.prediction_method_2 = str(closest_average_digit)
            db.session.commit()

            return jsonify({
                    'result': "Imagen guardada y procesada correctamente",
                    'prediction_method_1': str(most_common_digit),
                    'prediction_method_2': str(closest_average_digit)
                            })

        except Exception as e:
            return jsonify(error="Error al procesar la imagen base64: " + str(e))
    else:
        return jsonify(error="No se ha proporcionado una imagen base64")

@app.route('/image/<int:index>')
def get_image(index):
    # Obtén la imagen del array
    img_array = AVERAGE_IMAGES[index]

    # Escala la imagen
    img = PILImage.fromarray((img_array * 255).astype('uint8'))  # Asegúrate de que sea del tipo correcto
    img = img.resize((400, 400), PILImage.BICUBIC)  # Cambia 150x150 al tamaño deseado

    # Guarda la imagen en un buffer
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    return send_file(img_buffer, mimetype='image/png')


@app.route('/upload', methods=['GET'])
def upload_image():
    return redirect(url_for('list_images'))

@app.route('/list_images', methods=['GET'])
def list_images():
    images = Image.query.all()
    return render_template('list_images.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
