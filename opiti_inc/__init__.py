import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
# from flask_uploads import UploadSet, IMAGES, configure_uploads
from config import app_config

db = SQLAlchemy()
# ma = Marshmallow()
migrate = Migrate()
# login_manager = LoginManager()
# jwt = JWTManager()

# images = UploadSet('images', IMAGES)
# photos = UploadSet('photos', IMAGES)
 
def create_app(config_name):
	r"""
	An initialisation function for the Opiti Inc application. 

	parameters

		config_name: str, required
			A description referencing a set of configurations for the app
			
			Options include: ``development``, or ``production``

	"""

	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])

	# Ensure instance directory exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# configure_uploads(app, (photos,images))

	initialize_extensions(app)
	register_blueprints(app)

	return app

def initialize_extensions(app):
	r"""
	Initialisation of extensions used in/with the application.

	At application initialisation, these extensions are too:
		**database** - To enable SQLAlchemy ORM and CRUD functionality.
		**marshallow** - To enable validation of data, deserialization and 
			serialization app-level objects to basic python types and 
			rendering as JSON for use in the application.
		**migrate** - To initialize with the application the capability to 
			implement and modify database tables and schema.
		**flask JWT** - To enable creation of JSON Web Tokens for use with the 
			application/API for user authorization

	parameters

		app: flask application, required
			The application instance the extensions are associated with.

	"""

	db.init_app(app)
	# ma.init_app(app)
	migrate.init_app(app, db)
	# login_manager.init_app(app)
	# jwt.init_app(app)

def register_blueprints(app):
	r"""
	Includes blueprints and associated templates or static files with the application 
	instance at initialisation.

	parameters
	
		app: flask application, required
			The application instance to which the blueprints are to be included.
			
	"""

	from opiti_inc.views import site
	app.register_blueprint(site, url_prefix='/')
	# pass