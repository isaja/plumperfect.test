from sqlalchemy.orm import lazyload

from flask import request, session, abort

from plumperfect_test import db

from plumperfect_test.models import User
import bcrypt

class BaseCtrl( object ):

    def __init__( self ):

        self.db         = db
        self.session    = session
        self.request    = request

    def commit( self ):

        try:
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            # Abort as a bad request for now...
            raise e

class RestCtrl( BaseCtrl ):

    Model   = None

    offset  = 0
    limit   = 20

    @property
    def query( self ):

        return self.db.session.query( self.Model )

    @property
    def order_by( self ):

        return self.Model.timestamp.desc()

    def index( self, **data ):

        results = self.query.all()
        return results

    def get( self, id ):

        result = self.query.get( id )
        return result

    def post( self, **data ):

        model = self.Model( **data )
        self.db.session.add( model )
        self.commit()

        return model

    def put( self, id, **data ):

        model = self.query.options( lazyload( '*' ) ).get( id ).update( data )
        self.commit()

        return model

    def patch( self, id, **data ):

        model = self.query.options( lazyload( '*' ) ).get( id )
        for attr, value in data.iteritems():
            setattr( model, attr, value )
        self.commit()

        return model

    def delete( self, id ):

        self.query.options( lazyload( '*' ) ).get( id ).delete()

    def authenticate(self,  *authentication_data):
	
	''' return True if the authentication is successful'''
	#return True
        result = User.query.filter_by(email = 'email').first()
	if result != None:
	    if result.password == bcrypt.hashpw('password', result.password):
	        return True

	return False
	





