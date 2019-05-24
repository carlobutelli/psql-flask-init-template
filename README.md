# Loki ID Verification Service
Loki is the Nxchange Identity verification service used along with the Mitek system in order to validate new users' 
identity. 

# Project Requirements
Loki is a Python 3.7 project implemented by using Flask. To run the project make sure you have the following dependencies installed:
* Python 3 (3.7)
* pip3
* virtualenv

# Run the project
To run the project locally make sure you have all the project requirements installed and run (from the root directory):

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements/base.txt
$ export FLASK_APP=loki
$ export FLASK_DEBUG=1
$ cd loki
$ flask run
```

## Run tests

To run the tests activate the virtual environment and run the following commands:

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements/base.txt
$ export FLASK_APP=loki
$ export FLASK_DEBUG=1
$ pytest
```


#### HAPPY CODING

If you prefer to run the project in a docker environment you can also simply run Loki with:
```
$ docker-compose build
$ docker-compose up
````