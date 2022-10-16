# Create SSH configuration file for the local SSH client
#+   to connect without password

mod 'saz-ssh', '9.0.0'

class opensssh {
    package { 'openssh-client':
        ensure => 'latest',
    }
}

class { 'ssh::client':
    validate_sshd_file => true,
    storeconfigs_enabled => false,
    options => {
        'HOST *' => {
            'HostName'                => '3.238.134.11901',
            'User'                    => 'ubuntu',
            'PasswordAuthentication'  => 'no',
            'IdentityFile'            => '~/.ssh/school',
        }
    },
}
