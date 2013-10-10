import plumperfect_test

if __name__ == '__main__':

    app = plumperfect_test.create_app()

    app.run(
        host    = app.config.get( 'SERVER_HOST' ),
        port    = app.config.get( 'SERVER_PORT' ),
        debug   = app.config.get( 'DEBUG' )
    )
