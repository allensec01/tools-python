import socket

target_ip = '127.0.0.1'
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect((target_ip,target_port))
except Exception as error :
    print("[*]Exception connection: ",error)
    exit(0)
    
"""data = "Get /htttp/1.1\r\nhost:google.com\r\n\r\n"
client.sendall(bytes(data,'utf-8'))

respose = client.recv(1024)
print('[*]respose:' ,respose)"""

while True:
    msg = input('inter msg: ')
    client.sendall(bytes(msg,'utf-8'))
    respose = client.recv(1024)
    print('[*]respose:' ,respose)