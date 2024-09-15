from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget
import sys

class VentanaEjercicio5(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Ejercicio 5")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()
        datos = ["Nombre", "Apellido", "Edad", "Dirección", "Teléfono", "Correo Electrónico",
                 "Fecha de Nacimiento", "País", "Ciudad", "Ocupación"]

        for dato in datos:
            layout.addWidget(QLabel(dato + ":"))
            layout.addWidget(QLineEdit())

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaEjercicio5()
    ventana.show()
    sys.exit(app.exec_())
