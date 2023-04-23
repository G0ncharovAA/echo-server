import socket
import threading

IP = '127.0.0.1'
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(([IP], [PORT]))

def listen_thread():
    while True:
        data = s.recv(1024)
        print(data.decode('ascii'))

listen_thread = threading.Thread(target=listen_thread)
listen_thread.start()

def send_message(msg):
    s.send(msg.encode('ascii'))

prompt = ""
while prompt !=  "q":
    prompt = input()
    send_message(prompt)
