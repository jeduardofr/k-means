# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Nov 16 12:30:24 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etiquetaIteraciones = QtWidgets.QLabel(self.centralwidget)
        self.etiquetaIteraciones.setGeometry(QtCore.QRect(60, 40, 111, 16))
        self.etiquetaIteraciones.setObjectName("etiquetaIteraciones")
        self.etiquetaCorridas = QtWidgets.QLabel(self.centralwidget)
        self.etiquetaCorridas.setGeometry(QtCore.QRect(60, 70, 101, 16))
        self.etiquetaCorridas.setObjectName("etiquetaCorridas")
        self.etiquetaGrupos = QtWidgets.QLabel(self.centralwidget)
        self.etiquetaGrupos.setGeometry(QtCore.QRect(400, 40, 141, 16))
        self.etiquetaGrupos.setObjectName("etiquetaGrupos")
        self.etiquetaError = QtWidgets.QLabel(self.centralwidget)
        self.etiquetaError.setGeometry(QtCore.QRect(400, 80, 47, 13))
        self.etiquetaError.setObjectName("etiquetaError")
        self.cantidadIteraciones = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidadIteraciones.setGeometry(QtCore.QRect(180, 40, 113, 20))
        self.cantidadIteraciones.setObjectName("cantidadIteraciones")
        self.cantidadCorridas = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidadCorridas.setGeometry(QtCore.QRect(180, 70, 113, 20))
        self.cantidadCorridas.setObjectName("cantidadCorridas")
        self.cantidadGrupos = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidadGrupos.setGeometry(QtCore.QRect(540, 40, 113, 20))
        self.cantidadGrupos.setObjectName("cantidadGrupos")
        self.error = QtWidgets.QLineEdit(self.centralwidget)
        self.error.setEnabled(False)
        self.error.setGeometry(QtCore.QRect(540, 70, 113, 20))
        self.error.setObjectName("error")
        self.botonAlgoritmo = QtWidgets.QPushButton(self.centralwidget)
        self.botonAlgoritmo.setGeometry(QtCore.QRect(330, 480, 101, 23))
        self.botonAlgoritmo.setObjectName("botonAlgoritmo")
        self.tablaResultados = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaResultados.setGeometry(QtCore.QRect(30, 120, 711, 331))
        self.tablaResultados.setObjectName("tablaResultados")
        self.tablaResultados.setColumnCount(0)
        self.tablaResultados.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_archivo = QtWidgets.QAction(MainWindow)
        self.actionAbrir_archivo.setObjectName("actionAbrir_archivo")
        self.menuArchivo.addAction(self.actionAbrir_archivo)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "K-Means", None, -1))
        self.etiquetaIteraciones.setText(QtWidgets.QApplication.translate("MainWindow", "Número de iteraciones", None, -1))
        self.etiquetaCorridas.setText(QtWidgets.QApplication.translate("MainWindow", "Número de corridas", None, -1))
        self.etiquetaGrupos.setText(QtWidgets.QApplication.translate("MainWindow", "Número de grupos a buscar", None, -1))
        self.etiquetaError.setText(QtWidgets.QApplication.translate("MainWindow", "Error", None, -1))
        self.botonAlgoritmo.setText(QtWidgets.QApplication.translate("MainWindow", "Ejecutar algoritmo", None, -1))
        self.menuArchivo.setTitle(QtWidgets.QApplication.translate("MainWindow", "Archivo", None, -1))
        self.actionAbrir_archivo.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir archivo", None, -1))

