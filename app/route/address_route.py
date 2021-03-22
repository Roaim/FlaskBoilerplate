from flask import Blueprint, request

from ..schema.address_schema import address_schema, city_schema, city_list_schema, country_schema, country_list_schema
from ..service import address_service as service
from ..decorators import admin_required, auth_required

bp = Blueprint('address', __name__)


@bp.route('/countries', methods=('POST',))
@admin_required
def create_country(uid):
    body = request.get_json()
    return country_schema.jsonify(service.create_country(uid, body))


@bp.route('/countries', methods=('GET',))
@auth_required
def list_country():
    return country_list_schema.jsonify(service.list_country())


@bp.route('/cities', methods=('POST',))
@admin_required
def create_get_city(uid):
    body = request.get_json()
    return city_schema.jsonify(service.create_city(uid,body))


@bp.route('/countries/<country_id>/cities', methods=('GET',))
@auth_required
def list_city(country_id):
    return city_list_schema.jsonify(service.list_city(country_id))


@bp.route('/addresses', methods=('POST',))
@auth_required
def create_address(uid):
    body = request.get_json()
    return address_schema.jsonify(service.create_address(uid, body))
