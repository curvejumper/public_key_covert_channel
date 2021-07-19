import socket
import ssl

# using: https://docs.python.org/3/library/ssl.html to create ssl/tls server for key exchange

def generate_private_key():
    # Generate a private key for the key exchange with the client
    pass

# maybe generate a certificate? possibly even a fake certificate would work
# as long as the client gets the message

def run_tls_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 8443))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()

if __name__ == "__main__":
    run_tls_server()