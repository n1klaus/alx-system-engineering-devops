# Fix Apache server error 500
exec { 'enable environment variables':
    provider => shell,
    command  => '. /etc/apache2/envvars',
}

package { 'nscd':
    ensure   => installed,
    provider => 'apt',
}

exec { 'start nscd':
    provider => shell,
    command  => '/etc/init.d/nscd start; /usr/sbin/nscd -i hosts',
    require  => PACKAGE['nscd'],
}

exec { 'start resolvconf':
    provider => shell,
    command  => '/usr/sbin/service resolvconf restart; /usr/sbin/service resolvconf enable-updates',
    onlyif   => '/usr/bin/which resolvconf',
}

package { 'libapache2-mod-fcgid':
    ensure   => installed,
    provider => 'apt',
}

package { 'apache2-suexec-custom':
    ensure   => installed,
    provider => 'apt',
}

exec { 'enable suexec':
    provider => shell,
    command  => '/usr/sbin/a2enmod suexec',
    require  => PACKAGE['libapache2-mod-fcgid', 'apache2-suexec-custom'],
}

exec { 'start mysql':
    provider => shell,
    command  => '/etc/init.d/mysql restart',
}

exec { 'start apache2':
    provider => shell,
    command  => '/etc/init.d/apache2 restart',
}
