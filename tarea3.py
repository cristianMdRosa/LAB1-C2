import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QVBoxLayout, QLabel

def obtener_datos():
    app = QApplication(sys.argv)

    # Crear ventana
    ventana = QWidget()
    ventana.setWindowTitle('Datos Personales')
    layout = QVBoxLayout()

    # Pedir número de DUI
    dui, ok = QInputDialog.getText(ventana, "DUI", "Introduce tu número de DUI:")
    if ok and dui:
        label_dui = QLabel(f"DUI: {dui}")
        layout.addWidget(label_dui)

    # Pedir nombre completo
    nombre_completo, ok = QInputDialog.getText(ventana, "Nombre Completo", "Introduce tu nombre completo:")
    if ok and nombre_completo:
        label_nombre = QLabel(f"Nombre: {nombre_completo}")
        layout.addWidget(label_nombre)

    # Configurar y mostrar la ventana con los datos
    ventana.setLayout(layout)
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    obtener_datos()
