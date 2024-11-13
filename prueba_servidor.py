import socket
import sys

serverAddressPort   = ("127.0.0.1", 7000)
bufferSize          = 1024

if len(sys.argv) == 2:
	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
	comando = sys.argv[1]
	UDPClientSocket.sendto(str.encode(comando), serverAddressPort)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from Server {}".format(msgFromServer[0])
	print(msg)
		

