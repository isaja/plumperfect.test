from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

from plumperfect_test import db

from .base import BaseMixin

class Product( BaseMixin, db.Model ):

    '''An article of clothing.'''

    __tablename__   = 'product'

    id              = db.Column( db.Integer(), nullable = False, primary_key = True )
    timestamp       = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    brand_id        = db.Column( db.Integer(), db.ForeignKey( 'brand.id' ) )

    title           = db.Column( db.Unicode(256), nullable = False )
    description     = db.Column( db.UnicodeText() )

    colors          = db.relationship( 'Color' )
    brand           = db.relationship( 'Brand' )
    users           = association_proxy( 'colors', 'users' )
