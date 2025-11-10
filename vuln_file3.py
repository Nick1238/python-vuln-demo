# vuln_file3.py
import flask
from flask import request
import yaml
import base64
import logging

app = flask.Flask(__name__)

@app.route('/api/unsafe-load')
def unsafe_load():
    # Уязвимость: YAML unsafe load
    data = request.args.get('data')
    obj = yaml.load(data, Loader=yaml.FullLoader)
    return str(obj)

@app.route('/api/debug')
def debug():
    # Уязвимость: информации о внутреннем устройстве
    return str(request.__dict__)

@app.route('/api/unprotected')
def unprotected():
    # Уязвимость: отсутствие проверки авторизации
    return "protected data"

@app.route('/api/base64-decode')
def base64_decode():
    # Уязвимость: отсутствие проверки ввода
    data = request.args.get('data')
    return base64.b64decode(data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
