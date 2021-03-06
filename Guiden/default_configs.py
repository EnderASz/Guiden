from os import environ, path


class Config:
    SECRET_KEY = environ.get(
        'SECRET_KEY',
        '5567276479f37bde63742ec1e3b3507183f0d5ba9c832712089c8bf484bdaf9e')

    MONGO_HOST = environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(environ.get('MONGO_PORT', 27017))
    MONGO_DBNAME = environ.get('MONGO_DBNAME', 'Guiden')
    MONGO_USER = environ.get('MONGO_USER', "")
    MONGO_PASS = environ.get('MONGO_PASS', "")
    MONGO_OPTS = environ.get('MONGO_OPTS', "")

    PUBLIC_MEDIA_ROOT = path.join(path.dirname(__file__), 'media', 'public')

    # Home subapp
    HOME_NEWS_LIMIT = 4
    HOME_PREMIERES_LIMIT = 20


class DevelopmentConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
