# apptwo

Creating and running a minimal flask project


Prerequisites:

Globally install python (will install pip and virtualenv globally as well)
Both Python 2.7 or Python 3.3 will work but Python 2.7 is recommended.

Open a new terminal tab and type:

virtualenv -p $(which python) venv
. venv/bin/activate
pip install Flask
pip freeze > requirements.txt
pip install -r requirements.txt
python app.py

Open a new terminal tab and type:

open http://localhost:3000
