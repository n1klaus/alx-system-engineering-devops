    cat access.log | sort

    find . -type f -name "access.log" -exec grep --no-messages --count --word-regexp {} -e "GET" \;
 
    find . -type f -name "split-me.txt" -exec grep --only-matching --no-messages -E {} -e "\b([0-9]{1,9}){1}\b" \;
 
    seq -s " " 1 100

    find . -type f -name "*.txt" -exec sed -i '/challenges are difficult/d' {} \;

    awk -F '\n' '{ sum += $0 } END { print sum }' sum-me.txt

    find . -type f -printf "%f\n"

    find . -name "*.*" -exec sh -c 'f="{}"; mv -- "$f" "${f%.*}"' \;

    find . -type f -printf "%f\n" | tr ' ' '.'

