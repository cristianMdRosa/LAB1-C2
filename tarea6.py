import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

def obtener_datos_empleado():
    app = QApplication(sys.argv)

    # Crear la ventana principal
    ventana = QWidget()
    ventana.setWindowTitle('Registro de Empleado')
    ventana.resize(400, 250)  # Ajusté el tamaño para incluir el nuevo campo

    # Crear el diseño vertical
    layout = QVBoxLayout()

    # Pedir ID del empleado
    empleado_id, ok = QInputDialog.getText(ventana, "ID del Empleado", "Introduce el ID del empleado:")
    if ok and empleado_id:
        label_id = QLabel(f"ID: {empleado_id}")
        layout.addWidget(label_id)

    # Pedir nombre completo
    nombre_completo, ok = QInputDialog.getText(ventana, "Nombre Completo", "Introduce el nombre completo:")
    if ok and nombre_completo:
        label_nombre = QLabel(f"Nombre: {nombre_completo}")
        layout.addWidget(label_nombre)

    # Pedir país
    pais, ok = QInputDialog.getText(ventana, "País", "Introduce el país:")
    if ok and pais:
        label_pais = QLabel(f"País: {pais}")
        layout.addWidget(label_pais)

    # Pedir departamento
    departamento, ok = QInputDialog.getText(ventana, "Departamento", "Introduce el departamento:")
    if ok and departamento:
        label_departamento = QLabel(f"Departamento: {departamento}")
        layout.addWidget(label_departamento)

    # Crear botón para mostrar los datos
    boton_mostrar = QPushButton("Mostrar Datos")
    layout.addWidget(boton_mostrar)

    # Función para mostrar los datos en una nueva ventana
    def mostrar_datos():
        ventana_datos = QWidget()
        ventana_datos.setWindowTitle('Datos del Empleado')
        ventana_datos.resize(300, 250)  # Ajusté el tamaño para incluir todos los campos

        layout_datos = QVBoxLayout()
        layout_datos.addWidget(QLabel(f"ID: {empleado_id}"))
        layout_datos.addWidget(QLabel(f"Nombre: {nombre_completo}"))
        layout_datos.addWidget(QLabel(f"País: {pais}"))
        layout_datos.addWidget(QLabel(f"Departamento: {departamento}"))

        ventana_datos.setLayout(layout_datos)
        ventana_datos.show()

    boton_mostrar.clicked.connect(mostrar_datos)

    # Configurar y mostrar la ventana principal
    ventana.setLayout(layout)
    ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    obtener_datos_empleado()
