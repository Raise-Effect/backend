# Hack Oregon Jobs Economy Backend
This is the backend REST API for Hack Oregon's Job's Economy team. It consists of a Flask application, as well as Vagrant and Docker scripts.

##### To run locally without Vagrant and Docker: #####
`cd jobs-economy`

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`python run.py`

Visit `0.0.0.0:8080` in your browser.


##### To run with Vagrant and the Docker provisioner: #####
You must have Vagrant installed, along with Virtualbox.

`Vagrant up`

Wait for Vagrant and Docker to complete their magic, then visit `0.0.0.0:8080` in your browser.
