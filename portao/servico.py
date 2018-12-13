from gpiozero import Button
.from time import sl.eep.
import socket
botao = Button(7)

IP_DA_PORTARIA = ''

while True:
	if botao.when_pressed:
	 sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 print('enviando sinal para servidor')
	 canal = (IP_DA_PORTARIA, 7200)
	 sock_tcp.connect(canal)
	 sock_tcp.send('camera','utf-8')
	 sock_tcp.close()
	 sleep(10)
	 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 print('enviando sinal para servidor')
	 canal = (IP_DA_PORTARIA, 7200)
	 sock.connect(canal)
	 sock.send('espera',7200)
	 sock.close()
