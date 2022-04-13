"""
    You can either run the friends_database_setup.sql
    or launch python interactive shell 
    and run the follwong commands to create the database
    from friends import db
    db.create_all()
"""

from datetime import datetime
from flask_login import UserMixin
from friends import db, login

class Friends(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(16), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=True, default='first name')
    last_name = db.Column(db.String(50), unique=False, nullable=True, default='last name')
    friend_image = db.Column(db.String(20), nullable=False, default='default.png')
    display_name = db.Column(db.String(30), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Posts', backref='friend', lazy=True)
 

  #  def __repr__(self):
  #      return f"User ('{self.username}', '{self.email}','{self.image_file}')"

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    friend_id = db.Column(db.Integer, db.ForeignKey('friends.id'), nullable=False, )
 #   def __repr__(self):
 #       return f"Post ('{self.title}', '{'date_posted'})"

@login.user_loader
def login_user(friend_id):
    return Friends.query.get(int(friend_id))
