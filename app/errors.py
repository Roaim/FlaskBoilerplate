from flask import json, jsonify
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import HTTPException

from .exceptions import InvalidUsage
from .status_message import get_status_message


def handle_errors(app):
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(SQLAlchemyError)
    def handle_database_exception(e):
        msg = e.__dict__['orig'].args[0]
        res = jsonify({
            'message': msg
        })
        res.status_code = 500
        return res

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        res = e.get_response()
        res.data = json.dumps({
            'status': e.code,
            'message': get_status_message(e.code, e.name)
        })
        res.content_type = 'application/json'
        return res
