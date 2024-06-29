# Puppet manifest for optimizing Nginx configuration

# Description: Optimizes Nginx configuration for better performance under load

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
