import socket
import struct
import base64

# listening on localhost
IFACE = "127.0.0.1"
PORT = 4443

# read 4096 bytes from the socket at a time
bufferSize  = 4096

# Create a datagram socket
TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Bind to address and ip
TCPServerSocket.bind((IFACE, PORT))
TCPServerSocket.listen(1)

print("TCP server up and listening")

# Listen for incoming packets
while(True):
    # Wait for a connection
    # https://pymotw.com/3/socket/tcp.html
    print('waiting for a connection')
    connection, client_address = TCPServerSocket.accept()

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(bufferSize)
        if data.startswith(b'\x16\x03\x03\x00\x25\x10'):
            msg_len = struct.unpack('>I', b'\0' + data[6:9])[0]
            msg = data[9:9+msg_len]
            msg = base64.b64decode(msg)
            print('received {!r}'.format(msg.decode()))
        if not data:
            break
