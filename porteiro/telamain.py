from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl, QThread, pyqtSignal
from uis.uimain import Ui_Form
from portaria import Portaria
import socket

class serverThread(QThread):

    changeCamera = pyqtSignal()
    changeEspera = pyqtSignal()

    def __init__(self, urls):
        QThread.__init__(self)
        self.serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serve.bind(('localhost', 7200))
        self.serve.listen(1)
        self.urls = urls

    def run(self):
        print('chego aqui no socket')
        while True:
            print("chego no loop de novo")
            con, cliente = self.serve.accept()
            print("chegou sinal de", cliente)
            msg = con.recv(1024)
            con.close()
            print(msg)
            alias = str(msg, "utf-8")
            print(alias)
            if alias == 'camera':
                print('cheguei na câmera')
                print(self.urls['camera'])
                self.changeCamera.emit()
            elif alias == 'espera':
                print('cheguei na espera')
                print(self.urls['espera'])
                self.changeEspera.emit()


class TelaMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.urls = {}
        self.url = QUrl('https://www.google.com.br/')
        self.qserver = serverThread(self.urls)

        self.sock = None
        self.serve =None
        self.ui.configBtn.clicked.connect(self.instanceSocket)
        self.ui.openBtn.clicked.connect(self.openDoor)
        self.qserver.changeCamera.connect(self.changeToCamera)
        self.qserver.changeEspera.connect(self.changeToEspera)

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
        self.ui.webViewCamera.load(self.url)
        self.qserver.start()

    def changeToCamera(self):
        self.ui.webViewCamera.load(QUrl(self.urls['camera']))

    def changeToEspera(self):
        self.ui.webViewCamera.load(QUrl(self.urls['espera']))



    def openDoor(self):
        self.sock.enviarSinal()

