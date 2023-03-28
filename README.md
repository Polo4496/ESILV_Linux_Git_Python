# Project - Linux Git Python

Final Project of the course where we have to implement a script scrapping data on a website, store it and produce a dashboard in Python to display the data and a daily report presenting some metrics from the data.

## Virtual Machine

For the project, I needed a virtual machine to deploy the dashboard on a web page accesible from everyone.<br>
I created an account on Google Cloud Plateform and got one. Then I have taken some scripts from the TD to connect automatically to the instance and import/export file from local to remote.<br>
The IP address of my virtual machine where you can find my final website is http://34.155.100.18:8000/ on the port 8000.

## Web Scrapping

I decided to get the data of **AVAX** cryptocurrency for this project.<br>
I have found it on https://crypto.com/price/avalanche and scrapped it with the following code from *get_data_avax.sh* file:
```
actual_price=$(curl https://crypto.com/price/avalanche | grep -oP '(?<=<h2 class="chakra-heading css-64zram">).*?(?=<\/h2>)' | grep -oP '(?<=\$).*?(?=USD)')
actual_date=$(date --date='2hour' "+%A %B %d %Y %H:%M:%S")
echo "$actual_date, $actual_price" >> avax_data.csv
```
The data is then stored in a file *avax_data.csv*.<br>
After that, I had to make this script run automatically **every minute** to get live data (I decided every minute instead of every five minutes in order to get more data and a better graph). To do so, I made a *crontab* task.
```
crontab -e
*/1 * * * * ~/get_data_avax.sh
```

## Report Production

To produce the report I need at 8pm each day, I scheduled another task on crontab:
```
crontab -e
0 20 * * * ~/get_report.sh
```
This command run *get_report.sh* each day at 8pm. The content of this file is the following:
```
python3 ~/report.py
```
It just calls the file *report.py* which will produce the metrics from the data of the last day, and store them in a file *report.csv*.
For example, it computes:
- Return
- Volatility
- Max price
- Min price
- Mean price
- Open price
- Close price

## Web Dashboard

Finally, the file *dashboard_avax.py* contains the code to create the server for our web page, create the dashboard, load the data from *avax_data.csv* and *report.csv* to display them in the interface.<br>
There is an interval such that the files are read and the data is live actualised.<br>
I provided a graph of the prices of AVAX, with an underlying graph representing the RSI of AVAX's price.

## Git

I managed my code using git in linux shell to add, commit and push file in this github repository.

<br>

#### Thanks for taking the time to read this ;)

<br>

*@ESILV 2023 Financial Engineering*
