from plumperfect_test.controllers import UserCtrl
from .base import RestView

class UserView( RestView ):

    '''The user view.'''

    route_base = 'user'
    Controller = UserCtrl
