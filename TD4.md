# TD4
## Exercise 1: SSH
1. Create an account on a cloud computing platform (AWS, Azure, Google Cloud, IBM Cloud)<br>
— You must enter your credit card number, I have no affiliation<br>
— It is free. Delete the account in few month to prevent any fee
```
I have chosen Google Cloud and created a project Linux-Git-Python ESILV
```
2. Create a server instance on the website of your cloud platform (ec2 for AWS, Standard B1s for Azure)
```
I have called it lgp-instance (IP: 34.155.100.18)
```
3. Connect to the distant server via your terminal<br>
— Do chmod 400 your private key file. The connection won’t work otherwise<br>
— Use an SSH instruction to connect to your remote instance<br>
— Exit to return to your local machine
```
ssh-keygen
cd ~/.ssh
chmod 400 private_key
ssh -i ~/.ssh/private_key plejamtel@34.155.100.18
exit
```
4. Create a script named connect.sh to automatically connect to the remote instance
```
mkdir lgp-instance
cd lgp-instance
vim connect.sh
ssh -i ~/.ssh/private_key plejamtel@34.155.100.18
```
5. Run the script to check it is working properly. Then exit to return to your local machine.
```
source connect.sh
```
6. Rename your private key to make it a hidden file. Propagate the changes to your script. Run the script.
```
cd ~/.ssh
mv private_key .private_key
cd ~/lgp-instance
vim connect.sh
ssh -i ~/.ssh/.private_key plejamtel@34.155.100.18
source connect.sh
```

## Exercise 2: SCP
1. On your local machine create a file named test_to_remote_instance.txt
```
touch test_to_remote_instance.txt
```
2. Connect to your remote instance and create a file named test_from_remote_instance.txt. Then exit.
```
source connect.sh
touch test_from_remote_instance.txt
exit
```
3. Use the scp command to :<br>
— Send your file test_to_remote_instance.txt to the home folder of your remote instance<br>
— Get the file test_from_remote_instance.txt to your current local directory
```
scp test_to_remote_instance.txt plejamtel@34.155.100.18:~
scp plejamtel@34.155.100.18:~/test_from_remote_instance.txt ~/lgp-instance
```
4. Create two scripts :<br>
— scp_to_remote_instance.sh and scp_from_remote_instance.sh to respectively send and get data with your remote instance<br>
— Since you would like to send or receive any file (not just the test file), your scripts should use the path of the file to send / receive as an argument
```
vim scp_to_remote_instance.sh
scp $1 plejamtel@34.155.100.18:~
vim scp_from_remote_instance.sh
scp plejamtel@34.155.100.18:~/$1 ~/lgp-instance
```
5. Test your scripts with varying files
```
touch text.txt
source scp_to_remote_instance.sh test.txt
source connect.sh
ls (we can see the file uploaded)
touch test_remote.txt
exit
source scp_from_remote_instance.sh test_remote.txt
ls (we can see the file downloaded)
```
