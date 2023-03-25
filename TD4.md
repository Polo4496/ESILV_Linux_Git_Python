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
vim connect.sh
ssh -i ~/.ssh/.private_key plejamtel@34.155.100.18
source connect.sh
```
