from os import environ


class Config:
    SECRET_KEY = environ.get(
        'SECRET_KEY',
        '5567276479f37bde63742ec1e3b3507183f0d5ba9c832712089c8bf484bdaf9e')


class DevelopmentConfig(Config):
    pass
