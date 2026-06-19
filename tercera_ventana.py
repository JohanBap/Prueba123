from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton

class VentanaResumen(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        titulo = QLabel("📋 Resumen de Inventario Registrado")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(titulo)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio Unitario", "Valor Total"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tabla)

        btn_nuevo = QPushButton("➕ Agregar Otro Producto.")
        btn_nuevo.clicked.connect(self.controlador.mostrar_ventana_1)
        layout.addWidget(btn_nuevo)

        self.setLayout(layout)

    def actualizar_tabla(self):
        datos = self.controlador.historial_inventario
        self.tabla.setRowCount(len(datos))

        for fila, info in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(info["producto"]))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(info["cantidad"])))
            self.tabla.setItem(fila, 2, QTableWidgetItem(f"${info['precio']:.2f}"))
            self.tabla.setItem(fila, 3, QTableWidgetItem(f"${info['total']:.2f}"))
