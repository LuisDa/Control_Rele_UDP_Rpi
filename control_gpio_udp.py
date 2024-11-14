import RPi.GPIO as GPIO
import socket
from io import open

#https://raspberrytips.com/autostart-a-program-on-boot/
#https://unix.stackexchange.com/questions/20357/how-can-i-make-a-script-in-etc-init-d-start-at-boot

#Valores por defecto del pin, IP y puerto
pin_rele = 11 #Pin 11 de la placa de GPIO, serigrafiado como #17

direccionIP = "127.0.0.1"
puerto = 7000

bufferSize = 1024

ejecutar_servidor = True

#Ver esta URL para el pineado GPIO: https://pinout.xyz/pinout/pin23_gpio11/
def configurar_GPIO():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin_rele, GPIO.OUT)

#Leemos los parAmetros de configuraciOn
def leer_configuracion():
	global direccionIP, puerto, pin_rele
	
	with open('/home/pi/projects/Control_GPIO_UDP/Control_Rele_UDP_Rpi/config.cfg', 'r') as fichero_config:
		for linea in fichero_config:
			tokens = linea.split('=')
			
			if tokens[0] == 'direccionIP':
				print("IP: {}".format(tokens[1]))
				direccionIP = tokens[1]
			elif tokens[0] == 'puerto':
				print("Puerto: {}".format(tokens[1]))
				puerto = int(tokens[1])
			elif tokens[0] == 'pin_rele':
				pin_rele = int(tokens[1])
				print("PIN GPIO: {}".format(tokens[1]))
		
		fichero_config.close()


#Mensaje recibido
leer_configuracion()

configurar_GPIO()

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((direccionIP, puerto))

while ejecutar_servidor:
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)	
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]	
	#clientMsg = "Recibido mensaje: {}".format(message)
	#clientIP  = "Client IP Address: {}".format(address)
	
	print("Recibido {} de IP {}".format(message, address))
	
	respuesta = ""
	
	if message == "ON":
		GPIO.output(pin_rele,True)
		respuesta = "Rele activado"
	elif message == "OFF":
		GPIO.output(pin_rele,False)
		respuesta = "Rele desactivado"
	elif message == "PARAR":
		ejecutar_servidor = False
		respuesta = "El servidor se ha parado"
		
	bytesToSend = str.encode(respuesta)
	UDPServerSocket.sendto(bytesToSend, address)

