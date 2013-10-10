from flask import request, abort, jsonify
from flask.ext.classy import FlaskView

class ViewRegistrar( object ):

    VIEW_BASE = 'api'

    @classmethod
    def register( cls, app, views ):

        for view in views:

            route_base = cls.VIEW_BASE + '/' + view.route_base
            view.register( app, route_base = route_base )

class BaseView( FlaskView ):

    '''A default generic view.'''

    @property
    def request_data( self ):

        '''Get incoming data from API request.'''

        try:
            data = request.json
        except:
            data = None

        if data == None:
            data = request.form

        if hasattr( data, 'to_dict' ):
            data = data.to_dict()

        return data or {}

    @property
    def request_args( self ):

        return request.args

    def _json( self, data ):

        '''Return json response under instance's namespace.  This should be used by all API methods returning a json response.'''

        if isinstance( data, list ):
            data = map( lambda d: d.to_dict() if hasattr( d, 'to_dict' ) else d, data )
        elif hasattr( data, 'to_dict' ):
            data = data.to_dict()

        return jsonify( data )

class RestView( BaseView ):

    '''A default view for RESTful APIs.  Provides some typical get, post, ... methods.'''

    # REST controller class
    Controller = None

    # REST controller instance
    _controller = None

    @property
    def controller( self ):

        '''Controller whcih initializes itself on first access.'''

        if self._controller == None:
            self._controller = self.Controller()
        return self._controller

    def index( self ):

        results = self.controller.index( )
        return self._json( results )

    def get( self, id ):

        results = self.controller.get( id )
        return self._json( results )

    def post( self ):

        results = self.controller.post( **self.request_data )
        return self._json( results )

    def put( self, id ):

        results = self.controller.put( id, **self.request_data )
        return self._json( results )

    def patch( self, id ):

        results = self.controller.patch( id, **self.request_data )
        return self._json( results )

    def delete( self, id ):

        results = self.controller.delete( id )
        return self._json( results )
