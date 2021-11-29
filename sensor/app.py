import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/sensor/<float:temp>')
def show_post(temp):
    response = {}
    response['sensor_data'] = temp
    response['actuation'] = temp*10
    with open("/home/flask.txt", "a") as f:
        f.write(str(response)+'\n')
        f.close()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
