    #1.- Lista el nombre de todos los campeones.
    #2.- Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).
    #3.- Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.
    #4.- Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una vida igual o superior.
    #5.- Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).


def listado(datos):
    lista = []
    for i in range(0,23):
        lista.append(datos["Campeones"]["Champion"][i]["name"])
    return lista

def contar():


import json

with open("leagueoflegends.json","r") as fichero:
    datos = json.load(fichero)
    
print("\n1.- Lista el nombre de todos los campeones.\n")
print(listado(datos))  

print("\n2.- Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).\n")
