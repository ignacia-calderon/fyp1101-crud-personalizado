import os # permite limpiar la pantalla segun el sistema operativo 
pokedex = [] # lista principal donde guardare todo los pokemos que se registren 
nombre = "" # variable de texto para ingresar un nombre 
tipo = ""   # variable de texto para ingresar un tipo de pokemon
nivel = 0   #variable para el niver tipo entero
poder = 0  #variable para el poder tipo entero
opcion = "" #variable de texto para selecionar el menu 
def registrar_pokemon(nombre, tipo, nivel, poder): # esta linea de codigo nos sirve para crear un diccionario con los datos del pokemon 
    pokemon = {"nombre": nombre, "tipo": tipo, "nivel": nivel, "poder": poder}
    pokedex.append(pokemon) # agrega pokemon a la lista gracias al .append
    print(f"pokemon '{nombre}' agregado correctamente.") # mensaje de confirmacion 
def mostrar_pokedex():
    if len(pokedex) == 0:  #valida si la lista esta vacia
        print("\nLa Pokédex está vacía.")
        return # return nos ayuda a salir de la funcion
    print("\n======= POKÉDEX =======") # agregue el titulo para que se vea bonito 
    for pokemon in pokedex: # gracias al for recorremos la lista de pokemon
        print("-----------------------")
        print("Nombre:", pokemon["nombre"])  #aqui nos muestra el nombre 
        print("Tipo:", pokemon["tipo"])  # aqui nos muestra el tipo
        print("Nivel:", pokemon["nivel"]) # aqui nos muestra el nivel 
        print("Poder:", pokemon["poder"])  # aqui nos muestra el poder 
    print("-----------------------")
    print("Poder total:", calcular_poder()) # nos muestra la suma total
def calcular_poder():
    total = 0  # acumulador 
    for pokemon in pokedex: # aqui recorremos los pokemones 
        total = total + pokemon["poder"] # aqui sumamos el poder 
    return total  # gracias al return nos devuelve el total 
def actualizar_pokemon(nombre):
    for pokemon in pokedex:   # gracias al for buscamos el pokemon 
        if pokemon["nombre"].lower() == nombre.lower():  #aki comparamos sin mayuscula para que no se caiga el sistema al escribir mal
            nuevo_tipo = input("nuevo tipo: ") #aka le pide al usuario un nuevo tipo
            if nuevo_tipo == "": #aki validamos el vacio 
                print("tipo vacío.")
                return #con return salimos 
            try:
                nuevo_nivel = int(input("nuevo nivel: ")) #pide nivel en int numero entero positivo
                nuevo_poder = int(input("nuevo poder: ")) #pide poder en int numero entero positivo
                if nuevo_nivel < 0 or nuevo_poder < 0: # valida si coloca numero negativo
                    print("nivel y poder deben ser positivos")
                    return # aqui salimos 
            except ValueError: # error de numero por si ingresa un numero mal
                print("debe ingresar numeros.")
                return  #lo volvemos a usar para salir 
            pokemon["tipo"] = nuevo_tipo  #actualiza el tipo
            pokemon["nivel"] = nuevo_nivel #actualiza el nivel
            pokemon["poder"] = nuevo_poder # actualiza el poder 
            print("pokemon actualizado.") #nos da un mensaje de actualizado
            return #termina la funcion
    print("pokemon no encontrado.") #entrega un mensaje por si no existe el pokemon
def eliminar_pokemon(nombre):
    for pokemon in pokedex:  #volvemos a recorrer la lista 
        if pokemon["nombre"].lower() == nombre.lower(): # busca coincidencia 
            pokedex.remove(pokemon) # con remove eliminamos al pokemon
            print("pokemon eliminado.") #si fue con exito entregamos un mensaje 
            return #termina la funcion
    print("pokemon no encontrado.") # entregamos un mensaje si no se encuentra 
def existe(nombre):
    for pokemon in pokedex:  # volvemos a recorrer la lista 
        if pokemon["nombre"].lower() == nombre.lower(): #comparamos los nombres
            return True # con return true verificamos que ya existe
    return False # aqui es al reves 
while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("======POKEDEX======")
    print("1.- Registrar Pokemon")
    print("2.- Mostrar Pokedex")
    print("3.- Modificar Pokemon")
    print("4.- Eliminar Pokemon")
    print("5.- Salir")

    opcion = input("seleccione una opcion: ") #lee la opcion 
    if opcion == "1":
        nombre = input("nombre: ")
        if nombre == "":
            print("nombre vacío")
        elif not nombre.isalpha(): # Valida que el nombre solo tenga letras (permite espacios entre palabras)
            print("solo letras en el nombre")
        else:
            tipo = input("tipo: ")
            if tipo == "":
                print("tipo vacío")
            elif not tipo.replace(" ", "").isalpha():
                print("solo letras en el tipo")
            else:
                nivel = input("nivel: ")
                poder = input("poder: ")
                if not nivel.isdigit() or not poder.isdigit():
                    print("nivel y poder deben ser numeros")
                else:
                    nivel = int(nivel)
                    poder = int(poder)
                    if nivel < 0 or poder < 0:
                        print("no se permiten negativos")
                    elif existe(nombre):
                        print("ya existe ese pokemon")
                    else:
                        registrar_pokemon(nombre, tipo.lower(), nivel, poder)
        input("\nEnter para continuar...")
    elif opcion == "2":
        mostrar_pokedex()
        input("\nEnter para continuar...")
    elif opcion == "3":
        nombre = input("nombre del pokemon: ") # pide nombre 
        if nombre == "":
            print("nombre vacío.")
        else:
            actualizar_pokemon(nombre) #actualiza 
        input("\nEnter para continuar...")
    elif opcion == "4":
        nombre = input("nombre del pokemon: ")
        if nombre == "":
            print("nombre vacío.")
        else:
            eliminar_pokemon(nombre) # elimina el pokemon
        input("\nEnter para continuar...")
    elif opcion == "5":
        print("programa finalizado.")
        break
    else:
        print("opcion invalida.")
        input("\nEnter para continuar...")