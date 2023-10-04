#!/usr/bin/python3
"""This script generates an archive from the contents
    of the web_static folder of your AirBnB Clone repo"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates an archive from the contents of the web_static"""
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(current_datetime)

    local("mkdir -p versions")
    result = local("tar -zcvf {} web_static".format(archive))
    if result.succeeded:
        return archive
    else:
        return None
