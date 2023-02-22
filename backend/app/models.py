from datetime import datetime

from .app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer, default=0)
    register_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(512))
    cover = db.Column(db.String(512))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.Index('idx_author_title', owner_id, title, unique=True),
    )

    def __repr__(self):
        return f'<Book {self.name}'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'cover': self.cover,
            'ctime': self.create_time.isoformat(),
            'mtime': self.last_update.isoformat(),
            'owner': self.owner_id
        }


class Cell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    previous_id = db.Column(db.Integer, db.ForeignKey('cell.id'))
    original = db.Column(db.String)
    type = db.Column(db.String(10)) # 'md', 'img', 'tex', 'asciimath', 'plain'
    html = db.Column(db.String)
    is_question = db.Column(db.Boolean)
    is_answer = db.Column(db.Boolean)


class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'))
    original = db.Column(db.String)
    type = db.Column(db.String(10)) # 'md', 'tex', 'asciimath', 'plain'
    html = db.Column(db.String)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    
    