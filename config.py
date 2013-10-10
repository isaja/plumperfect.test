import os
here = os.path.abspath( os.dirname( __file__ ) )

DEBUG = True

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 900001

# Generate this with os.urandom(24)
SECRET_KEY = '>\x85\xf0\xd5\xa4\xfa\xf6\xbe\xe9\xbd\x1d\xe2\xf9\x98\xd8\x17\xb4\xd7\xd4\xafW\x95\xddJ'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join( here, 'plumperfect_test.db' )
