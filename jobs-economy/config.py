# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database, SQLite
SQLALCHEMY_DATABASE_URI = 'postgresql://hoadmin:ILovePepperoniPizza@raise-effect-db.c1srwyzwwu1a.us-west-2.rds.amazonaws.com:5432/raise_effect'
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
