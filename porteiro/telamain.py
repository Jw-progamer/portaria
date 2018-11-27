from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from uis.uimain import Ui_Form
from portaria import Portaria


class TelaMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.webViewCamera.load(QUrl('/uis/espera.html'))

        self.sock = None
        self.ui.configBtn.clicked.connect(self.instanceSocket)
        self.ui.openBtn.clicked.connect(self.openDoor)

    def instanceSocket(self):
        ip = self.ui.iptxt.text()
        porta = int(self.ui.portatxt.text())
        print(ip, porta)
        self.ui.ip_trava.setText(ip)
        self.ui.porta_trava.setText(str(porta))
        self.sock = Portaria(ip, porta)
        self.ui.configBtn.enabled = False

    def openDoor(self):
        self.sock.enviarSinal()
