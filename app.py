import os
from flask import (Flask, 
                   render_template, 
                   request, 
                   url_for, 
                   redirect, 
                   flash)
from flask_sqlalchemy import SQLAlchemy

#app object start  
app = Flask(__name__)

#app config
app.config['SECRET_KEY'] = 'My_SeCR3t!'

# database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple_crud.db'

db = SQLAlchemy(app)


# class User inherit from sql alchemy class
class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User.{self.name},{self.age}'


# ROUTES

# REDIRECT FOR READ PAGE
@app.route('/')
def index():
    return redirect(url_for('read'))


# CREATE PAGE
@app.route('/create', methods=['GET','POST'])
def create():

    if request.method == 'POST':
        name =  request.form['name']
        age = request.form['age']

        user = User(name=name,age=age)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('read'))
    else:
        return render_template('create.html') 


# READ PAGE
@app.route('/read')
def read():
    
    users = User.query.all()
    return render_template('read.html', users=users)

# UPDATE PAGE
@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        user = User.query.filter_by(id=id).first() 
        user.name = name
        user.age = age
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('read'))
    else:
        user = User.query.filter_by(id=id).first()   
        return render_template('update.html', user=user)


# DELETE PAGE redirect for read page and flash a message with deleted user
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):

    if request.method == 'GET':
        
        user = User.query.filter_by(id=id).first() 
        db.session.delete(user)
        db.session.commit()

        flash (f'User {user.name} deleted!')
        return redirect(url_for('read'))


if __name__ == "__main__":
    app.run(debug=True)