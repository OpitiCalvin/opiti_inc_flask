import os
import json
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
	"""
	Parent configuration class.
	"""
	DEBUG = False
	
	

class DevelopmentConfig(Config):
	""" Configuration for Development."""
	
	DEBUG = True
	
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'opiti_inc.sqlite')
	# POSTGRES = {
	# 'user': '',
	# 'pw': '',
	# 'db': '',
	# 'host': 'localhost',
	# 'port': '5432',
	# }
	# SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES # for postgresql
	SECRET_KEY = '3xtr3m3ly-pr1v@t3-@p1-k3y'
	CUSTOM_DB_FLAG = 'local'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'geofarmer_apis','uploads')
	# UPLOADED_IMAGES_DEST = os.path.join(basedir, 'geofarmer_apis','uploads', 'logo')
	# UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'geofarmer_apis','uploads', 'disp_pic')

class ProductionConfig(Config):
	"""
	Configurations for Production.

	"""
	
	TESTING = False
	SECRET_KEY = uuid.uuid4().hex
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'wits_acms.sqlite')
	# SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
	CUSTOM_DB_FLAG = 'production'
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JSON_SORT_KEYS = False
	# UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'geofarmer_api','uploads')
	# UPLOADED_IMAGES_DEST = os.path.join(basedir, 'geofarmer_api','uploads', 'logo')
	# UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'geofarmer_api','uploads', 'disp_pic')

	
app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
}
