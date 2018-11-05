import socket

class ReceberSinal:
    def __init__(self, porta):
        self.host = ''
        self.porta = porta
        conect = (self.host, self.porta)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(conect)
        self.server.listen(1)
    def start(self):
        while True:
            con, cliente = self.server.accept()
            print("chegou sinal de",cliente)
            msg = con.recv(1024)
            print(str(msg,"utf-8"))
            con.close()
            