from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

# Initialize Flask application
app = Flask(__name__)

# Load Flask app with desired configuration
app.config.from_object(config("APP_SETTINGS"))

# Binds database to Flask app 
db = SQLAlchemy(app)

# Creates automatic revision script
migrate = Migrate(app, db)

from core import routes
