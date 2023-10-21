# Simple_CRUD_Flask

<strong>A simple crud example in Flask + SQLAlchemy + SQLite</strong>

How to run (windows):

<strong>VIRTUAL ENVIRONMENT</strong>

<strong>create a virtual environment:</strong><br>
(terminal) py -3 -m venv venv_simple_crud

<strong>activate the venv_simple_crud:</strong><br>
(terminal).\venv_simple_crud\Scripts\activate

<strong>INSTALL FLASK</strong>

(terminal) pip install -r requirements.txt <br>

<strong>CREATE A SQLITE DATABASE </strong>

(terminal) flask shell

(terminal) from app import db

(terminal) db.create_all()

(terminal) exit()

<strong>RUN!</strong>

(terminal) Flask run
