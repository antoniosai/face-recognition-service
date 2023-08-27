import os
import requests
import numpy as np
import face_recognition
from PIL import Image
import datetime
from io import BytesIO
from flask import Flask, request, jsonify

app = Flask(__name__)

def download_image(url):
    response = requests.get(url)
    image_content = response.content
    image = Image.open(BytesIO(image_content))
    return image

def compare_faces(image_path1, image_url2):
    # Load and process the first image
    image1 = face_recognition.load_image_file(image_path1)
    face_encoding1 = face_recognition.face_encodings(image1)[0]

    # Download and process the second image from URL
    image2 = download_image(image_url2)
    image2_rgb = np.array(image2.convert('RGB'))
    face_encoding2 = face_recognition.face_encodings(image2_rgb)[0]

    # Compare face encodings
    are_same_person = face_recognition.compare_faces([face_encoding1], face_encoding2)[0]
    
    return int(are_same_person)  # Convert boolean to integer

@app.route('/compare', methods=['POST'])
def compare_images():
    try:
        # Get uploaded image from HTTP POST
        uploaded_image = request.files['image']
        uploaded_image_path = 'uploaded_image.jpg'
        uploaded_image.save(uploaded_image_path)

        # URL of the image for comparison
        url_image = request.form['url']

        # Compare images
        result = compare_faces(uploaded_image_path, url_image)

        os.remove(uploaded_image_path)  # Delete the temporary uploaded image

        current_datetime = datetime.datetime.now()

        # Format the datetime as a string with a custom format
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        if result != 1:
            return jsonify({"message": "Not OK! They are not even similar!", "result": False, "time": formatted_datetime}), 422
        else:
            return jsonify({"message": "Accepted! Both of Images are similar!", "result":  True, "time": formatted_datetime}), 200

        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
