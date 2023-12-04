#  configuration file task.
include 'stdlib'

exec { 'update':
  command => '/usr/bin/apt-get update'
}

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  require => Exec['update']
}
exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  require => Package['nginx']
}
package { 'nginx':
  ensure => installed,
  require => Exec['install']
}
exec { 'header':
  provider    => shell,
  environment => ["tmph=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$tmph\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart'],
}
