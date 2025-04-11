from . import db
from datetime import datetime, timezone

# Add any model classes for Flask-SQLAlchemy here

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    poster = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    def __init__(self, title, description, poster):
        if not title or not description or not poster:
            raise ValueError("Title, description, and poster are required.")
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now(timezone.utc)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Movie(title={self.title!r}, created_at={self.created_at.isoformat()!r})>"

    def to_dict(self, message):
        return {
            'message': message,
            'title': self.title,
            'poster': self.poster,
            'description': self.description,
        }