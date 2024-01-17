#Strace is your friend
exec { 'fix wp-settings file':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}