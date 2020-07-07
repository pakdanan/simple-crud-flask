# Simple_CRUD_Flask

<strong>A simple crud example in Flask + SQLAlchemy + SQLite</strong>

How to run (linux/debian):

<strong>VIRTUAL ENVIRONMENT</strong>

<strong>create a virtual environment:</strong><br>
(terminal) python3 -m venv venv_simple_crud

<strong>activate the venv_simple_crud:</strong><br>
(terminal)source venv_crud/bin/activate

<strong>INSTALL FLASK</strong>

(terminal) pip3 install -r requirements.txt <br>

<strong>export default Flask environments variables:</strong><br>
(terminal) export FLASK_APP=app.py<br>
(terminal) export FLASK_ENV=development

<strong>CREATE A SQLITE DATABASE </strong>

(terminal) Flask Shell

(terminal) from app import db

(terminal) db.create_all()

(terminal) exit()

<strong>RUN!</strong>

(terminal) Flask run


    
