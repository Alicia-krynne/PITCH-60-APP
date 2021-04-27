import os


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'
MAIL_USERNAME = 'alicakryne@outlook.com'
MAIL_PASSWORD = 'Wayne2015'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
