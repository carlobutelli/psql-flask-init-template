#!/usr/bin/env python3
from datetime import datetime

import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column

from api.core.db_manager import db, get_db


class User(db.Model):
    __tablename__ = "user"

    uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    name = db.Column(db.String(36), nullable=False, default=False)
    surname = db.Column(db.String(36), nullable=False, default=False)
    username = db.Column(db.String(36), nullable=False, default=False)
    email = db.Column(db.String(36), nullable=False, index=True)
    password = db.Column(db.String(50), nullable=False, index=True)

    timestamp_created = db.Column(db.DateTime, unique=False, nullable=False, index=True, default=datetime.utcnow())
    timestamp_edited = db.Column(db.DateTime, unique=False, nullable=False, index=True, default=datetime.utcnow())
    deleted = db.Column(db.Boolean(), nullable=False, default=False)

    def save(self) -> None:
        db_instance = get_db()
        self.timestamp_edited = datetime.utcnow()
        db_instance.session.add(self)
        db_instance.session.commit()

    def delete(self) -> None:
        db_instance = get_db()
        self.deleted = True
        db_instance.session.add(self)
        db_instance.session.commit()
