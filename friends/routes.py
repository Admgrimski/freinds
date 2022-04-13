from re import L
from time import gmtime
from friends import app, hashpass, db
from flask import render_template, url_for, redirect, request, flash
from friends.models import Friends, Posts
from flask_login import current_user, login_required, login_user, logout_user
from friends.forms import RegistrationForm, LoginForm, ProfieUpdateForm


@app.route("/")
@app.route("/home")
@login_required
def home():
    """
    Friends Home Page to Render in Flask
    """
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Friend Login Page to Render in Flask
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        friend = Friends.query.filter_by(username=form.username.data).first()
        if friend and hashpass.check_password_hash(friend.password, form.password.data):
            login_user(friend, remember=form.remember_session.data)
            next_query = request.args.get('next')
            return redirect(next_query) if next_query else redirect(url_for('profile'))
        else:
            flash('Login in Failure', 'danger')
    return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Friend Register Page to Render in Flask
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        
        gen_hashed_password = hashpass.generate_password_hash(form.password.data).decode('utf-8')
        friend = Friends(username=form.username.data,
        password=gen_hashed_password, email=form.email.data, display_name=form.username.data)
        try:
                db.session.add(friend)
                db.session.commit()
                flash(f'Account created for {form.username.data}!', 'success')
                return redirect(url_for('login'))
        except:
            flash('Creation of account has falied,please try again', 'danger')
            return redirect(url_for('register'))
        
    else:
        return render_template("register.html", title='Register', form=form)

@app.route("/profile")
@login_required
def profile():
    form = ProfieUpdateForm()
    profile_image = url_for('static', filename='friendpics/' + current_user.friend_image)
    return render_template('profile.html', title='Profile', profile_image=profile_image, form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
        logout_user()
        return redirect(url_for('home'))
