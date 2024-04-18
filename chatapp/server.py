import socket
CHUNK = 65535 # recieve at most these bytes of data at once

port = 3000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

hostname = '127.0.0.1'  #ip addres of local machine , same for everyone

s.bind((hostname, port)) #bind the socket with host machine and port 3000

print(f"server is live on{s.getsockname()}")

#run this server infinetly,till i stop manually
while True: #infinite loop
    data, ClientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')  #data by defaukt travels in bytes
    print("Vraj at {clinetAdd} says : {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    #send data to the ip add that sent me the data
    s.sendto(data, ClientAdd)
