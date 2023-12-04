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
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
