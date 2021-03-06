from plumperfect_test.controllers import ProductCtrl
from .base import RestView
from flask.ext.classy import route #added by me

class ProductView( RestView ):

    '''The product view.'''

    route_base = 'product'
    Controller = ProductCtrl



    @route('/<id>/')
    @route('/<id>/<category>')
    def get(self, id, category = None):
        if category == None:
	    result = self.controller.get(id)
	elif category == 'color':
	    results = self.controller.filter_color(id)
	elif category == 'brand':
	    results = self.controller.filter_brand(id)
	else:
	    results = []
	return self._json(results)



