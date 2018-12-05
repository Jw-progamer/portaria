import socket
import time

qual = 'camera'
while True:
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('enviando sinal para servidor')
    canal = ('localhost', 7200)
    sock_tcp.connect(canal)
    sock_tcp.send(bytearray(qual, "utf-8"))
    if qual == 'espera':
        qual = 'camera'
        print('envie camera')
    else:
        qual = 'espera'
        print('enviei espera')
    sock_tcp.close()
    time.sleep(30)
