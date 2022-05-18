from flask import Flask, render_template, jsonify
import utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/books', methods=['GET'])
def read_books():
    books = utils.load_books_from_json()
    return jsonify(books)


@app.route('/books/<book_id>', methods=['GET'])
def read_book(book_id):
    return jsonify({"content": f"Получаем книжку {book_id}"})


@app.route('/books', methods=['POST'])
def create_book():
    return jsonify({"content": "Создаем книжку"})


@app.route('/books/‹book_id›', methods=['PUT'])
def update_book(book_id):
    return jsonify({"content": f"Обновляем книжку {book_id}"})


@app.route('/books/‹book_id›', methods=['DELETE'])
def delete_book(book_id):
    return jsonify({"content": f"Удаляем книжку {book_id}"})


if __name__ == '__main__':
    app.run()
