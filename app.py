from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/metadata', methods=['POST'])
def metadata():

    if 'file' not in request.files or 'search_string' not in request.form:
        return jsonify({'error': 'Missing file or search_string in the request'}), 400

    file = request.files['file']
    search_string = request.form['search_string']


    if file and allowed_file(file.filename):

        text = file.read().decode('utf-8')

        metadata = {
    'length_of_text': len(text),
    'amount_of_alphanumeric_symbols': sum(c.isalnum() for c in text),
    'occurrences_of_string': text.lower().count(search_string.lower())
}


        return jsonify(metadata)

    return jsonify({'error': 'Invalid file'}), 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
 #curl -X POST -F "file=@sample.txt" -F "search_string=text" http://127.0.0.1:5000/metadata