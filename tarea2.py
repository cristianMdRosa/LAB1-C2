from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.contra()
    
    def contra(self):
        self.setWindowTitle('Ingresar Contraseña')
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()

        # se crea y agrega el qlabel para darle una diferenciacion del cuadro de texto
        self.label = QLabel('Ingresar contraseña:')
        layout.addWidget(self.label)

        # Crear y agregar el QLineEdit para poder ingresar la contraseña en el campo asignado
        self.input = QLineEdit()
        self.input.setEchoMode(QLineEdit.Password)  # esta linea sirve para poder ocultar la contraseña que se va a escribir
        layout.addWidget(self.input)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec_()
