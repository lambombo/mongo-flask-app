#!/usr/bin/env python
import os
import subprocess
import sys

from flask_script import Manager, Command, Server



from app import create_app


manager = Manager(create_app())


if __name__ == '__main__':

    manager.run()
