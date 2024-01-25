#increase for hard and soft
exec {'hard incr':
  provider => shell,
  command  => 'sudo sed -i "s/ile 5/ile 50000/" /etc/security/limits.conf',
  before   => Exec['soft incr'],
}

exec {'soft incr':
  provider => shell,
  command  => 'sudo sed -i "s/ile 4/ile 40000/" /etc/security/limits.conf',
}
