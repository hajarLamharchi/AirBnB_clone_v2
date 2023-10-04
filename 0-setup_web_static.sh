#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static

# installing nginx
sudo apt-get update
sudo apt-get -y install nginx

# creating directories if they don't already exit
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create random html file to test nginx config
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# check if symlink exist, if so delete it
if [ -L "/data/web_static/current" ]; then
	sudo rm "/data/web_static/current"
fi

# create symbolic link
sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"

# change ownership of /data/ and every folder/file inside
sudo chown -R ubuntu:ubuntu /data/

# update nginx config
sudo sed -i '/listen 80 default_server;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# check the syntax errors
sudo nginx -t

# restart nginx
sudo service nginx restart
