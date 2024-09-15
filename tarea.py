import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QInputDialog
from PyQt5.QtCore import Qt

def mostrar_info():
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = QWidget()
    ventana.setWindowTitle('Información Personal')
    ventana.resize(300, 150)  # Tamaño adecuado para mostrar la info

    # Solicitar el nombre completo
    nombre_completo, ok = QInputDialog.getText(ventana, "Nombre Completo", "Introduce tu nombre completo:")
    if not ok or not nombre_completo:
        nombre_completo = "No proporcionado"  # Valor por defecto si no se proporciona

    # Solicitar la edad
    edad, ok = QInputDialog.getText(ventana, "Edad", "Introduce tu edad:")
    if not ok or not edad:
        edad = "No proporcionada"  # Valor por defecto si no se proporciona

    # Crear etiquetas para el nombre y la edad
    label_nombre = QLabel(f"Nombre: {nombre_completo}")  # Nombre proporcionado por el usuario
    label_edad = QLabel(f"Edad: {edad}")  # Edad proporcionada por el usuario

    # Estilo de texto
    label_nombre.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")  # Nombre más grande, negrita y centrado
    label_edad.setStyleSheet("font-size: 16px; text-align: center;")  # Edad un poco más grande y centrado

    # Diseño vertical
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)  # Centra el contenido verticalmente
    layout.setSpacing(10)  # Espacio entre etiquetas

    layout.addWidget(label_nombre)
    layout.addWidget(label_edad)
    ventana.setLayout(layout)

    # Mostrar ventana
    ventana.show()

    sys.exit(app.exec_())  

if __name__ == "__main__":
    mostrar_info()
