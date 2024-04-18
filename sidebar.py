from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class UpdaterV2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Colibri Updater")

        self.icon_name_widget.setHidden(True)

        self.home_1.clicked.connect(self.switch_to_homePage)
        self.home_2.clicked.connect(self.switch_to_homePage)

        self.offlineInstall_1.clicked.connect(self.switch_to_offlineInstallPage)
        self.offlineInstall_2.clicked.connect(self.switch_to_offlineInstallPage)

        self.logs_1.clicked.connect(self.switch_to_logsPage)
        self.logs_2.clicked.connect(self.switch_to_logsPage)

        self.hideShells_1.clicked.connect(self.switch_to_hideShellsPage)
        self.hideShells_2.clicked.connect(self.switch_to_hideShellsPage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

    #Different methods to actually switch between different dashboards
    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_offlineInstallPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_logsPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_hideShellsPage(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)