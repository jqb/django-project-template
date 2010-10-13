# -*- coding: utf-8 -*-
# ...assumes that you keep extended configuration files in `<project-name>`/conf
# directory
import os


this_conf_dir = os.path.dirname(os.path.abspath(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(this_conf_dir, '..', 'db', 'project.db'),
        }
    }
