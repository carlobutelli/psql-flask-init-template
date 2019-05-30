# Loki ID Verification Service
Loki is the Nxchange Identity verification service used along with the Mitek system in order to validate new users' 
identity. 

## Project Requirements
Loki is a Python 3.7 project implemented by using Flask. To run the project make sure you have the following dependencies installed:
* Python 3 (3.7)
* pip3
* virtualenv

## Run the project
To run the project locally make sure you have all the project requirements installed and run (from the root directory):

```
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r requirements/dev.txt
export FLASK_APP=loki
export FLASK_DEBUG=1
export FLASK_ENV=Local
flask run
```
If you prefer to run the project in a docker environment you can also simply run Loki with:
```
docker-compose build
docker-compose up
````
Application running in the container is isolated from the local code so, after some changes, to be able to see the 
updates the app needs to be built again.

## Run tests

To run the tests activate the virtual environment and run the following commands:

```
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r requirements/test.txt
export FLASK_APP=loki
export FLASK_DEBUG=1
export FLASK_ENV=Testing
pytest pytest --disable-warnings
```


## Documentation
API documentation with requests' types, urls and endpoints' descriptions can be found at

  `GET` /apidocs
