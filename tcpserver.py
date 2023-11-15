import socket
import threading
def handel_client(client):
    client_recv = client.recv(4056)
    print(client_recv)
    msg = input("msg :")
    client.sendall(bytes(msg,'utf-8'))    
    
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP   = '127.0.0.1'
PORT = 9999
server.bind((IP,PORT))
server.listen(5)
print('[+] Listening is on')
client,addr = server.accept()
while True:
    print(f'[#] accepted connection ip:{addr[0]} , port: {addr[1]}')
    #handel_client(client)
    threa = threading.Thread(target=handel_client,args=(client,))
    threa.start()