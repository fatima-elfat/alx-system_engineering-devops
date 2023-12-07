#  configuration file task
exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install'],
}
exec { 'install':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['header'],
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
exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart'
}
