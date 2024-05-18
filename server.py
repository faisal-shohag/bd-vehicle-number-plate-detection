from flask import Flask, render_template
from flask import request, jsonify
import os
import base64
from main import predict


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file.'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file.'
    if file:
        file.save('./uploads/'+file.filename)
        plate_number = predict('./uploads/'+file.filename)
        with open('./cropped/bounded.jpg', "rb") as img_file:
            bounded_img = base64.b64encode(img_file.read()).decode('utf-8')
        with open('./cropped/cropped_0.jpg', "rb") as img_file:
            cropped_img = base64.b64encode(img_file.read()).decode('utf-8')

        return jsonify({
            'message': 'File uploaded successfully', 
            'filename': file.filename,
            'bounded_image': bounded_img,
            'cropped_image': cropped_img,
            'plate': plate_number[1],
            'plate_number': plate_number[0],
            }), 200
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)

