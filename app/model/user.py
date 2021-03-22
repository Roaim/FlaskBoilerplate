from .base_model import db, BaseModel
from .address import Address
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    name = db.Column(db.String(55))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(20), unique=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id', ondelete='CASCADE'))
    address = db.relationship(Address, lazy='subquery')


class PasswordUser(BaseModel):
    password_hash = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    user = db.relationship(User, lazy='subquery')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
