import random
import os

lista=[]
lista_marca=[]
lista_elementos_con_marca_nueva = []
lista_insumos_act=[]

def mostrar_menu(): #Menu del programa
    opcion=""
    print("****************** MENU *****************")
    print("1 - Cargar archivo") #Esta opción permite cargar el contenido del archivo "movies.csv" en una colección
    print("2 - Imprimir lista")
    print("3 - Asignar tiempos")
    print("4 - Filtrar por genero")
    print("5 - Mostar duraciones")# ASCENDENTE ante generos iguales, por duracion descendente.
    print("6 - Guardar peliculas")
    print("7 - Salir") 
    while True:
        opcion = input("Ingrese una opción para continuar: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 7:
            break
        else:
            print("Error: Ingrese nuevamente una opción válida (1 al 7).")
    return opcion

def mostrar_lista(lista:list):
    print("-------------------------------------------------------------------------")
    print(f'{"ID".ljust(5)} {"TITULO".ljust(25)} {"GENERO".ljust(25)} {"DURACION".ljust(5)}')
    print("-------------------------------------------------------------------------")
    for elemento in lista:
        id_peli = elemento["id_peli"]
        titulo = elemento["titulo"]
        genero = elemento["genero"]
        duracion = elemento["duracion"]
        print(f'{str(id_peli).ljust(5)} {str(titulo).ljust(25)} {str(genero).ljust(25)} {str(duracion).ljust(5)}')
    print("-------------------------------------------------------------------------")
    print("\n")

def asignar_tiempos(elemento):
    duracion = random.randint(100, 240)
    elemento["duracion"] = duracion #pisa el tiempo que trae del csv original
    return elemento

def mostrar_por_tipo(lista:list, key):
    tipo=input("ingrese genero/tipo: ")
    #validar ingreso de tipo
    validacion=0
    while validacion==0 or tipo == "":
        for elemento in lista:
            if str(tipo).lower() in str(elemento[key]).lower():
                validacion+=1
        if validacion==0 or tipo == "":
            tipo=input("Error! ingrese genero: ")
        else:
            break
    print("-------------------------------------------------------------------------")
    print(f'{"ID".ljust(5)} {"TITULO".ljust(25)} {"GENERO".ljust(25)} {"DURACION".ljust(5)}')
    print("-------------------------------------------------------------------------")

    directorio="recu_primer_parcial_labo"
    nombre_archivo = tipo
    nombre_archivo+=".csv"
    ruta=os.path.join(directorio, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as file:
        for elemento in lista:
            if str(tipo).lower() in str(elemento[key]).lower():
                with open(ruta, "a", encoding="utf-8") as file:
                    file.write(
                        f'{elemento["id_peli"]}{","}{elemento["titulo"]}{","}{elemento["genero"]}{","}{elemento["duracion"]}\n')
                id_peli = elemento["id_peli"]
                titulo = elemento["titulo"]
                genero = elemento["genero"]
                duracion = elemento["duracion"]
                print(f'{str(id_peli).ljust(5)} {str(titulo).ljust(25)} {str(genero).ljust(25)} {str(duracion).ljust(5)}')
    print("-------------------------------------------------------------------------")
    
def ordenar_listas_dict(lista: list, key: str, ascendente=True)->list:
    tamaño_lista = len(lista)
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]).isdigit():
                if (ascendente and float(lista[i][key]) > float(lista[j][key])) or (not ascendente and float(lista[i][key]) < float(lista[j][key])):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
            else:
                if (ascendente and lista[i][key] > lista[j][key]) or (not ascendente and lista[i][key] < lista[j][key]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]==lista[j][key] and lista[i]["duracion"]<lista[j]["duracion"]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    print("------------------------------------------------------------------------")
    print(f'{"ID".ljust(5)} {"TITULO".ljust(25)} {"GENERO".ljust(25)} {"DURACION".ljust(5)}')
    print("------------------------------------------------------------------------")

    for elemento in lista:
        id_peli = elemento["id_peli"]
        titulo = elemento["titulo"]
        genero = elemento["genero"]
        duracion = elemento["duracion"]
        print(f'{str(id_peli).ljust(5)} {str(titulo).ljust(25)} {str(genero).ljust(25)} {str(duracion).ljust(5)}')        
    print("------------------------------------------------------------------------")
    return lista

def guardar_peliculas_csv(lista):
    with open("recu_primer_parcial_labo\lista_ordenada.csv", "w") as file:
        while True:
            for elemento in lista:
                with open("recu_primer_parcial_labo\lista_ordenada.csv", "a", encoding="utf-8") as file:
                    file.write(
                        f'{elemento["id_peli"]}{","}{elemento["titulo"]}{","}{elemento["genero"]}{","}{elemento["duracion"]}\n')
            break
    print("---------------------------------------------------------------------------------------------")
    print("Se guardo un listado de las películas ordenadas por género Ascendente y duración descendente.")
    print("---------------------------------------------------------------------------------------------")
    