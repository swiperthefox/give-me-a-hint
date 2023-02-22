import os.path
from urllib.request import urlopen
from flask import url_for
from sqlalchemy.exc import SQLAlchemyError

import app
from app.models import Book
from app.database import db
from app.app import socketio

from app.auth import with_valid_token


@socketio.on('new-book')
@with_valid_token
def new_book(uid, book_info):
    print(uid, book_info['title'])
    try:
        cover_img_name = '%s_%s.png' % (book_info['title'], str(uid))
        cover_img_path = os.path.join(app.Config.UPLOAD_DIR, 'covers', cover_img_name)
        save_picture(cover_img_path, book_info['cover'])
        book_info['cover'] = url_for('static', filename='upload/covers/' + cover_img_name)
        book = Book(owner_id=uid, **book_info)
        db.session.add(book)
        db.session.commit()
        books = Book.query.filter_by(owner_id=uid).all()
        books_json = [book.to_dict() for book in books]
        return {
            'success': True,
            'data': books_json
        }
    except SQLAlchemyError:
        return {
            'success': False,
            'error': 'Database insertion error'
        }


@socketio.on('get-book-list')
@with_valid_token
def get_book_list(uid):
    try:
        books = Book.query.filter_by(owner_id=uid).all()
        books_json = [book.to_dict() for book in books]
        return {
            'success': True,
            'data': books_json
        }
    except SQLAlchemyError:
        return {
            'success': False,
            'error': 'Database error'
        }


def save_picture(p, data_url):
    print("path:", p)
    response = urlopen(data_url)
    with open(p, 'wb') as f:
        f.write(response.read())
