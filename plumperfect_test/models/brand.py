from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

from plumperfect_test import db

from .base import BaseMixin

class Brand( BaseMixin, db.Model ):

    '''A brand.'''

    __tablename__   = 'brand'

    id              = db.Column( db.Integer(), nullable = False, primary_key = True )
    timestamp       = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    title           = db.Column( db.Unicode(256), nullable = False )
    description     = db.Column( db.UnicodeText() )

    products        = db.relationship( 'Product' )
    colors          = association_proxy( 'products', 'colors' )
    users           = association_proxy( 'products', 'users' )
