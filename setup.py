from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'flask_sqlalchemy', 'flask_marshmallow', 'marshmallow-sqlalchemy', 'marshmallow_enum', 'click',
        'marshmallow', 'flask_migrate', 'werkzeug', 'flask_cors', 'flask_jwt_extended'
    ],
)