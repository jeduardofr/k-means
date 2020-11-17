from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot, QStandardPaths
from ui_mainwindow import Ui_MainWindow
import pandas as pd
from kmeans import KMeans


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botonAlgoritmo.clicked.connect(self.k_means)
        self.ui.actionAbrir_archivo.triggered.connect(self.abrir_archivo)
        self.file = None
        self.data = None

    @Slot()
    def abrir_archivo(self):
        location = QStandardPaths.standardLocations(QStandardPaths.HomeLocation)
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', location[0], 'CSV Files(*.csv)')
        self.data = pd.read_csv(ubicacion[0])

    @Slot()
    def k_means(self):
        iteraciones = int(self.ui.cantidadIteraciones.text())
        corridas = int(self.ui.cantidadCorridas.text())
        clusters = int(self.ui.cantidadGrupos.text())

        if self.data is None:
            print("No data loaded")
            return

        k = KMeans(clusters, corridas, iteraciones)
        without_class = self.data.drop(columns=["class"])
        k.set_data(without_class)
        k.solve()
        # k.snapshots contiene todos los resultados
