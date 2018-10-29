from PyQt5.QtWidgets import QDialog
from uis.uiconfig import Ui_Dialog

class ConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)