from typing import Union
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import SQLAlchemyError
import jwt
from jwt.exceptions import InvalidTokenError
from app.models import User
from app.database import db
from app.app import socketio

ADMIN = 1
STUDENT = 0

JWT_SECRET = 'chap1aole!'
bcrypt = Bcrypt()


@socketio.on('register')
def create_user(d):
    # create a user
    pw_hash = bcrypt.generate_password_hash(d['password'])
    user = User(username=d['name'], 
        email=d['email'], 
        role=d.get('role', STUDENT),
        password_hash=pw_hash)
    db.session.add(user)
    try:
        db.session.commit()
        return True
    except SQLAlchemyError:
        return False


@socketio.on('login')
def login(d):
    name = d['name']
    password = d['password']
    user: Union[User, None] = User.query.filter_by(username=name).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        token = jwt.encode({'uid': user.id}, JWT_SECRET, algorithm='HS256')
    else:
        token = ''
    return {'name': name, 'token': token}


@socketio.on('verify-token')
def verify_token(token):
    try:
        tmp = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return True
    except InvalidTokenError:
        return False


def with_valid_token(func):
    def wrapper(token, *args, **kws):
        try:
            print(token)
            token = jwt.decode(token,JWT_SECRET, algorithms=['HS256'])
            uid = token['uid']
            print(uid)
            return func(uid, *args, **kws)
        except InvalidTokenError as e:
            print(e)
            print("invalid token provided")
            return {
                'success': False,
                'error': 'Invalid login token'
            }
    return wrapper
