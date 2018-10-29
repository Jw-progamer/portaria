from PyQt5.QtWidgets import QWidget
from uis.uimain import Ui_Form
from dialog import ConfigDialog

class TelaMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        config = ConfigDialog()
        config.show()
        config.exec_()


