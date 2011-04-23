import os


# Change THIS! per project
SITE_NAME = 'Project'
ROOT_URLCONF = 'project.urls'
SECRET_KEY = '+x&(yo6og$2yn)byx274l(ej31ae5%kt@oi**du6f$0r7wqq9y'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

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
    # 'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'annoying',
    'debug_toolbar',

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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'conf.middleware.StaticServe',
    )


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'conf.context_processors.conf',
    )


JQUERY_VER = '1.4.3'
JQUERY_UI_VER = '1.8.5'
JQUERY_UI_THEME = 'ui-lightness'
# JQUERY UI PROVIDES FOLLOWING THEMES:
# base, black-tie, blitzer, cupertino, dark-hive, dot-luv,
# eggplant, excite-bike, flick, hot-sneaks, humanity,
# le-frog, mint-choc, overcast, pepper-grinder, redmond,
# smoothness, south-street, start, sunny, swanky-purse,
# trontastic, ui-darkness, ui-lightness, vader


# small javascript library that provides python-like classes in javascript.
# If don't want to use it you can set CLASSY_VER to None
CLASSY_VER = '1.3'


MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media')
MEDIA_URL = '%s/' % '/'.join(['site_media', 'media'])


# APPS SETTINGS #########################################
# django.contrib.sites
# SITE_ID = 1

# django.contrib.admin
# ADMIN_MEDIA_PREFIX = '/media/'

# django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False
}

# django.contrib.staticfiles
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'static')
STATIC_URL = '%s/' % '/'.join(['site_media', 'static'])
# APPS SETTINGS #########################################



# add here options which you'd like to have in templates
TEMPLATE_SETTINGS = ['SITE_NAME', 'JQUERY_VER', 'JQUERY_UI_VER',
                     'JQUERY_UI_THEME', 'CLASSY_VER']



# Settings cunstomizations ##############################
# the module can be cunstomize via DJANGO_ENV environ
# variable
ENV = os.environ.get('DJANGO_ENV', 'conf.dev_sqlite')
config_module = __import__('%s' % ENV, globals(), locals(), SITE_NAME)


for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)


# cleaninig up
del config_module, setting, ENV
