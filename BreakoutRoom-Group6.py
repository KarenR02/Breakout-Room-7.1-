#Option 2: New Code - Create an IPv4/IPv6 Address Application

import urllib
import requests

external_ip = urllib.request.urlopen('https://ident.me/').read().decode('utf8')
#Requesting the external IP address using an API

url = "https://ipapi.co/" + external_ip + "/json"
#The API that gets information from the external_ip

json_info = requests.get(url).json()
#Requesting the JSON data from url

column_title = ["ISP", "IP Add" , "IP Version", "Country", "Region", "City", "Postal Code"]
#The printed labels for each data

json_columntitle = ["org", "ip", "version", "country_name", "region", "city", "postal"]
#Keys that call data from the JSON

for i in range(len(column_title)):
    print(column_title[i] + ": " + json_info[json_columntitle[i]]) 
#Displaying the output