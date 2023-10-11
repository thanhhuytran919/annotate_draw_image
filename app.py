from flask import Flask, render_template, request, send_from_directory, make_response, redirect
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/annotate', methods=['POST'])
def annotate():
    # Lấy tọa độ từ yêu cầu POST
    x = int(request.form['x'])
    y = int(request.form['y'])
    w = int(request.form['w'])
    h = int(request.form['h'])

    uploaded_image = request.files['image']
    if uploaded_image:

        filename = 'upload.jpg'
        uploaded_image.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))

        image = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), -1)

        annotated_image_path = os.path.join('static', 'annotated_image.jpg')
        cv2.imwrite(annotated_image_path, image)

        return render_template('annotate.html')
    else:
        return "No image provided."


if __name__ == '__main__':
    app.run()
