# Control_Rele_UDP_Rpi
Control de salidas digitales en Raspberry Pi via UDP con Python

1.- Ejecutar el script setup.sh.

	1.a) Darle permisos de ejecución (por si viniera sin ellos):
	$ chmod a+x setup.sh
	
	1.b) Ejecutarlo:
	$ ./setup.sh
	
2.- Reiniciar la Raspberry Pi:

	$ sudo reboot
	
3.- Una vez iniciada la Raspberry Pi, comprobar que el servidor está levantado:

	$ ps ax | grep control_gpio_udp.py
	
	Nos dará una salida similar a la siguiente (la primera línea es la importante):
	
	395 ?        S      0:00 python /home/pi/Control_GPIO_UDP/control_gpio_udp.py
	925 pts/2    S+     0:00 grep --color=auto control_gpio_udp.py

4.- Si se ve el proceso anterior, comprobar que funciona el control:

	4.a) Probar activación (deberá poner a nivel alto el pin 13 del GPIO... probar, p.e. con resistencia + LED):
	
	$ python /home/pi/Control_GPIO_UDP/prueba_servidor.py "ON"

	4.b) Probar desactivación (deberá poner a nivel bajo el pin 13 del GPIO):
	
	$ python /home/pi/Control_GPIO_UDP/prueba_servidor.py "OFF"	
	
	
