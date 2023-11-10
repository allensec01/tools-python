import requests
from bs4 import BeautifulSoup
import json
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument('-d','--domain')
arg = parser.parse_args()

url = arg.domain
if '.txt' in url:
    with open(url) as file:
       url_lst =[line.strip() for line in file]
subdomain = []


abuse = requests.get('https://www.abuseipdb.com/whois/' + url).text
soup = BeautifulSoup(abuse, 'lxml')
list_items = soup.find_all('li')

for item in list_items:
    subdomain.append(item.text + '.'+url)


jldc = requests.get("https://jldc.me/anubis/subdomains/" + url).content

data = json.loads(jldc)
for item in data:
    subdomain.append(item)


certsh = requests.get('https://crt.sh/?q=%.' + url + '&output=json').text

d = json.loads(certsh)


for i in d:
    subdomain.append(i['name_value'])
  


res = list(set(subdomain))
print (res)
result = '\n'.join(res).replace('*.', '')


#print(result)




