from plumperfect_test.models import Brand
from .base import RestCtrl


class BrandCtrl( RestCtrl ):

    '''The brand controller.'''

    Model = Brand

    def get(self, id):
	result = Model.query.get(id)
	return result

    def filter_product(self, id):
	results = Model.query.get(id).products.all()
	return results
