from plumperfect_test.controllers import BrandCtrl
from .base import RestView

class BrandView( RestView ):

    '''The brand view.'''

    route_base = 'brand'
    Controller = BrandCtrl
