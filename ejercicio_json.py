    #1.- Lista el nombre de todos los campeones.
    #2.- Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).
    #3.- Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.
    #4.- Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una vida igual o superior.
    #5.- Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).
    
import json

def listado(datos):
    lista = []
    for i in range(0,23):
        lista.append(datos["Campeones"]["Champion"][i]["name"])
    return lista


def contar_tipos(cad,datos):
    listatipos = []
    for Campeones in datos:
        for Champion in Campeones:
            if Champion["tags"].find(cad)!=-1:
                listatipos.append(Champion["name"])
    return len(listatipos)
        

with open("leagueoflegends.json","r") as fichero:
    datos = json.load(fichero)
    
print("\n1.- Lista el nombre de todos los campeones.\n")
print(listado(datos))  

print("\n2.- Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).\n")
print ('''Chuleta de tipos:
- Ranged     - Mage     - Assassin  - Melee
- Stealth    - Fighter  - Carry     - Recommended
- Jungler    - Tank     - Support   - Pusher
''')
cad=str(input("\n¿Que tipo de campeon deseas contar?: "))
cad=cad.lower()
print(contar_tipos(cad,datos))
        
#print('''\n\n	Elige una de las siguientes opciones:				
#1. Lista los nombres de todos los campeones.
#2. Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).
#3. Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.
#4. Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una #vida igual o superior.
#5. Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).
#			''')
#opcion=str(input("Elige una opcion: "))

