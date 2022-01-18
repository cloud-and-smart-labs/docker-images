import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/save/<string:filename>/<string:content>')
def save(filename, content):
    response = {}
    response['filename'] = filename
    response['content'] = content
    with open(f"/tmp/{filename}", "w") as f:
        f.write(f"{content}")
        f.close()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
