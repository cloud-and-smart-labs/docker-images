import flask
from flask import jsonify
import random

app = flask.Flask(__name__)


@app.route('/delay', methods=['GET'])
def delay():
    response = {}
    response['delay'] = random.randint(1, 10)
    return jsonify(response)


# @app.route('/')
# def home():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
