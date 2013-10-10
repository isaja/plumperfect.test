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

    product_colors  = db.relationship( 'ProductColor' )
    
    brand           = db.relationship( 'Brand' )
    colors          = association_proxy( 'product_colors', 'color' )
    users           = association_proxy( 'product_colors', 'users' )

class ProductColor( BaseMixin, db.Model ):

    '''A many-to-many relationship between product and color.'''

    __tablename__       = 'product_color'
    __table_args__      = ( db.UniqueConstraint( 'product_id', 'color_id' ), )

    id                  = db.Column( db.Integer(), nullable = False, primary_key = True )
    product_id          = db.Column( db.Integer(), db.ForeignKey( 'product.id' ) )
    color_id            = db.Column( db.Integer(), db.ForeignKey( 'color.id' ) )
    timestamp           = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    product_color_users = db.relationship( 'ProductColorUser' )

    product             = db.relationship( 'Product' )
    color               = db.relationship( 'Color' )
    users               = association_proxy( 'product_color_users', 'user' )

class ProductColorUser( BaseMixin, db.Model ):

    '''A many-to-many relationship between product_color and user.'''

    __tablename__       = 'product_color_user'

    product_color_id    = db.Column( db.Integer(), db.ForeignKey( 'product_color.id' ), nullable = False, primary_key = True )
    user_id             = db.Column( db.Integer(), db.ForeignKey( 'user.id' ), nullable = False, primary_key = True )
    timestamp           = db.Column( db.DateTime(), nullable = False, default = datetime.now, onupdate = datetime.now )

    product_color       = db.relationship( 'ProductColor' )

    user                = db.relationship( 'User' )
    product             = association_proxy( 'product_color', 'product' )
    color               = association_proxy( 'product_color', 'color' )
