from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_migrate import Migrate

from app.database import db
from app.config import Config
from app.models import User, Book, Cell, Annotation 

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

socketio = SocketIO(app, cors_allowed_origins="*")

from app import auth, book


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

# @socketio.on('register')
# def handle_register_event(json, methods=['GET', 'POST']):
#     print('received register event: ' + str(json))
#     socketio.emit('registered')


if __name__ == '__main__':
    print("running server")
    socketio.run(app)