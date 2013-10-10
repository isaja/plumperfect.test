from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

from plumperfect_test import db

from .base import BaseMixin

class Color( BaseMixin, db.Model ):

    '''A color.'''

    __tablename__   = 'color'

    id              = db.Column( db.Integer(), nullable = False, primary_key = True )
    timestamp       = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    title           = db.Column( db.Unicode(256), nullable = False )
    rgb_r           = db.Column( db.Integer(), nullable = False, index = True )
    rgb_g           = db.Column( db.Integer(), nullable = False, index = True )
    rgb_b           = db.Column( db.Integer(), nullable = False, index = True )

    product_colors  = db.relationship( 'ProductColor' )

    products        = association_proxy( 'product_colors', 'product' )
    users           = association_proxy( 'product_colors', 'users' )
