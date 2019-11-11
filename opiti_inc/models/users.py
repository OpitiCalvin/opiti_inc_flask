from opiti_inc import db, ma, jwt
from sqlalchemy import Column, Integer, String, Date, DateTime, ARRAY, Float, ForeignKey, BigInteger, SmallInteger, BOOLEAN 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
# from marshmallow import fields, ValidationError, validates
# from passlib.hash import pbkdf2_sha256 as sha256
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):

	__tablename__ = 'users'

	user_id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(50), unique=False, nullable=False)
	email = Column(String(50), unique=True, nullable=False)
	password = Column(String(100), nullable=False)
	authenticated = Column(BOOLEAN, nullable=False, default=False, server_default="false")
	last_logged_in = Column(DateTime(timezone=True), nullable=True)
	current_logged_in = Column(DateTime(timezone=True), nullable=True)

	# Standard
	created = Column(DateTime(timezone=True), server_default=func.now())
	created_by = Column(String(100), nullable=False)
	updated = Column(DateTime(timezone=True), onupdate=func.now())
	updated_by = Column(String(100), nullable=True)

	def __init__(self, username, email, password, ):
	    self.username = username
	    self.email = email
	    self.password = password
	    

	@classmethod
	def find_by_username(cls,username):
		return cls.query.filter_by(username = username).first()

	@classmethod
	def find_by_email(cls,email):
		return cls.query.filter_by(email = email).first()

	@staticmethod
	def generate_hash(password):
		return generate_password_hash(password, method='sha256')

	@staticmethod
	def verify_hash(hash, password):
		return check_password_hash(hash, password)

class AvatarModel(db.Model):
	"""
	"""
	__tablename__ = 'user_avatars'

	avatar_id = Column(Integer, primary_key=True, autoincrement=True)
	avatar_name = Column(String(), nullable=False)
	avatar_link = Column(String(), nullable=False)
	user_id = Column(Integer(), ForeignKey('users.user_id'), nullable=False)
	user = relationship('UserModel', backref=db.backref('user_avatar',lazy=True))

	# Standard
	created = Column(DateTime(timezone=True), server_default=func.now())
	updated = Column(DateTime(timezone=True), onupdate=func.now())

class UserProfile(db.Model):
	__tablename__ = 'user_profiles'

	profile_id = Column(Integer, primary_key=True)
	first_name = Column('first_name', db.String(50), nullable=False)
	last_name = Column('last_name', db.String(50), nullable=False)
	user_phone = Column('phone_contact', db.String(20), nullable=False)
	user_country = Column('country', db.String(50), nullable=False)
	# user_image_url = db.Column(db.String(120), nullable=True) # Look into image field type
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
	user = db.relationship('UserModel', backref=db.backref('profiles',lazy=True))
	# Standard
	created = Column(DateTime(timezone=True), server_default=func.now())
	created_by = Column(String(100), nullable=False)
	updated = Column(DateTime(timezone=True), onupdate=func.now())
	updated_by = Column(String(100), nullable=True)

	def __init__(self,first_name, last_name, user_phone, user_country, user_id):
	    self.first_name = first_name
	    self.last_name = last_name
	    self.user_phone = user_phone
	    self.user_country = user_country
	    self.user_id = user_id

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def __repr__(self):
		return f'User: {self.first_name} {self.last_name}'

class RevokedTokenModel(db.Model):
	r"""
	A model to capture and store revoked JWT tokens
	"""

	__tablename__ = 'revoked_tokens'

	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String(120))

	def add(self):
		r"""
		A function to actualize storage of the revoked token to a database.
		"""
		
		db.session.add(self)
		db.session.commit()

	@classmethod
	def is_token_blacklisted(cls, token):
		r"""
		Queries the database to check if provided token has been revoked.

		parameters
		----------
			token: str, required:
				A JWT token to be checked for validity.

		returns
		-------
			Returns ``True`` if token has been revoked and therefore invalid 
			or ``False`` to indicate validity of the token.
		"""

		query = cls.query.filter_by(token = token).first()
		return bool(query)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
	r"""
	A JWT loader for verification of revoked status of tokens.

	parameters
	----------
		decrypted_token: JWToken, required
			A token to be checked with the records of blacklisted tokens.

	returns
	-------
		Response returned is boolean - ``True`` or ``False`` depending on the blacklisted status of the token

	"""

	token = decrypted_token['jti']
	return RevokedTokenModel.is_token_blacklisted(token)