    ln -s tmp/files/take-the-command-challenge take-the-command-challenge

    find . -type f,d,l -delete

    find . -type f -name "*.doc" -delete

    fgrep -riw ./access.log -e "GET"

    find * -type f -exec grep --color -olsr {} -e "500" \;

    find . -type f -name "access.log*"

    find . -type f -name "access.log*" -exec grep --color -srw {} -e "500" \;

    find . -type f -name "access.log*" -exec grep --only-matching -E {} -e "\b([0-9]{1,3}\.){3}([0-9]{1,3})\b" \;
 
    find . -type f | grep "" -c

