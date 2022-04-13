import secrets, sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(512)

# In order to test local, switched to a SQLITE3 DB, and host
DB_URL = 'sqlite:///friends.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

login = LoginManager(app)
login.login_view = 'login'

hashpass = Bcrypt(app)

db = SQLAlchemy(app)

from friends import routes
