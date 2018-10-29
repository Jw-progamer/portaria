from PyQt5.QtWidgets import QApplication
from telamain import TelaMain
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =TelaMain()
    main.show()
    sys.exit(app.exec_())