# Python Flask Boilerplate
This is a simple Backend Rest API developed using python flask. The architecture of the codebase is highly maintainable. It has following functionalites:

1. User registration
2. User login
3. List users (Admin only)
4. Get current user details
5. Generate JWT token
6. Create Countries (Admin only)
7. Get Countries
8. Create Cities (Admin only)
9. Get Cities

### Dependencies
* Flask
* Flask SQL Alchemy
* Flask Marshmallow
* Marshmallow SQL Alchemy
* Flask Migrate
* Werkzeug
* Flask CORS
* Flask JWT Extended

## Environment Setup

Create project directory

    mkdir flaskboilerplate
    cd flaskboilerplate
    
#### Requirements
* **Python 3.7+**

Run the following commands to create and activate a virtual environment named `venv` (different name can be used)

    python3 -m venv venv
    . venv/vin/activate

## Build and Install
Set flask app by running following command:
#### Windows
    
    set FLASK_APP=app

#### Linux / Mac

    export FLASK_APP=app

### Build Distribution Package
If wheel is not installed run the follwoing command to install it:

    pip install wheel

To build distribution package run the following command:

    python setup.py bdist_wheel

    
## Create database
For the first time, run the following commands to create database schemas:

    flask db init
    flask db migrate
    flask db upgrade

### Install Distribution Package
Replace **x.x.x** with the actual version name

    pip install app-x.x.x-py3-none-any.whl

## Run
If **`waitress`** is not installed run the following command to install it:

    pip install waitress

If **`waitress`** is already installed run the following command to run the application:

    waitress-serve --call app:create_app
