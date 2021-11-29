import flask
from flask import request, jsonify, render_template
import json
import random
from fetch import Subscribe

app = flask.Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    source = Subscribe()
    data = json.dumps(source.fetch_update(), indent=1)
    path = '/home/swarm-'+str(random.randint(1, 1000))+'.json'
    # path = './swarm-'+str(random.randint(1, 1000))+'.json'
    f = open(path, 'w')
    f.write(data)
    f.close()
    return jsonify(data)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
