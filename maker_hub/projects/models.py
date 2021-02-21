"""Models for Projects."""

from datetime import datetime

from maker_hub.extensions import db


class Project(db.Model):
    """Project Model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(80), nullable=True)
    owner = db.Column(db.String(30), nullable=False)
    public = db.Column(db.Boolean(), default=False)
    created = db.Column(
        db.Timestamp(), nullable=False, default=datetime.now().timestamp
    )
    updated = db.Column(db.Timestamp, nullable=False, default=datetime.now().timestamp)
