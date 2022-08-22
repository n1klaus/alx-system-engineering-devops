# Processes and Signals
- ***0-what-is-my-pid*** - displays its own PID
- ***1-list_your_processes*** - displays a list of currently running processes.
    >* Must show all processes, for all users, including those which might not have a TTY
    >* Display in a user-oriented format
    >* Show process hierarchy
- ***2-show_your_bash_pid*** - displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process
- ***3-show_your_bash_pid_made_easy*** - displays the PID, along with the process name, of processes whose name contain the word `bash`
- ***4-to_infinity_and_beyond*** - displays `To infinity and beyond` indefinitely
- ***5-dont_stop_me_now*** - stops `4-to_infinity_and_beyond` process
- ***6-stop_me_if_you_can*** - stops `4-to_infinity_and_beyond` process
- ***7-highlander*** - displays:
    >* `To infinity and beyond` indefinitely
    >* With a sleep 2 in between each iteration
    >* `I am invincible!!!` when receiving a `SIGTERM` signal`
- ***8-beheaded_process*** - kills the process `7-highlander`
- ***100-process_and_pid_file*** - Creates the file `/var/run/myscript.pid` containing its PID
    >* Displays `To infinity and beyond` indefinitely
    >* Displays `I hate the kill command` when receiving a `SIGTERM` signal
    >* Displays `Y U no love me?!` when receiving a `SIGINT` signal
    >* Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal
- ***101-manage_my_process*** - manages `manage_my_process`
    `manage_my_process` is a Bash script that:
    >* Indefinitely writes `I am alive!` to the file `/tmp/my_process`
    >* In between every `I am alive!` message, the program should pause for 2 seconds
- ***102-zombie.c*** - C program that creates 5 zombie processes. For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
