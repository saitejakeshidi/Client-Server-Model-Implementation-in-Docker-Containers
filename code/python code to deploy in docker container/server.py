import socket
import time
hostname=socket.gethostname()
portnumber=25000
address=('',portnumber)
tcpserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpserver.bind(address)
tcpserver.listen(1)
tcpclient,address=tcpserver.accept()
print("Connection established")
while(1):
    message1=tcpclient.recv(1024).decode()
    localtime = time.asctime( time.localtime(time.time()) )
    print("Message received from the client is:",message1)
    print("Time is:",localtime)
    msg1=input("Enter the message")
    tcpclient.send(msg1.encode())
    print("Message send to client as a response from the server is:",msg1)
tcpserver.close()
