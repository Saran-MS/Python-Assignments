import socket

udp_ip = '127.0.0.1'
udp_port = 8014

fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fd.bind((udp_ip,udp_port))

while True:
    print("server listening..")
    r,ip = fd.recvfrom(1024)
    print("client : {}".format(r.decode()) )
    reply = input('server : ')
    reply = reply.encode()
    fd.sendto(reply,ip)