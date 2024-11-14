import socket
import sys
from io import open

bufferSize          = 1024

direccionIP = "127.0.0.1"
puerto = 7000

def leer_configuracion():
	global direccionIP, puerto
	
	with open('config.cfg', 'r') as fichero_config:
		for linea in fichero_config:
			#print(linea)
			tokens = linea.split('=')
			
			if tokens[0] == 'direccionIP':
				direccionIP = tokens[1]
			elif tokens[0] == 'puerto':
				puerto = int(tokens[1])
		
		fichero_config.close()
			

if len(sys.argv) == 2:
	leer_configuracion()
	serverAddressPort   = (direccionIP, puerto)
	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	
	comando = sys.argv[1]
	UDPClientSocket.sendto(str.encode(comando), serverAddressPort)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from Server: {}".format(msgFromServer[0])
	print(msg)
		

