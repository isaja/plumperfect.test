from .base import ViewRegistrar

from product import ProductView
from color import ColorView
from brand import BrandView
from user import UserView

views = [ ProductView, ColorView, BrandView, UserView ]

def register( app ):

    ViewRegistrar.register( app, views )
