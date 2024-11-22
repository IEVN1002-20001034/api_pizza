class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='api_diana'
    MYSQL_CLIENT_FLAGS = [2] 
    
#SQLALchemy
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SECRET_KEY = 'mi_clave_secreta'  