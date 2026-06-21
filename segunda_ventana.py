from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class VentanaAnalisis(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lbl_info = QLabel("")

        self.lbl_info.setStyleSheet("font-size: 25px; font-weight: bold; color: ; margin-bottom: 10px;")
        layout.addWidget(self.lbl_info)

        cantidad = QLabel("Cantidad en Stock:")
        cantidad.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(cantidad)
        

        self.lbl_info.setStyleSheet("font-size: 16px; font-weight: bold; color: #bf4c17; margin-bottom: 10px;")
        layout.addWidget(self.lbl_info)

        layout.addWidget(QLabel("Cantidad en Stock:"))

        self.input_cantidad = QLineEdit()
        self.input_cantidad.setPlaceholderText("Ej. 50")
        layout.addWidget(self.input_cantidad)


        precio = QLabel("Precio Unitario ($):")
        precio.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(precio)
        

        layout.addWidget(QLabel("Precio Unitario ($):"))

        self.input_precio = QLineEdit()
        self.input_precio.setPlaceholderText("Ej. 1200.50")
        layout.addWidget(self.input_precio)

        btn_layout = QHBoxLayout()
        btn_volver = QPushButton("⬅️ Volver")
        btn_volver.clicked.connect(self.controlador.mostrar_ventana_1)
        
        btn_guardar = QPushButton("Guardar y Ver Resumen 💾")
        btn_guardar.clicked.connect(self.procesar_datos)
        
        btn_layout.addWidget(btn_volver)
        btn_layout.addWidget(btn_guardar)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def actualizar_titulo(self):
        self.lbl_info.setText(f"Producto: {self.controlador.producto_actual}")

    def procesar_datos(self):
        try:
            cantidad = int(self.input_cantidad.text().strip())
            precio = float(self.input_precio.text().strip())
        except ValueError:
            cantidad = 0
            precio = 0.0

        total_valor = cantidad * precio

        registro = {
            "producto": self.controlador.producto_actual,
            "cantidad": cantidad,
            "precio": precio,
            "total": total_valor
        }
        self.controlador.historial_inventario.append(registro)

        self.input_cantidad.clear()
        self.input_precio.clear()
        self.controlador.mostrar_ventana_3()
