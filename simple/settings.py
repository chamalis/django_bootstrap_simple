"""
Django settings for simple project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#BASE_DIR = os.path.dirname(os.getcwd())
#print 'base dir ', BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

NAME='simple'

LOGIN_URL = '/login/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jk0vg7-5mcsr=rsgr54-es$+*zklo&wt=4zg(&-oar2tld$slt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'persons'
    # 'compressor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simple.urls'

WSGI_APPLICATION = 'simple.wsgi.application'

# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_FINDERS=(
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, NAME, "static"),
    #'/common/programming/django/myProjects/simple/simple/static',
)

STATIC_URL = os.path.join(BASE_DIR, NAME, 'static/')
#print 'static ', STATIC_URL
SITE_PAGES_DIRECTORY  = os.path.join(STATIC_URL, 'pages')
#print SITE_PAGES_DIRECTORY
SITE_OUTPUT_DIRECTORY = os.path.join(BASE_DIR, '_build')
#print SITE_OUTPUT_DIRECTORY
STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static')

#models_pages = [dir in os.listdir(SITE_PAGES_DIRECTORY)]
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, NAME, 'templates/'),
    SITE_PAGES_DIRECTORY,
)
#print 'template dirs ', TEMPLATE_DIRS



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

