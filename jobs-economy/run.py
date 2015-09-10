# Run a test server.
# Requires software from setup/dev-requirements
from flask import Flask
from flask.ext.runner import runner
from app import app

runner = Runner(app)
runner.run()
