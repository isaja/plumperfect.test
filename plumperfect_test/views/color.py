from plumperfect_test.controllers import ColorCtrl
from .base import RestView

class ColorView( RestView ):

    '''The color view.'''

    route_base = 'color'
    Controller = ColorCtrl
