import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Function name of a route
login_manager.login_message = 'Please login first!'
login_manager.login_message_category = 'info'
mail = Mail(app)


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