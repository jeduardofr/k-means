from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot, QStandardPaths
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botonAlgoritmo.clicked.connect(self.k_means)
        self.ui.actionAbrir_archivo.triggered.connect(self.abrir_archivo)

    @Slot()
    def abrir_archivo(self):
        location = QStandardPaths.standardLocations(QStandardPaths.HomeLocation)
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', location[0], 'CSV Files(*.csv)')

    @Slot()
    def k_means(self):
        print("Hello world")
