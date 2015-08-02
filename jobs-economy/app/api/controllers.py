from flask import Blueprint
from flask import current_app as app

api = Blueprint('api', __name__, url_prefix='/')

@api.route('/', methods=['GET'])
def index():        
    return 'Hello world'
