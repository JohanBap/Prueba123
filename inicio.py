import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

from primera_ventana import VentanaBienvenida
from segunda_ventana import VentanaAnalisis
from tercera_ventana import VentanaResumen

class ControladorInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Inventario Inteligente")
        self.setFixedSize(750, 500)

        self.producto_actual = ""
        self.historial_inventario = []

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.vista_bienvenida = VentanaBienvenida(self)
        self.vista_analisis = VentanaAnalisis(self)
        self.vista_resumen = VentanaResumen(self)

        self.stacked_widget.addWidget(self.vista_bienvenida)  
        self.stacked_widget.addWidget(self.vista_analisis)    
        self.stacked_widget.addWidget(self.vista_resumen)     

        self.mostrar_ventana_1()

    def mostrar_ventana_1(self):
        self.stacked_widget.setCurrentIndex(0)

    def mostrar_ventana_2(self):
        self.vista_analisis.actualizar_titulo()
        self.stacked_widget.setCurrentIndex(1)

    def mostrar_ventana_3(self):
        self.vista_resumen.actualizar_tabla()
        self.stacked_widget.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = ControladorInventario()
    ventana_principal.show()
    sys.exit(app.exec_())
