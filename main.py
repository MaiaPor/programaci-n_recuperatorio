from recuperatorio_27_8 import *
#Inicializamos el menù

bandera = True

while bandera:
    print("··· Estacionamiento Patos Center ···")
    print("1. Cargar vehiculo")
    print("2. Mostrar lista completa")
    print("3. Buscar vehiculo por patente")
    print("4. Ordenar vehiculo por año")
    print("5. Vehiculo con mas horas estacionado")
    print("6. Vehiculo con menos horas estacionado")
    print("7. Cantidad de vehiculos con mas de 4 horas estacionado")
    print("8. Promedio de horas estacionadas")
    print("9. Cantidad e vehiculos de la marca Ford")
    print("0. Salir del menú")

    eleccion = int(input("Seleccione la opción"))

    if eleccion == 0:
        bandera = False
    elif eleccion == 1:
        carga_de_datos()
