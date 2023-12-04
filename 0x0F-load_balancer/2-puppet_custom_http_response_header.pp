#  configuration file task.
include 'stdlib'
exec {'update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure => installed,
}
-> file_line { 'header':
  path  => '/etc/nginx/sites-enabled/default',
  after  => '/server_name',
  line  => "_/a add_header X-Served-By $HOSTNAME;",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
