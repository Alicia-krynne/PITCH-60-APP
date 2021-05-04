import os

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql://foozzhvvhqpsgm:6e03d4d2f7a47eff5af26c93078a4136efbe5cf74c657bc33e6024653316589a@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d3q6asgrmtqln1'
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://foozzhvvhqpsgm:6e03d4d2f7a47eff5af26c93078a4136efbe5cf74c657bc33e6024653316589a@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d3q6asgrmtqln1'

    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macrine:Alicemacrine!@localhost/pitch'
   
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
