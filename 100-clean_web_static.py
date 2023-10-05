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
            "ln -s /data/web_static/releases/{}/web_static/ "
            "/data/web_static/current".format(folder)
            )
        return True
    except Exception as e:
        return False


@task
def deploy():
    """Creates and destributes an archive to your web server"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


@task
def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1

    try:
        local_archives = local("ls -1t versions", capture=True).split("\n")
        remote_archives = run("ls -1t /data/web_static/releases").split("\n")

        for archive in local_archives[number:]:
            local("rm -f versions/{}".format(archive))

        for archive in remote_archives[number:]:
            run("rm -rf /data/web_static/releases/{}".format(archive))

    except Exception:
        pass
    return True
