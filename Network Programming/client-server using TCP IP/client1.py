import socket

s = socket.socket()
host = socket.gethostname()
port = 5000

s.connect((host,port))
print('sending message to server..')
s.send(b'hello server!')

with open('received_file.txt','wb') as f:
    print('File opened')
    while True:
        print('receiving data..')
        data = s.recv(1024)
        print('data is',(data))
        if not data:
            break
        f.write(data)

f.close()
print('Successfully got the file')
s.close()
print('connection closed')