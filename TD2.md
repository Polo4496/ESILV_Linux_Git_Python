# TD2
## Exercise 1 : Access general computer informations
1. Put system up to date
```
sudo apt update
```
2. Display

— Linux version
```
```
— Current processes and memory usage associated
```
```
— Display it in a more pleasant way ("more readable for humans")
```
```
— Number of processors
```
```
— L1, L2 and L3 cache size
```
```
— Disk space
```
```
— Monted devices
```
```
— Connected usb devices
```
```
— Hostname
```
```

## Exercise 2 : Shell - Variables and scripts scope
1. Create a variable x and assign it the short text piri pimpin
```
x="piri pimpim"
```
2. Display the value of this variable
```
echo $x
```
3. Add to this value the following text piri pimpon
It should contain the following : piri pimpim piri pimpon
```
x+=" piri pimpom"
```
4. Create a folder named my_programs, then enter into that folder
```
mkdir my_programs
cd my_programs
```
5. Create a script named pilou that displays pilou pilou
```
vim pilou
echo "pilou pilou"
```
6. Run this script
```
source pilou
```
7. Make this script executable
```
chmod u+x pilou
```
8. Run the script by writting its name only
```
./pilou
```
9. Programs called from the terminal are usually found thanks to a variable named PATH
Display the content of the variable PATH
```
echo $PATH
```
10. Add the path of your current location to the global variable PATH
```
PATH=$PATH:$(pwd)
```
11. When you are sure of the result, export it
```
export PATH
```
12. Go to your home directory
```
cd ~
```
13. Run your script by writting its name only
```
pilou
```
14. Change the value of the PATH in the .profile file in order to make it permanent
```
vim .profile
PATH="$PATH:$HOME/my_programs"
```
15. Create a new shell and run your script using its name only
```
source .profile
pilou
```

## Exercise 3 : Scheduling task - daemon
1. Create a script say_hello.sh
— Make it write the current date and time followed by ’Hello’
— It should write it in a file named ’hellos.txt’
— Each new output should be appened to the file (it shouldn’t remove previous hellos)
```
vim say_hello.sh
echo "$(date) - Hello You" >> $HOME/linux_ex_3/hellos.txt
```
2. Make the script executable
```
chmod u+x say_hello.sh
```
3. Use crontab to schedule the running of the script every minute
```

```
