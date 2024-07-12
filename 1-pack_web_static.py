#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """

from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """ Fabric script that generates a .tgz archive from the contents of the...
    ...web_static folder """
    if not os.path.exists('versions'):
        os.makedirs('versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = c.local("tar -cvzf {} web_static".format(filename))
    if result.exited == 0:
        return filename
    else:
        return None

