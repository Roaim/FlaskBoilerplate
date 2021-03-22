from ..model.address import Country, City
from ..schema.address_schema import country_schema, city_schema, address_schema


def create_country(uid, body):
    country = country_schema.load(body)
    country.set_user_id(uid)
    return country.create()


def list_country():
    return Country.query.all()


def create_city(uid, body):
    city = city_schema.load(body)
    city.set_user_id(uid)
    return city.create()


def list_city(county_id):
    return City.query.filter_by(country_id=county_id).all()


def create_address(uid, body):
    address = address_schema.load(body)
    address.set_user_id(uid)
    return address.create()
