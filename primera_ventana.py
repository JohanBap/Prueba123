from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaBienvenida(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        titulo = QLabel("📊 Sistema de Inventario")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(titulo)

        layout.addWidget(QLabel("Ingrese el nombre del producto:"))
        self.input_producto = QLineEdit()
        self.input_producto.setPlaceholderText("Ej. Laptop, Teléfono...")
        layout.addWidget(self.input_producto)

        btn_siguiente = QPushButton("Siguiente ➡️")
        btn_siguiente.clicked.connect(self.ir_a_la_siguiente)
        layout.addWidget(btn_siguiente)

        self.setLayout(layout)

    def ir_a_la_siguiente(self):
        producto = self.input_producto.text().strip()
        if not producto:
            producto = "Producto Genérico"

        self.controlador.producto_actual = producto
        self.controlador.mostrar_ventana_2()
        self.input_producto.clear()

