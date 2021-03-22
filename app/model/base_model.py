from datetime import datetime

from . import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_by_user_id = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def set_user_id(self, uid):
        self.created_by_user_id = uid
        return self

    def create(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
        return self

    def update(self):
        self.updated_at = datetime.now()
        db.session.commit()
        return self
