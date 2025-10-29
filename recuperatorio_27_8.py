#1.Cargar vehiculo

def carga_de_datos(matriz:list):

    patente = input("Ingrese la patente del vehiculo")
    marca = input("Ingrese la marca del vehiculo")
    modelo = input("Ingrese el modelo del vehiculo")
    año = int(input("Ingrese el año del vehiculo"))
    cant_horas_estacionado = int(input("Ingrese la cantidad de horas estacionado"))

    datos_vehiculo = [patente, marca, modelo, año, cant_horas_estacionado]


    return datos_vehiculo


#2.Mostrar lista completa
def mostrar_lista(matriz):
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    
    else:  
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                datos =  ("Patente:", matriz[i][0]
                        , "Marca: ", matriz[i][1]
                        ," Modelo: ", matriz[i][2]
                        , "Año:", matriz[i][3]
                        , "Cantidad de horas estacionado: ", matriz[i][4] )
                return datos


#3.Buscar vehiculo por patente
def buscar_vehiculo(matriz, patente):
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                if matriz[i][0] == patente:
                    datos = ( "Se encontro la patente" 
                            ," Patente ", matriz[i][0]
                            , "Marca", matriz[i][1]
                            , "Modelo ", matriz[i][2]
                            , "Año ", matriz[i][3]
                            , "Cantidad de horas estacionado ", matriz[i][4])
                    return datos
                else: 
                    datos = "No se ha encontrado"
                    return datos


#4.Ordenar vehiculos por año(descendente)
def ordenar_vehiculo(matriz):
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        orden = 0
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                if matriz[i][3] > orden:
                    orden = matriz [i][3]
                    lista = []
                    lista =+ [orden]
                else:
                    pass

#5.Vehiculo con más horas estacionado
def vehiculo_mas_horas(matriz):
    horas = float("-inf")
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
            if matriz[i][4] > horas:
                ganador = matriz[i][4]
            return ganador

#6.Vehiculo con menos horas estacionado
def vehiculo_menos_horas(matriz):
    horas = float("inf")
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
            if matriz[i][4] < horas:
                ganador = matriz[i][4]
            return ganador

#7.Cantidad de vehiculos con màs de 4 horas estacionado
def cantidad_vehiculos_cuatro_horas(matriz):
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
            if matriz[i][4] > 4:
                print(matriz[i][4])
                cantidad =+ 1
                datos = (f"Los autos con +4 horas de estacionamiento son: {cantidad}")
                return datos

#8.Promedio de horas estacionadas
def promedio(matriz):
    acum = 0
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
                if matriz[i][4] != 0:
                    datos = matriz[i][4]
                    print(datos)
                    acum += datos

        promedio = acum / len(matriz)
        return promedio

    

#9.Cantidad de vehiculos de la marca "Ford"
def vehiculos_ford(matriz):
    cont = 0
    if len(matriz) == 0:
        datos = "Error, no hay datos guardados"
        return datos
    else:
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                if matriz[i][1] == "ford":
                    cont =+ 1
            return cont