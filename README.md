# loki-id-verification-service

# Run the project
To run the project locally make sure you have all the project requirements installed and run (from the root):

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install -r requirements/base.txt
$ export FLASK_APP=loki
$ export FLASK_DEBUG=1
$ cd loki
$ flask run
```