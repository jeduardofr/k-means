from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem
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

        # Proceed to draw general results
        columns = ["# Ronda", "# de Iteraciones", "Error"]
        self.ui.tablaGenerales.setColumnCount(3)
        self.ui.tablaGenerales.setHorizontalHeaderLabels(columns)
        self.ui.tablaGenerales.setRowCount(corridas)

        row = 0
        for s in k.snapshots:
            self.ui.tablaGenerales.setItem(row, 0, QTableWidgetItem(str(row+1)))
            self.ui.tablaGenerales.setItem(row, 1, QTableWidgetItem(str(s["iterations"])))
            self.ui.tablaGenerales.setItem(row, 2, QTableWidgetItem(str(s["error"])))
            row += 1


        # Proceed to draw data
        columns = [x for x in self.data.columns]
        columns.append("cluster")
        self.ui.tablaResultados.setColumnCount(6)
        self.ui.tablaResultados.setHorizontalHeaderLabels(columns)
        self.ui.tablaResultados.setRowCount(len(self.data))

        # Get the snapshot with the lowest error
        min, index = k.snapshots[0]["error"], 0
        for i in range(1, len(k.snapshots)):
            if k.snapshots[i]["error"] < min:
                min, index = k.snapshots[i]["error"], i

        self.ui.error.setText(str(k.snapshots[index]['error']))

        nodes = k.snapshots[index]['data']
        row = 0
        for i in range(len(nodes)):
            self.ui.tablaResultados.setItem(row, 0, QTableWidgetItem(str(nodes[i].points[0])))
            self.ui.tablaResultados.setItem(row, 1, QTableWidgetItem(str(nodes[i].points[1])))
            self.ui.tablaResultados.setItem(row, 2, QTableWidgetItem(str(nodes[i].points[2])))
            self.ui.tablaResultados.setItem(row, 3, QTableWidgetItem(str(nodes[i].points[3])))
            self.ui.tablaResultados.setItem(row, 4, QTableWidgetItem(self.data["class"][i]))
            self.ui.tablaResultados.setItem(row, 5, QTableWidgetItem("C{}".format(nodes[i].centroid_id)))
            row += 1
