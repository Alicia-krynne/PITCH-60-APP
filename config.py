import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'
   
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
