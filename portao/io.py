import socket

class receberSinal:
    def __init__(self, porta):
        self.host = "localhost"
        self.porta = porta
        conect = (self.host, self.porta)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        while True:
            con, cliente = self.server.accept()
            print("chegou sinal de",cliente)
            while True:
                msg = con.recv(1024)
                if not msg: break
                print(msg)