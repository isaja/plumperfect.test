from plumperfect_test.controllers import ColorCtrl
from .base import RestView
from flask.ext.classy import route #added by me

class ColorView( RestView ):

    '''The color view.'''

    route_base = 'color'
    Controller = ColorCtrl


    @route('/<id>/')
    @route('/<id>/<category>')
    def get(self, id, category = None):
        if category == None:
	    results = self.controller.get(id)
	elif category == 'product':
	    results = self.controller.filter_product(id)
	elif category == 'color_users':
	    results = self.controller.filter_color_users(id)
	else:
	    results = []
	return self._json( results )

