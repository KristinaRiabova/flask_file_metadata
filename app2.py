from flask import Flask, jsonify, send_file

app = Flask(__name__)


image_paths = {
    'wolf.png': 'images/wolf.png',
    'carrot.jpeg': 'images/carrot.jpeg',
    'notexistingpic': 'images/notexistingpic'
}


@app.route('/images/<path:image_name>', methods=['GET'])
def get_image(image_name):
    if image_name in image_paths:
      
        image_path = image_paths[image_name]
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({'message': 'Image not found'}), 404


@app.route('/', methods=['GET'])
def get_docs():
    return """
    <h1>Documentation</h1>
    <p>Available Endpoints:</p>
    <ul>
    <li>GET /images/{image_name} - Returns the image if it exists.</li>
    <li>GET / - Documentation on available endpoints.</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)
