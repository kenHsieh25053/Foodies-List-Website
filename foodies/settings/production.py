# Settings for production model

from foodies.settings.common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')
