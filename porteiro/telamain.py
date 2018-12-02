from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from uis.uimain import Ui_Form
from portaria import Portaria
import threading
import socket


class TelaMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.urls = {}

        self.sock = None
        self.serve =None
        self.ui.configBtn.clicked.connect(self.instanceSocket)
        self.ui.openBtn.clicked.connect(self.openDoor)

    def instanceSocket(self):
        ip = self.ui.iptxt.text()
        porta = int(self.ui.portatxt.text())
        camerahost = 'http://'+ip+':8081'
        self.urls['camera'] = camerahost
        self.urls['espera'] = 'https://www.google.com.br/'
        print(ip, porta, camerahost)
        self.ui.ip_trava.setText(ip)
        self.ui.porta_trava.setText(str(porta))
        self.sock = Portaria(ip, porta)
        self.ui.configBtn.enabled = False
        self.ui.webViewCamera.load(QUrl(self.urls['espera']))
        threading.Thread(target=self.runServer).start()

    def runServer(self):
        print('chego aqui')
        ip = self.ui.iptxt.text()
        self.serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serve.bind((ip,7200))
        self.serve.listen(1)
        while True:
            con, cliente = self.serve.accept()
            print("chegou sinal de", cliente)
            msg = con.recv(1024)
            alias = str((msg, "utf-8"))
            if alias == 'camera':
                self.ui.webViewCamera.load(QUrl(self.urls['camera']))
            elif alias == 'espera':
                self.ui.webViewCamera.load(QUrl(self.urls['espera']))


    def openDoor(self):
        self.sock.enviarSinal()
