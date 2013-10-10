from plumperfect_test.models import User
from .base import RestCtrl

class UserCtrl( RestCtrl ):

    '''The rest controller.'''

    Model = User
