from flask import redirect, render_template, url_for, request
from flask_login import current_user, logout_user, login_user
from data import db_session
from init import app, login_manager
from functions import set_urls
import json


@app.route('/', methods=['GET'])
def index():
    params = {}
    set_urls(params)
    return render_template('index.html', **params)


@app.route('/signin', methods=['GET'])
def signin():
    if current_user.is_authenticated:
        return redirect('/')
    else:
        params = {}
        set_urls(params)
        return render_template('signin.html')


# Backend here
@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    session.close()
    return user


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
         logout_user()
    else:
         pass
    return redirect('/')