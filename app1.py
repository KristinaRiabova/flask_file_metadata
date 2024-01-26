from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

def parse_url(url):
    try:
        parsed_url = urlparse(url)
        scheme = parsed_url.scheme
        domain = parsed_url.netloc
        path_steps = parsed_url.path.strip('/').split('/')
        query_params = parse_qs(parsed_url.query)

        result = f'It has {scheme} protocol,\n'
        result += f'Domain is \'{domain}\'\n'
        result += f'The path to the resource has {len(path_steps)} steps - {", ".join(path_steps)}\n'

        if query_params:
            result += f'Query parameters ({len(query_params)}) are present: {query_params}\n'

        return result

    except Exception as e:
        return f'Error parsing URL: {str(e)}'

@app.route('/url-info', methods=['POST'])
def url_info():
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL not provided in the request'}), 400

        result = parse_url(url)
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
