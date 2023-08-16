import sys 
import socket
import threading

global_ports = list(range(130,136))
def scan(ip):
    #print (" [ + ] Start  Thread " )
    while(len(global_ports) != 0):
        port = global_ports.pop(0)
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(ip,port)
            print(' [+] ' + str(port) + " open port")
        except  :
            print(' [-] ' + str(port) + " dont open port")


ip = sys.argv[1]  # input
threads = []
for i in range(10):
    t = threading.Thread(target=scan,args=(ip,))
    threads.append(t)

for t in threads :
    t.start()

while (True):
    pass