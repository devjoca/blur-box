import os
from worker.worker import generate_blur
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/blur', methods=['POST'])
def blur_image():
    image = request.form['image']
    image = image[image.find(",")+1:]
    base_64 = generate_blur(image)
    return jsonify(base_64)