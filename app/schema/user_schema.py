from marshmallow import post_load, fields
from ..model import ma
from ..model.user import User
from .address_schema import AddressSchema
from . import BASE_MODEL_FIELDS


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    email = fields.Email(required=True)
    address = fields.Nested(AddressSchema(exclude=BASE_MODEL_FIELDS))

    @post_load
    def create_model(self, data, **kwargs):
        return User(**data)


user_schema = UserSchema()
user_list_schema = UserSchema(many=True, exclude=('address',))
