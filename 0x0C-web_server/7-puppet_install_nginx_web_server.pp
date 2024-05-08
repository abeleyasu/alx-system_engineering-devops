# File: 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
}

# Ensure Nginx is listening on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {\n\tlisten 80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm;\n\tlocation / {\n\t\treturn 200 'Hello World!';\n\t}\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n}",
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure  => running,
  require => File['/etc/nginx/sites-available/default'],
}
