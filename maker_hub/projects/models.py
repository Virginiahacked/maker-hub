"""Models for Projects."""

from datetime import datetime

from maker_hub.database import PkModel, db


class Project(PkModel):
    """Project Model."""

    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(80), nullable=True)
    owner = db.Column(db.String(30), nullable=False)
    public = db.Column(db.Boolean(), default=False)
    created = db.Column(
        db.Timestamp(), nullable=False, default=datetime.now().timestamp
    )
    updated = db.Column(db.Timestamp, nullable=False, default=datetime.now().timestamp)
