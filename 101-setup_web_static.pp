# Setting web server for deployment with puppet

package { 'nginx':
  ensure => installed,
}

-> file { '/data/web_static/releases/test':
  ensure => directory,
}

-> file { '/data/web_static/shared':
  ensure => directory,
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
}
-> exec {'owner':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell,
}

-> file { '/data/web_static/current':
  ensure => absent,
}

-> file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}

-> exec { 'configuration':
  command  => "sudo sed -i '/listen 80 default_server;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default",
  provider => shell,
  notify  => exec['nginx'],
}

-> exec { 'nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
