from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget
import sys

class VentanaEjercicio4(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración del tamaño de la ventana
        self.setWindowTitle("Ejercicio 4")
        self.setGeometry(100, 100, 400, 300)

        # se crea los campos de entrada de los datos
        layout = QVBoxLayout()

        for i in range(1, 4):  # Para 3 mascotas
            layout.addWidget(QLabel(f"Mascota {i} - Nombre:"))
            layout.addWidget(QLineEdit())

            layout.addWidget(QLabel(f"Mascota {i} - Edad:"))
            layout.addWidget(QLineEdit())

            layout.addWidget(QLabel(f"Mascota {i} - Tipo:"))
            layout.addWidget(QLineEdit())

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaEjercicio4()
    ventana.show()
    sys.exit(app.exec_())
