#increase for hard and soft files
$myvar = "/etc/security/limits.conf"
exec {'hard incr':
  provider => shell,
  command  => 'sudo sed -i "s/ile 5/ile 50000/" $myvar',
  before   => Exec['soft inc'],
}

exec {'soft incr':
  provider => shell,
  command  => 'sudo sed -i "s/ile 4/ile 40000/" $myvar',
}
