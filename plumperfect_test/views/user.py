from plumperfect_test.controllers import UserCtrl
from .base import RestView
from flask.ext.classy import route #added by me
from flask import url_for #added by me

class UserView( RestView ):


    '''The user view.'''

    route_base = 'user'
    Controller = UserCtrl


    def post( self ):
	''' overwrite post method in base.py so that user.post doesn't require authentication '''
        results = self.controller.post( **self.request_data )
        return self._json( results )


    @route('/<id>/')
    @route('/<id>/<category>')
    def get(self, id, category = None):
        if category == None:
	    results = self.controller.get(id)
	elif category == 'user_colors':
	    results = self.controller.filter_user_colors(id)
	else:
	    results = []
	return self._json(results)




















