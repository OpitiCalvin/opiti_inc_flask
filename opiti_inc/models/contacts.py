from opiti_inc import db#, ma, jwt
from sqlalchemy import Column, Integer, String, Date, DateTime, ARRAY, Float, ForeignKey, BigInteger, SmallInteger, BOOLEAN 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
# from marshmallow import fields, ValidationError, validates
# from passlib.hash import pbkdf2_sha256 as sha256
from werkzeug.security import generate_password_hash, check_password_hash


class ContactModel(db.Model):

	__tablename__ = 'contacts'

	contact_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), unique=False, nullable=False)
	email = Column(String(50), unique=False, nullable=False)
	# phone = Column(String(100), nullable=True)
	# country = Column(String(100), nullable=False)
	message = Column(String(500), nullable=False)
	
	# Standard
	created = Column(DateTime(timezone=True), server_default=func.now())
	created_by = Column(String(100), nullable=False)
	updated = Column(DateTime(timezone=True), onupdate=func.now())
	updated_by = Column(String(100), nullable=True)

	@classmethod
	def find_by_email(cls,email):
		return cls.query.filter_by(email = email).first()