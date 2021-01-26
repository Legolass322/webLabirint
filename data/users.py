import sqlalchemy
from sqlalchemy.dialects.mysql import VARCHAR
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                            primary_key=True,
                            autoincrement=True)
    login = sqlalchemy.Column(VARCHAR(128))
    email = sqlalchemy.Column(VARCHAR(128))
    password = sqlalchemy.Column(VARCHAR(128))
    admin = sqlalchemy.Column(VARCHAR(128), default='0')

    def set_password(self, _pass):
        self.password = generate_password_hash(_pass)

    def check_password(self, _pass):
        return check_password_hash(self.password, _pass)