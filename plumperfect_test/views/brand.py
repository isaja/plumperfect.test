from plumperfect_test.controllers import BrandCtrl
from .base import RestView
from flask.ext.classy import route #added by me

class BrandView( RestView ):

    '''The brand view.'''

    route_base = 'brand'
    Controller = BrandCtrl


    @route('/<id>/')
    @route('/<id>/<category>')
    def get(self, id, category = None):
        if category == None:
	    results = self.controller.get(id)
	elif category == 'product':
	    results = self.controller.filter_product(id)
	else:
	    results = []
	return self._json(results)
