#!/usr/bin/env python3
"""
Generates an RSA 4096 key pair to obtain
a key's length. This is done as RSA public
keys are not constant in length due to the
selected prime factors. Therefore, our
covert channel message is never constant
in length and appears less suspicious.
"""
import argparse
from Crypto.PublicKey import RSA # PIP install pycrypto
import socket
import struct
import base64

RSA_BITS = 4096

def gen_pub_key():
	"""
	Returns an RSA public key.
	"""
	key = RSA.generate(RSA_BITS)
	pub_key = key.publickey()
	return pub_key.exportKey()

def connect(hostname, port):
	"""
	Connect to server for covert channel
	"""
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (hostname, int(port))
	sock.connect(server_address)
	return sock

def send_message(sock, message):
	# https://tls.ulfheim.net
	pre_formatted_packet = b'\x16\x03\x03\x00\x25' # record header (tls 1.2)
	pre_formatted_packet += b'\x10' # handshake header (client key exchange)
	# Encode message into base64
	encoded_message = base64.b64encode(message.encode('utf-8'))

	while len(encoded_message) != 0:
		rsa_pub_key = gen_pub_key()

		packet_msg_len = len(encoded_message)
		if len(encoded_message) > len(rsa_pub_key):
			packet_msg_len = len(rsa_pub_key)

		message_to_send = encoded_message[:packet_msg_len]
		message_to_send += rsa_pub_key[:len(rsa_pub_key) - packet_msg_len]
		encoded_message = encoded_message[packet_msg_len:]
		packet = struct.pack('>I', packet_msg_len)[1:] # only need 3 bytes worth
		packet += message_to_send
		print(pre_formatted_packet + packet)
		sock.send(pre_formatted_packet + packet)

def main():
	# Parse arguments from the command line
	print("Parsing arguments...")
	parser = argparse.ArgumentParser(description='RSA Public Key Covert Channel (Raw TCP)')
	parser.add_argument('hostname', help='Server address to send message', type=str, nargs='?', default="127.0.0.1")
	parser.add_argument('port', help='Server port to connect to', type=str, nargs='?', default="4443")
	parser.add_argument('message', help='Message to send', type=str, nargs='?', default="Secret Message!")
	args = parser.parse_args()

	print(f"Connecting to: {args.hostname}:{args.port}")
	sock = connect(args.hostname, args.port)

	print(f"Sending message: {args.message}")
	send_message(sock, args.message)
	print("Done!")

if __name__ == '__main__':
	main()