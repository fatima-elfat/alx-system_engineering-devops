file { 'etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  content => 'Host *
      PasswordAuthentication no
      IdentifyFile ~/.ssh/school',
}
