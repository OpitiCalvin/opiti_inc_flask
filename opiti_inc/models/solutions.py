from opiti_inc import db, ma, jwt
from sqlalchemy import Column, Integer, String, Date, DateTime, ARRAY, Float, ForeignKey, BigInteger, SmallInteger, BOOLEAN 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
# from marshmallow import fields, ValidationError, validates
# from passlib.hash import pbkdf2_sha256 as sha256
from werkzeug.security import generate_password_hash, check_password_hash


class SolutionModel(db.Model):

	__tablename__ = 'solutions'

	soln_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(100), unique=False, nullable=False)
	link = Column(String(100), nullable=False)
	description = Column(String(500), nullable=False)
	
	# Standard
	created = Column(DateTime(timezone=True), server_default=func.now())
	created_by = Column(String(100), nullable=False)
	updated = Column(DateTime(timezone=True), onupdate=func.now())
	updated_by = Column(String(100), nullable=True)