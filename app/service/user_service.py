from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from sqlalchemy import or_

from ..exceptions import InvalidUsage
from ..model.user import User, PasswordUser
from ..schema.user_schema import user_schema


def create_user(user_body):
    try:
        user = user_schema.load(user_body)
    except ValidationError as e:
        raise InvalidUsage(e.messages)
    return user.create()


def create_password_user(user_id, password):
    password_user = PasswordUser(user_id=user_id)
    password_user.set_password(password)
    return password_user.create()


def list_user():
    return User.query.all()


def generate_token(body):
    email_or_phone = body['email_or_phone']
    password = body['password']
    user = User.query.filter(
        or_(User.email.is_(email_or_phone), User.phone.is_(email_or_phone))
    ).first()
    if user is None:
        raise InvalidUsage('User not found', 404)
    pw_user = PasswordUser.query.filter(PasswordUser.user_id.is_(user.id)).first()
    if pw_user is None:
        raise InvalidUsage('User not found', 404)
    elif pw_user.check_password(password):
        token = create_access_token(identity=user.id, user_claims={'is_admin': user.is_admin})
        return {
            'token': token,
            'user': user_schema.dump(user)
        }
    else:
        raise InvalidUsage('Wrong password', 401)


def get_user(uid):
    return User.query.filter(User.id.is_(uid)).first_or_404()