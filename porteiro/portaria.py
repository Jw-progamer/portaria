import socket


class Portaria:
    def __init__(self, ip, porta):
        self.ip_porta = ip
        self.porta = porta

    def enviarSinal(self):
        self.sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('enviando sinal para',self.ip_porta,self.porta)
        canal = (self.ip_porta, self.porta)
        self.sock_tcp.connect(canal)
        self.sock_tcp.send(bytearray('Acesso Liberado, Abra o portão', "utf-8"))
        self.sock_tcp.close()
