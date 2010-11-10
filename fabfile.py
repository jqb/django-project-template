from __future__ import with_statement

import os

from fabric.api import *
from fabric.contrib.project import rsync_project


env.project_name = 'project'


# sample 'context' configuration
# def example():
#     env.hosts = ['example.com']
#     env.path = '/home/services/www/example' # without trailing slash
#     env.user = 'user'


def setup():
    run('mkdir -p %s; cd %s; virtualenv $(pwd);' % (env.path, env.path))


def push():
    """Sync new development code on device"""
    rsync_project(
        remote_dir=env.path,
        local_dir=".",
        # delete=True,
        exclude=[".git*", ".svn*", "*.pyc", "*.pyo"])

    run("chown :www-data -R %s/" % env.path)
    run("chmod g+rw -R %s/db")


def requirements():
    """Install the required packages from the requirements file using pip"""
    run('cd %s; pip install -E $(pwd) -r requirements.txt' % env.path)


def restart():
    """Restart apache"""
    sudo("/etc/init.d/apache2 restart")


def deploy():
    """Full deploy: push and start"""
    push()
    requirements()
    restart()

