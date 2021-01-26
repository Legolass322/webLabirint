from flask import Flask
from flask_login import LoginManager
from data import db_session
from settings import SECRET_KEY, STR_CONN_TO_MYSQL


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init(STR_CONN_TO_MYSQL)