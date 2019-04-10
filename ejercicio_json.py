import json

#1.- Lista el nombre de todos los campeones.
def listado(datos):
    lista = []
    for i in range(0,23):
        lista.append(datos["Campeones"]["Champion"][i]["name"])
    return lista

#2.- Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).
def contar_tipos(datos,tipo):
    listar_tipos = []
    for tipos in range(0,23):
        lista_cont_campeones = []
        if str(datos["Campeones"]["Champion"][tipos]["tags"]).find(tipo) != -1:
            listar_tipos.append(datos["Campeones"]["Champion"][tipos]["tags"] == tipo)
    return len(listar_tipos)
        
#3.- Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.
def filtro_descripcion(datos,clave):
    lista = []
    for i in range(0,23):
        if str(datos["Campeones"]["Champion"][i]["description"]).find(clave) != -1:
            lista.append(datos["Campeones"]["Champion"][i]["description"])
            
    cad = "Palabra clave :" + clave + "\n"
    for i in lista:
        cad = cad + "\n\n" + i
    return cad

#4.- Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una vida igual o superior.

#5.- Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).
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
tipo=str(input("\n¿Que tipo de campeon deseas contar?: "))
tipo=tipo.lower()
print(contar_tipos(datos,tipo))
        
print("\n3.- Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.\n")
clave=str(input("\n¿Que palabras buscas en la descripción?: "))
print(filtro_descripcion(datos,clave))

print("\n4.- Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una vida igual o superior.\n")

print("\n5.- Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).\n")
#print('''\n\n	Elige una de las siguientes opciones:				
#1. Lista los nombres de todos los campeones.
#2. Contar los campeones que sean magos/tanques/luchadores(Lo que pidas por teclado).
#3. Buscar(Palabra escrita por teclado)que se encuentre en la descripcion.
#4. Pedir la vida base(hp) de los campeones por teclado y mostrar a los campeones que una #vida igual o superior.
#5. Compara algun stat(pedido por teclado) entre dos campeones (pedidos por teclado).
#			''')
#opcion=str(input("Elige una opcion: "))

