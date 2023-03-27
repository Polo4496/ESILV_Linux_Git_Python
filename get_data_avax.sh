actual_price=$(curl https://crypto.com/price/avalanche | grep -oP '(?<=<h2 class="chakra-heading css-64zram">).*?(?=<\/h2>)' | grep -oP '(?<=\$).*?(?=USD)')
actual_date=$(date --date='2hour' "+%A %B %d %Y %H:%M:%S")
echo "$actual_date, $actual_price" >> avax_data.csv
