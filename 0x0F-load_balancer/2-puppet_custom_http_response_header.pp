# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
        add_header X-Served-By \$hostname;
    }
}",
  notify  => Service['nginx'],
}

# Enable Nginx service
service { 'nginx':
  ensure => running,
}
