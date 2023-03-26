# TD5
## Exercise 1: Extract data from a website
The Domesday Book is the greatest medieval census. It lists the manors (private properties) in every place of every county in England in the years 1066 and 1086, before and after the Norman conquest. OpenDomesday presents it in a modern-human-readable website, as well as an *application programming interface* (API). We will use this API to extract some data from our command-line shell.

### Exercise 1.1: curl

Check the data on https://opendomesday.org/api/, for instance
- *https://opendomesday.org/api/1.0/county/*
- *https://opendomesday.org/api/1.0/place/2346/*
- *https://opendomesday.org/api/1.0/manor/181/*

Can you find other interesting URLs ?

**Yes, there is https://opendomesday.org/api/1.0/county/[id_county] to get informations about a specific county.**

### Exercise 1.2: curl and grep
Let’s try to get the ids for all the places in Derbyshire !
```
curl https://opendomesday.org/api/1.0/county/ | grep -o "{[^}]*\"name\":\"Derbyshire\"[^}]*}" | grep -o '"id":[^,}]*'
```
We can see with this command that the *id* of Derbyshire is **dby**. So we can use the other link so it is easier to acces information.
```
mkdir linux_API
cd linux_API
curl https://opendomesday.org/api/1.0/county/dby/ | grep -o '[^{}]*"id":[^,}]*' | grep -o '[^:]*$' | tail -n +2 > "ids.txt"
cat ids.txt
```
Now we have all the ids of the places in Derbyshire in a file.

### Exercise 1.3: curl, grep and for
Now that we have ids for all the places in Derbyshire, we can load all their details...
And from their details, we can list all the details of their manors.
Go grep the data !
```
mkdir places_details
mkdir manors_details
```
To create the directories to put the details about places and manors we will load.
```
while read id; do 
  content=$(curl https://opendomesday.org/api/1.0/place/$id/);
  echo $content > "places_details/${id}_details.json";
  manor=$(cat "places_details/1036_details.json" | grep -o '[^,]*"manors":[^,}]*' | grep -o '[^:}]*$');
  content=$(curl https://opendomesday.org/api/1.0/manor/$manor/);
  echo $content > "manors_details/place_${id}_manor.json";
done<ids.txt
```
Then we have loaded every informations about places in our file *ids.txt* in a new file *[id]_details.json* and about the manor in *place_[id]_manor.json*.
