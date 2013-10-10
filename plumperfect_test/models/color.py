from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

from plumperfect_test import db

from .base import BaseMixin

class Color( BaseMixin, db.Model ):

    '''A color.'''

    __tablename__   = 'color'

    id              = db.Column( db.Integer(), nullable = False, primary_key = True )
    product_id      = db.Column( db.Integer(), db.ForeignKey( 'product.id' ), nullable = False, index = True )
    timestamp       = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    title           = db.Column( db.Unicode(256), nullable = False )
    rgb_r           = db.Column( db.Integer(), nullable = False, index = True )
    rgb_g           = db.Column( db.Integer(), nullable = False, index = True )
    rgb_b           = db.Column( db.Integer(), nullable = False, index = True )

    color_users     = db.relationship( 'ColorUser' )

    product         = db.relationship( 'Product' )
    brand           = association_proxy( 'product', 'brand' )
    users           = association_proxy( 'color_users', 'user' )

class ColorUser( BaseMixin, db.Model ):

    '''A many-to-many relationship between product_color and user.'''

    __tablename__       = 'color_user'

    color_id            = db.Column( db.Integer(), db.ForeignKey( 'color.id' ), nullable = False, primary_key = True )
    user_id             = db.Column( db.Integer(), db.ForeignKey( 'user.id' ), nullable = False, primary_key = True )
    timestamp           = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    product             = association_proxy( 'color', 'product' )
    color               = db.relationship( 'Color' )
    user                = db.relationship( 'User' )
