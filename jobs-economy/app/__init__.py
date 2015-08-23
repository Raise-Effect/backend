# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI application object
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from .api import models

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.api.controllers import api as api_module

# Register blueprint(s)
app.register_blueprint(api_module)
