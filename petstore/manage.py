import sys
import os
sys.path.append(os.getcwd() + '/..')

from app import db
from petstore.User.model import *

db.create_all()
db.session.commit()
