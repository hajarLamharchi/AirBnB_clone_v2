#!/usr/bin/python3
"""This script distributes an archive to your web servers"""
from fabric.api import run, put, env, sudo
from os.path import exists

env.hosts = ['52.86.213.205', '52.91.119.144']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive = archive_path.split('/')[-1]
        folder = archive[:-4]

        run('mkdir -p /data/web_static/releases/{}/'.format(folder))
        run(
            'tar -xzf /tmp/{} '
            '-C /data/web_static/releases/{}/'.format(archive, folder)
            )

        run('rm /tmp/{}'.format(archive))

        run('rm -rf /data/web_static/current')

        run(
            'ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(folder)
            )
        return True
    except Exception as e:
        return False
