from flask import Blueprint

site = Blueprint('site',__name__)

from . import site_management
from . import contact_management