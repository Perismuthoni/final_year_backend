
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
 DEBUG = True
 TESTING = False
 CSRF_ENABLED = True
 SECRET_KEY = 'this-really-needs-to-be-changed'
 SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

 class ProductionConfig(Config):
        DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2



# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

