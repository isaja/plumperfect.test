from plumperfect_test.controllers import ProductCtrl
from .base import RestView

class ProductView( RestView ):

    '''The product view.'''

    route_base = 'product'
    Controller = ProductCtrl
