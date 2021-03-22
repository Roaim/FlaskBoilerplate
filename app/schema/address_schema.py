from marshmallow import post_load, INCLUDE
from marshmallow.fields import Nested

from . import BASE_MODEL_FIELDS
from ..model import ma
from ..model.address import Address, City, Country


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        unknown = INCLUDE

    city = Nested(lambda: CitySchema(exclude=BASE_MODEL_FIELDS))

    @post_load
    def create_model(self, data, **kwargs):
        return Address(**data)


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        unknown = INCLUDE

    country = Nested(lambda: CountrySchema(exclude=BASE_MODEL_FIELDS))

    @post_load
    def create_model(self, data, **kwargs):
        return City(**data)


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country

    @post_load
    def create_model(self, data, **kwargs):
        return Country(**data)


address_schema = AddressSchema()
city_schema = CitySchema()
city_list_schema = CitySchema(many=True, exclude=('country',))
country_schema = CountrySchema()
country_list_schema = CountrySchema(many=True)
