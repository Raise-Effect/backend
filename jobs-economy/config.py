# Statement for enabling the development environment

DEBUG = True

# Define the application directory
import os
import configparser
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

config = configparser.ConfigParser()
config.read('secrets.cfg')

POSTGRESQL_USER = config['database']['user']
POSTGRESQL_PASSWORD = config['database']['password']

# Define the database, SQLite
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@raise-effect-db.c1srwyzwwu1a.us-west-2.rds.amazonaws.com/raise_effect'.format(
    user=POSTGRESQL_USER,
    password=POSTGRESQL_PASSWORD,
)
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using another.
THREADS_PER_PAGE = 2

# Enable protections agains CSRF
CSRF_ENABLED = True

# Use a secure key
CSFR_SESSION_KEY = "secret"

# Secret for signing cookies
SECRET_KEY = "secret"
