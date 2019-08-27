import os
DEBUG = True
from flask_uploads import UploadSet, IMAGES, DOCUMENTS, configure_uploads, ALL

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'forum'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

WHOOSH_BASE='path/to/whoosh/base'

SECURITY_PASSWORD_SALT = 'my_precious_two'
# mail settings
MAIL_SERVER = 'smtp.126.com'
MAIL_PROT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False

# gmail authentication
# MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
# MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
MAIL_USERNAME = 'forumaces@126.com'
MAIL_PASSWORD = 'aces6666'
MAIL_DEBUG = True

# mail accounts
MAIL_DEFAULT_SENDER = 'from@example.com'

UPLOADED_PHOTO_DEST = '/forum/static/images'
UPLOADED_PHOTO_ALLOW = IMAGES

UPLOADED_DOCUMENT_DEST = '/forum/static/documents'
UPLOADED_DOCUMENTS_ALLOW = DOCUMENTS