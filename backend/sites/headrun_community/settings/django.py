import os

os.environ['APP_LIST'] = str([
                            'community',
                            'user'
                        ])

try:
    from base.settings.django import *
except:
    from base.settings.django import *

API_APP_LIST = [
                'community',
                'user'
            ]

INSTALLED_APPS += ['base']
