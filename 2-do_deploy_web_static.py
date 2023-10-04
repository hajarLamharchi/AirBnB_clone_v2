#!/usr/bin/python3
"""This script distributes an archive to your web servers"""
from fabric.api import run, put, env, local, task
from os.path import exists
from datetime import datetime

env.hosts = ["52.86.213.205", "52.91.119.144"]


@task
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


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive = archive_path.split("/")[-1]
        folder = archive[:-4]

        run("mkdir -p /data/web_static/releases/{}/".format(folder))
        run(
            "tar -xzf /tmp/{} "
            "-C /data/web_static/releases/{}/".format(archive, folder)
            )

        run("rm /tmp/{}".format(archive))

        run("rm -rf /data/web_static/current")

        run(
            "ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(folder)
            )
        return True
    except Exception as e:
        return False
