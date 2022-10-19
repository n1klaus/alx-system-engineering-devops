# Create SSH configuration file for the local SSH client
#+   to connect without password
include 'stdlib'

file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    match   => '^#.*PasswordAuthentication.*',
    replace => true,
}

file_line { 'Delare identity file':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true,
}
