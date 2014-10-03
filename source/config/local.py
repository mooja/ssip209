# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
from pathlib import PurePath
from configurations import values
from .common import Common


class Local(Common):

    # DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = values.ListValue(['127.0.0.1', 'localhost'])
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = values.Value('smtp.sendgrid.com')
    EMAIL_HOST_USER = values.Value("mooja")
    EMAIL_HOST_PASSWORD = values.SecretValue()
    DEFAULT_FROM_EMAIL = values.Value('Max Shkurygin <max.atreides@gmail.com>')
    EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    EMAIL_SUBJECT_PREFIX = values.Value('[SSIP 209] ', environ_name="EMAIL_SUBJECT_PREFIX")
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # EMAIL_USE_TSL = True
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = values.Value(['127.0.0.1'], environ_name="INTERNAL_IPS")

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    DATABASES = values.DatabaseURLValue("sqlite:///database/db.sqlite3")
    # Your local stuff: Below this line define 3rd party libary settings
    # trying out django extensions
    INSTALLED_APPS += ('django_extensions',)
