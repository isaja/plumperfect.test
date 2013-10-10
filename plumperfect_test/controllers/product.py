from plumperfect_test.models import Product
from .base import RestCtrl

class ProductCtrl( RestCtrl ):

    '''The product controller.'''

    Model = Product
