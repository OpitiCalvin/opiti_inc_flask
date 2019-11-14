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
	# 'user': 'spatialadmin',
	# 'pw': 'sp@t1@l@dm1n',
	# 'db': 'geofarmer',
	# 'host': 'localhost',
	# 'port': '5432',
	# }
	# SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES # for postgresql
	SECRET_KEY = '3xtr3m3ly-pr1v@t3-@p1-k3y'
	CUSTOM_DB_FLAG = 'local'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JWT_TOKEN_LOCATION = ['headers', 'cookies']	# Configure app to store JWTs in cookies
	JWT_COOKIE_SECURE = False	# Only allow JWT cookies to be sent over https. In production, this should be True
	JWT_SECRET_KEY = 'jwt-secret-string'
	JWT_BLACKLIST_ENABLED = True
	JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
	JWT_ACCESS_TOKEN_EXPIRES = False
	JWT_ACCESS_COOKIE_PATH = '/'
	JWT_REFRESH_COOKIE_PATH = '/'
	JWT_COOKIE_CSRF_PROTECT = True	# Enable CSRF double submit protection
	# UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'geofarmer_apis','uploads')
	# UPLOADED_IMAGES_DEST = os.path.join(basedir, 'geofarmer_apis','uploads', 'logo')
	# UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'geofarmer_apis','uploads', 'disp_pic')

class ProductionConfig(Config):
	"""
	Configurations for Production.

	"""
	
	TESTING = False
	SECRET_KEY = uuid.uuid4().hex
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'opiti_inc.sqlite')
	# SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
	CUSTOM_DB_FLAG = 'production'
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JWT_SECRET_KEY = ''
	JWT_ACCESS_TOKEN_EXPIRES = False
	JSON_SORT_KEYS = False
	# UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'geofarmer_api','uploads')
	# UPLOADED_IMAGES_DEST = os.path.join(basedir, 'geofarmer_api','uploads', 'logo')
	# UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'geofarmer_api','uploads', 'disp_pic')

	
app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
}
