from flask import Blueprint, request, jsonify

from ..schema.user_schema import user_schema, user_list_schema
from ..service import user_service as service
from ..exceptions import InvalidUsage
from ..decorators import admin_required, auth_required

bp = Blueprint('users', __name__)


@bp.route('/register', methods=('POST',))
def register():
    body = request.get_json()
    method = body.get('method')
    if method is None:
        raise InvalidUsage('Method field is missing')
    if method == 'password' and body.get('password') is None:
        raise InvalidUsage('Password filed is missing')
    user_body = body.get('user')
    if user_body is None:
        raise InvalidUsage('User field is missing')
    user = service.create_user(user_body)
    if method == 'password':
        password = body['password']
        service.create_password_user(user.id, password)
    return user_schema.jsonify(user)


@bp.route('/login', methods=('POST',))
def login():
    body = request.get_json()
    method = body.get('method')
    if method is None:
        raise InvalidUsage('Method field is missing')
    elif method == 'password':
        token = service.generate_token(body)
        return jsonify(token)
    else:
        raise InvalidUsage('Unknown login method')


@bp.route('/users', methods=('GET',))
@admin_required
def list_user():
    return user_list_schema.jsonify(service.list_user())


@bp.route('/users/me', methods=('GET',))
@auth_required
def get_me(uid):
    return user_schema.jsonify(service.get_user(uid))
