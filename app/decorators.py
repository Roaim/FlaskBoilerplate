import inspect
from functools import wraps

from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims, get_jwt_identity

from .exceptions import InvalidUsage


def admin_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['is_admin']:
            identity = get_jwt_identity()
            if 'uid' in inspect.signature(fn).parameters:
                kwargs['uid'] = identity
            return fn(*args, **kwargs)
        else:
            raise InvalidUsage('Admin only', 403)

    return decorator


def auth_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if 'uid' in inspect.signature(fn).parameters:
            kwargs['uid'] = identity
        return fn(*args, **kwargs)

    return decorator
