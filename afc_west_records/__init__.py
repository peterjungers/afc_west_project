"""
This module initiates Flask app instance and database.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


from afc_west_records import handlers
from afc_west_records import models
from afc_west_records import routes
