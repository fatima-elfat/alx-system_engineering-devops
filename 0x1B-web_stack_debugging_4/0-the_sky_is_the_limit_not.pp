#Sky is the limit, let's bring that limit higher
exec {'change ulimit':
  provider => shell,
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  before   => Exec['nginx re'],
}

exec {'nginx re':
  provider => shell,
  command  => 'sudo service nginx restart',
}
