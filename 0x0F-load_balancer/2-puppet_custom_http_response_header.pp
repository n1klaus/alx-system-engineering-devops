#Installs a Nginx server and configures HTTP response header

exec { 'install nginx':
  provider => shell,
  command  => "sudo apt-get -y update && sudo apt-get install ufw nginx -y;
		sudo ufw allow 'ssh' && sudo ufw allow 'Nginx HTTP' && sudo ufw enable;
		sudo mkdir -p /var/www/html;
		echo 'Hello World!' | sudo tee /var/www/html/index.html;
		echo -e 'Ceci n\'est pas une page' | sudo tee /var/www/html/404.html;",
}

exec { 'set header':
  provider => shell,
  command  => echo -e "server {\n\t
		listen 80 default_server;\n\t
		listen [::]:80 default_server;\n\t
		root /var/www/html;\n\t
		index index.html index.htm index.nginx-debian.html;\n\t
		server_name _;\n\t
		rewrite ^/redirect_me https://github.com/n1klaus permanent;\n\t
		error_page 404 /404.html;\n\t
		add_header X-Served-By $HOSTNAME;\n\t
		ignore_invalid_headers on;\n}" | 
		sudo tee /etc/nginx/sites-enabled/default;
		sudo service nginx start',
  require  => EXEC['install nginx'],
}
