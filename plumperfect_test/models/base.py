class BaseMixin( object ):

    '''A base mixin providing some basic functionality.'''

    __table_args__ = {
        'mysql_engine'  : 'MyISAM',
        'mysql_charset' : 'utf8'
    }

    def __repr__( self ):

        '''Gives a debug representation of the model so that it can be easily queried.'''

        keys = map( lambda key: key.name, self.__mapper__.primary_key )
        keys = ', '.join( map( lambda key: '{0}={1}'.format( key, getattr( self, key ) ), keys ) )
        return '< {0} ({1}) >'.format( self.__class__.__name__, keys )

    def to_dict( self ):

        '''A generic dictionary representation.'''

        d = dict()
        for column in self.__table__.c.keys():
            d[ column ] = getattr( self, column )

        return d
