#!/usr/bin/python3
"""This script generates an archive from the contents
    of the web_static folder of your AirBnB Clone repo"""
from fabric.api import run
from datetime import datetime


def do_pack():
    """Generates an archive from the contents of the web_static"""
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(current_datetime)

    run("sudo mkdir -p versions")
    result = run("tar -zcvf {} web_static".format(archive))
    if result.succeeded:
        return run("sudo readlink archive")
    else:
        return None
