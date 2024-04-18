from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys 
from sidebar import UpdaterV2

app = QApplication(sys.argv)

window = UpdaterV2()

window.show()
app.exec()