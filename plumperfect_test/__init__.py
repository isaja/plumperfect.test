from flask import Flask
from database import db

def init_db( app ):

    db.init_app( app )
    db.app = app

    from models import *
    db.create_all()

def create_app( config = 'config', app_name = __name__ ):

    '''Flask application factory.'''

    app = Flask( app_name )
    app.config.from_object( config )

    init_db( app )

    import views
    views.register( app )

    return app
