# Flask init template
---------------------
This is a simple init template base for starting services with Flask.

---

### Run the App
---------------
First start the database service
```bash
docker-compose up -d
```

Then run the project locally
```
virtualenv -p python3 venv && . venv/bin/activate
pip3 install -r requirements/dev.txt
flask run -p 8080
```

---

### Env variables
--------------------
```bash
export FLASK_APP=web
export FLASK_DEBUG=1
export APP_SETTINGS=Local
export DATABASE_URL=postgresql://webapp:d0nt4get@postgres:5432/app
export DATABASE_TEST_URL=postgresql://webapp:d0nt4get@postgres:5432/app_test
```