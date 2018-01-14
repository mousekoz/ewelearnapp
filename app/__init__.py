from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Create configuration object from the Config class
app.config.from_object(Config)
# Create database instance
db = SQLAlchemy(app)
# Create an instance of the database migration engine
migrate = Migrate(app, db)

from app import routes, logic