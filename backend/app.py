from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


BOOKS = [
    {
        'title': 'Software Telemetry',
        'author': 'Jamie Riedesel',
        'read': True
    },
    {
        'title': 'Grokking Streaming Systems',
        'author': 'Josh Fischer and Ning Wang',
        'read': False
    },
    {
        'title': 'Rust in Action',
        'author': 'Tim McNamara',
        'read': True
    }
]


@app.route('/api/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
        })


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/<path:fallback>")
def fallback(fallback):
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
