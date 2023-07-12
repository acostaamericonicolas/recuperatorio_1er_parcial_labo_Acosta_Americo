from funciones_parcial1 import *
import os
import sys

lista_elementos_con_marca_nueva = []
lista_insumos_act=[]
lista_elementos = []
while True:
    os.system("cls")  # limpia el terminal de ejecuc
    opcion = mostrar_menu()  # importo el menu desde el archivo menu.py
    if opcion == "1":
        # abro el archivo insumos.csv, lo recorro y convierto en lista de # diccionarios
        archivo = input("ingrese archivo a cargar (movies.csv): ")
        while archivo != "movies.csv":
            archivo = input("Error!!! ingrese archivo a cargar (movies.csv): ")
        with open("recu_primer_parcial_labo\movies.csv", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                lista_elementos.append({"id_peli": elemento[0], "titulo": elemento[1],
                                        "genero": elemento[2], "duracion": elemento[3]})
            print("-------------------------------------------------------------------------")
            print('                    Se genero una lista de peliculas')
            print("-------------------------------------------------------------------------")

    elif opcion == "2":
        motrar = mostrar_lista(lista_elementos)
    elif opcion == "3":
        lista_elementos_duracion_random = list(map(asignar_tiempos, lista_elementos))
        mostrar_lista(lista_elementos_duracion_random)
    elif opcion == "4":  # hacer compras
        mostrar = mostrar_por_tipo(lista_elementos, "genero")
    elif opcion == "5":
        mostrar_genero = ordenar_listas_dict(lista_elementos, "genero", True)
    elif opcion == "6":
        lista_ordenada = mostrar_genero
        if len(lista_ordenada) != 0:
            guardar_peliculas_csv(lista_ordenada)
        else:
            print("Ingrese opcion 5 primero")
            os.system("cls")  # limpia el terminal de ejecuc
            opcion = mostrar_menu()  # importo el menu desde el archivo menu.py
    elif opcion == "7":  # salir
        salida = input("Confirma salida?: s/n: ")
        if salida == "s" or "S":
            print("-----------SALISTE----------") 
            break
    os.system("pause")  # pausa el sistema para ver los resultados
