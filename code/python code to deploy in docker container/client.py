import socket
import time
hostname='172.17.0.2'
portnumber=25000
address=(hostname,portnumber)
tcpclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpclient.connect(address)
while(1):
    message=input("enter msg")
    tcpclient.send(message.encode())
    print("Message sent to server:")
    print(message)
    msg=tcpclient.recv(1024).decode()
    localtime1 = time.asctime( time.localtime(time.time()))
    print("msg received from server is:",msg)
    print("time is:",localtime1)
tcpclient.close()
