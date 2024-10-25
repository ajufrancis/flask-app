from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    file_info = None

    if request.method == 'POST':
        # Handle checkbox selection
        animal = request.form.get('animal')
        if animal:
            image_url = url_for('static', filename=f'images/{animal}.jpg')

        # Handle file upload
        uploaded_file = request.files.get('file')
        if uploaded_file and uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            file_info = {
                'name': filename,
                'size': os.path.getsize(filepath),
                'type': uploaded_file.content_type
            }

    return render_template('index.html', image_url=image_url, file_info=file_info)

if __name__ == '__main__':
    app.run(debug=True)

