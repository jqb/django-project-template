import os 


# Change THIS! per project
SITE_NAME = 'Project'
ROOT_URLCONF = 'django-project-template.urls'
SECRET_KEY = '+x&(yo6og$2yn)byx274l(ej31ae5%kt@oi**du6f$0r7wqq9y'


BASE_LOCATION = '/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_URL = '%s/' % '/'.join([BASE_LOCATION, 'static'])


DEBUG = True
TEMPLATE_DEBUG = True
ADMINS = ()
MANAGERS = ()


TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True


INSTALLED_APPS = (
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',

    'db',
    )


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    )


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'conf.context_processors.conf',
    )
TEMPLATE_SETTINGS = ['SITE_NAME']



# APPS SETTINGS #########################################
# django.contrib.sites
# SITE_ID = 1

# django.contrib.admin
# ADMIN_MEDIA_PREFIX = '/media/'
# APPS SETTINGS #########################################



# Settings cunstomizations ##############################
# the module can be cunstomize via DJANGO_ENV environ
# variable
ENV = os.environ.get('DJANGO_ENV', 'conf.dev_sqlite')
config_module = __import__('%s' % ENV, globals(), locals(), SITE_NAME)


for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)


# cleaninig up
del config_module, setting
