import socket
from email.policy import HTTP
from pickle import GET

target_host = "www.google.com"
target_port = 80

#CREATE A SOCKET OBJECT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONNECT THE CLIENT
client.connect((target_host, target_port))

#SEND SOME DATA
client.send("GET / HTTP/1.1\R\nHost: google.com\r\n\r\n")


#RECEIVE SOME DATA

response = client.recv(4096)

print(response)
