#!/usr/bin/env python
import os
import subprocess
import sys

from app import create_app
from flask_script import Manager, Command, Server

# class GunicornServer(Command):
#     """Run the app within Gunicorn"""
#
#     def get_options(self):
#         from gunicorn.config import make_settings
#
#         settings = make_settings()
#         options = (
#             Option(*klass.cli, action=klass.action)
#             for setting, klass in settings.iteritems() if klass.cli
#         )
#         return options
#
#     def run(self, *args, **kwargs):
#         from gunicorn.app.wsgiapp import WSGIApplication
#         app = WSGIApplication()
#         app.app_uri = 'app:wsgi'
#         return app.run()

manager = Manager(create_app())

# manager.add_command("gunicorn", GunicornServer())

if __name__ == '__main__':

    manager.run()
