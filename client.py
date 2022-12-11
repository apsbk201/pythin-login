import socket
from getpass import getpass
# from pwinput import pwinput
global i
i = 0

def login():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    message = client.recv(1024).decode()
    client.send(input(message).encode())

    message = client.recv(1024).decode()
    message = getpass('Password: ')
    # message = pwinput('Password: ', '*')

    client.send(message.encode())
    # client.send(input(message).encode())
    msg = str(client.recv(1024).decode())
    client.close()
    print(msg)
    return msg

while i < 3:

    msg = login()
    if msg == 'Login failed' :
        i += 1
        print("---------------------------------------")

    if msg == 'Login successfull' :
        print('Be care full')
        exit()
