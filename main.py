from flask import Flask, request, render_template
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/blur', methods=['POST'])
def blur_image():
    return request.get_data();