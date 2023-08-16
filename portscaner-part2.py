import sys
import socket
import threading 

ports =[443,80]
def scan(ip):
    while (len(ports) != 0):
        port = ports.pop(0)
        try:
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.connect((ip,ports))
            print ('[+]',str(port),'is open')
        except :
            print('[-]',str(port),"is not open")
        
count = int(sys.argv[1])
ip = []

for i in range(2,2+count,1):
    print(sys.argv[i])
    ip.append(sys.argv[i])
    
threads =[]   
for i in range(2):
    ip1 = ip.pop()
    th = threading.Thread(target=scan,args=(ip1,))
    threads.append(th)

for t in threads:
    t.start()

while (True):
    pass