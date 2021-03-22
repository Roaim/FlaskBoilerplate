from .base_model import db, BaseModel


class Country(BaseModel):
    name = db.Column(db.String(255))
    iso_code = db.Column(db.String(2))
    isd_code = db.Column(db.String(3))


class City(BaseModel):
    name = db.Column(db.String(255))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'))
    country = db.relationship('Country', lazy='subquery')


class Address(BaseModel):
    line1 = db.Column(db.String(255))
    line2 = db.Column(db.String(255))
    street = db.Column(db.String(255))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id', ondelete='CASCADE'))
    city = db.relationship('City', lazy='subquery')
