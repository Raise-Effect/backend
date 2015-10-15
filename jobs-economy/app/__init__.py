# Import flask and template operators
from flask import Flask, request, jsonify, make_response
from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI application object
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable
from app.api.controllers import api as api_module

# Register blueprint(s)
app.register_blueprint(api_module)


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'errorMessage': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    return make_response(resp, 404)


@app.errorhandler(Exception)
def internal_server_error(error):
    message = {
        'status': 500,
        'errorMessage': 'Internal Server Error: %r' % error
    }
    resp = jsonify(message)
    return make_response(resp, 500)
