# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI application object
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

#from .api import models

# Import a module / component using its blueprint handler variable
from app.api.controllers import api as api_module

# Register blueprint(s)
app.register_blueprint(api_module)
