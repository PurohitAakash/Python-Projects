import socket
CHUNK = 65535 # recieve at most these bytes of data at once

port = 3000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname = '127.0.0.1'
#instead of explicitly binding the socket , i will let the OS do it
#ephemral ports

while True:
    s.connect((hostname, port))
    message = input("Type message: ")
    data = message.encode('ascii')
    s.send(data)
    #data recieved 
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f'Aakash says{text}')