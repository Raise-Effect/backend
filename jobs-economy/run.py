# Run a test server.
# Requires libraries from setup/dev-requirements.txt
from flask.ext.runner import Runner
from app import app

runner = Runner(app)
runner.run()
