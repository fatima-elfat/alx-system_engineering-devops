#  configuration file task.
include 'stdlib'

exec { 'update':
  command => '/usr/bin/apt-get update'
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  require => Exec['update']
}
exec { 'restart':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
package { 'nginx':
  ensure => installed,
  require => Exec['install Nginx']
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
file_line { 'header':
  ensure   => 'present',
  after    => 'http {',
  path     => '/etc/nginx/nginx.conf',
  multiple => true,
  line     => 'add_header X-Served-By \"${hostname}\";',
  notify   => Exec['restart'],
}
