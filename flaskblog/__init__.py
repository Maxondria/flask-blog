from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee9ce57217cad182c77c88b36f62e79c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


@app.before_first_request
def create_tables():
    db.create_all()


'''
 [App routes]

This module imports routes but routes module too import [app] from this module,
This technically would mean circular imports.
However, importing this routes module below after declaring [app]
means that by the time python runs the routes import, app will already be available
to routes
'''
from flaskblog import routes