from plumperfect_test.models import User
from .base import RestCtrl

class UserCtrl( RestCtrl ):

    '''The rest controller.'''

    Model = User

    def get(self, id):
	result = User.query.get(id)
	return result

    def filter_user_colors(self, id):
	results = User.query.get(id).user_colors.all()
	return results
