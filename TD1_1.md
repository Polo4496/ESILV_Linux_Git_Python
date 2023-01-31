# TD1
## Exercise 1 : Move around
1. Go to the root directory
```
cd /
```
2. Display the content of the current (root) directory
```
ls
```
3. Check your current location
```
pwd
```
4. Try to create a directory named test (we don't have permissions)
```
mkdir test
```
5. Go to the general home directory (should contain folders named after each user)
```
cd home
```
6. Go to your home directory
```
cd plejamtel
```
7. Go back to the general home directory (located "just above")
```
cd ..
```
8. Go again "just above", you should be back to the root directory
```
cd ..
```
9. Go directly to your home directory (named after you). It should be a very simple command, which take no name as parameter of the path
```
cd ~
```
10. Try to create a directory named test
```
mkdir test
```
11. Go into this new directory
```
cd test
```
12. Check your current location
```
pwd
```

## Exercise 2 : Create, Rename, Copy, Delete
1. Go to your home directory (should be named after you, you might be
there by default)
```
cd ~
```
2. Check your current location
```
pwd
```
3. Create a folder linux_ex_1
```
mkdir linux_ex_1
```
4. Go into this folder
```
cd linux_ex_1
```
5. Create an empty text file named [first_name]_[last_name].txt (e.g. alexis_bogroff.txt)
```
touch paul_lejamtel.txt
```
6. Create a folder notes
```
mkdir notes
```
7. Move your text file into this folder
```
mv paul_lejamtel.txt notes
```
8. Rename the text file by appending the current year [first_name]_[last_name]_[current_year].txt
```
mv paul_lejamtel.txt paul_lejamtel_2023.txt
```
9. Make a copy of this folder, name it notes_2022
```
cp -R notes notes_2023
```
10. Delete the first folder (notes) using the verbose option
```

```

## Exercise 3 : Create and run a script
1. Create a script script_1.sh in the folder linux_ex_1
```
```
2. In the script, write the commands that would output the following :
Script running please wait ...
Done.
```
```
3. Quit editing and save the script
```
```
4. Display the content of the script (using a command, not from an editor)
```
```
5. Run the script
```
```

## Exercise 4 : Accessing or modifying a file : permissions and root privilege
### Exercise 4.1 : Change the rights for accessing  or modifying a file
1. Create a file credentials in the folder linux_ex_1
(a) Write any kind of (fake) personal information within the file
```
```
(b) Display the file content
```
```
(c) Display the current permissions
```
```
2. Change the current permissions to : read only for all users
(a) Display the new permissions
```
```
(b) Modify and save the file
```
```
(c) Display the file content
```
```
3. Change the permissions back to read and write for all users
(a) Display the new permissions
```
```
(b) Modify and save the file
```
```
(c) Display the file content
```
```
On the same file :
1. Add the execute permission to the owner
(a) Display the new permissions
```
```
2. Remove the read permission to other users
(a) Display the new permissions
```
```
3. Change the permissions to read, write and execute for all users
(a) Display the new permissions
```
```

### Exercise 4.2 : Access root files
1. Go to the root folder
```
```
2. Create a file in root user mode named .private_file
(a) Write some information in the file
```
```
(b) Display the file content
```
```
(c) Display all the files in the folder including hidden files
```
```
3. Modify the file in normal user mode
(a) Write some new information in the file
```
```
(b) Display the file content
```
```
4. Modify the file in root user mode
(a) Write some new information in the file
```
```
(b) Display the file content
```
```
5. Change permissions to read, write and execute for all users
(a) Modify the file content in normal user mode
```
```
(b) Display the file content
```
```

### Exercise 4.3 : Change a file owner
1. Change permissions of .private_file to read and write for all users, in
normal user mode
```
```
2. Set the new file owner as the current user
```
```
3. Change permissions of .private_file to read and write for all users, in
normal user mode
```
```

### Exercise 4.4 : Manage Packages (tools/functions)
1. Update your main package manager named apt
```
```
2. Upgrade apt
```
```
3. Install the package cmatrix
```
```
4. Launch cmatrix
```
```
5. Quit cmatrix
```
```
6. Install the package tmux
```
```
7. Launch tmux
```
```
8. Say "Hello session 0" using bash in your current tmux session
```
```
9. Launch cmatrix in your current tmux session
```
```
10. Detach from the current tmux session (without stopping cmatrix)
```
```
11. Create a new tmux session
```
```
12. Say "Hello session 1" using bash in your new tmux session
```
```
13. Detach from the current tmux session
```
```
14. List all running sessions
```
```
15. Attach again to session 0
```
```
16. Detach again
```
```
17. Attach again to session 1
```
```
18. Detach again
```
```
19. List all running sessions
```
```
20. Kill all tmux sessions and quit tmux
```
```
21. List all sessions
```
```

### Exercise 4.5 : Use functions arguments / parameters
1. Display the cmatrix help function
```
```
2. Launch cmatrix and make it display white characters (in place of the green)
```
```
3. Re-launch cmatrix and slow down the speed of characters actualization
```
```
4. Stop cmatrix
```
```
5. Launch cmatrix with both :
— A slow speed of characters actualization
— Blue characters
```
```
6. Display cmatrix manual (different from the help notice)
```
```
7. Display the tmux help function
```
```
8. Display the tmux manual
```
```

