import os

secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' # tokens CSRF
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD) # conexion BD
SQLALCHEMY_TRACK_MODIFICATIONS = False # deshabilita gestión de notificaciones sqlalchemy