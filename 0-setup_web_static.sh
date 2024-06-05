#!/usr/bin/env bash
#Script that sets up a web server for deployment of web_static

sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
EOF
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx reload
