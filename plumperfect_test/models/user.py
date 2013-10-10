from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

from plumperfect_test import db

from .base import BaseMixin

class User( BaseMixin, db.Model ):

    '''A user.'''

    __tablename__       = 'user'

    id                  = db.Column( db.Integer(), nullable = False, primary_key = True )
    timestamp           = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )
    last_login          = db.Column( db.DateTime(), nullable = True )

    email               = db.Column( db.Unicode(256), nullable = False )
    password            = db.Column( db.Unicode(256), nullable = False )

    user_product_colors = db.relationship( 'ProductColorUser' )

    products            = association_proxy( 'user_product_colors', 'product' )
    colors              = association_proxy( 'user_product_colors', 'color' )
