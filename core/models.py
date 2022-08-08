from core import db
from datetime import datetime

class ShortUrls(db.Model):
    """
    Database class used for recording URL entries and it's shortened URL.
    """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
