import requests


url = "http://192.168.254.129/DVWA/vulnerabilities/brute/"
param = {"username" : "admin" , "password" : "password" ,"Login" :"Login"}
cookie ={"security":"low", "PHPSESSID":"d80lfk4i81thqk2hhbpppl9a3h"}
req = requests.get(url,params=param,cookies=cookie)
txt = req.text
print(txt)
if "Welcome" in txt:
    print("true")


    
            
            
            
    


