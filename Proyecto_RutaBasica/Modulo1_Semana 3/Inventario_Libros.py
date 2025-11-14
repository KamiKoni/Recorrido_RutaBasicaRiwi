from colorama import Fore, Back, Style, init
init(autoreset=True)
inventory = [
    {"title": "it", "price": 10.0, "quantity": 100},
    {"title": "the diary of anne frank", "price": 15.0, "quantity": 50},
    {"title": "the portrait of markov", "price": 20.0, "quantity": 30},
    {"title": "pride and prejudice", "price": 25.0, "quantity": 10},
    {"title": "frankenstein", "price": 30.0, "quantity": 5}
]
global Amount
Amount = 0
def agregar():
    Amount = int(input(Fore.BLUE("Cuantos libros quieres agregar al sistema: ")))
    while Amount != 0:
        try:
            title = input("Cual es el titulo del libro?: ")
            price = float(input("Cual es el precio del libro?: "))
            quantity = int(input("Cual es la cantidad del libro en stock?: "))
            Amount -= 1
        except ValueError:
            print(Fore.RED("ERROR, VALOR INGRESADO NO VALIDO"))
        if(inventory["price"] and inventory["quantity"] > 0):
            print(Fore.RED("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
        else:
            print(Fore.green("Libro introducido agregado al sistema exitosamente ✔"))
        book = {"title": title, "price": price, "quantity": quantity}
        book.append(inventory)
def consultar():
    busqueda = input(Fore.BLUE("Cual es el titulo del libro que buscas: "))
    for libro in inventory:
        if libro["title"].lower() == busqueda.lower():   # comparación sin mayúsc./minúsc.
            print(f"Titulo: {libro['title']} | Precio: {libro['price']} | Cantidad en stock: {libro['quantity']}")
            return
    else:
        print(Fore.RED("El libro que ingresaste no esta actualmente en el inventario"))
def Actualizar():
    busqueda = input(Fore.BLUE("Cual es el titulo del libro que actualizaras: "))
    for libro in inventory:
        if libro["title"].lower() == busqueda.lower():
            inventory["price"] = input(Fore.BLUE("Ingresa el precio nuevo de", libro ,": "))
            if(libro["price"] > 0):
                print(Fore.RED("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
            else:
                print(Fore.RED(Fore.GREEN("Libro actualizado exitosamente ✔")))
        else:
            print(Fore.RED("Libro no encontrado en el sistema (┬┬﹏┬┬)"))
def eliminar():
    busqueda = input(Fore.BLUE("Cual es el titulo del libro que actualizaras: "))
    for libro in inventory:
        if libro["title"].lower() == busqueda.lower():
            delete = input(Fore.BLUE(f'Estas seguro de que quieres eliminar del sistema a {libro} (Y,N): ')).lower().strip()
            if(delete == "y"):
                inventory.remove(libro)
def Calcular():
    total = sum(p["price"] * p["cantidad"] for p in inventory)
    print(f"El valor total del inventario es: {total:.2f}")
while True:
    try:
        option = int(input("""  
1. Agregar libros al inventario  
2. Consultar libros al inventario  
3. Actualizar precios del libro 
4. Eliminar libro del inventario
5. Calcular elvalor total del inventario  
6. Salir del programa  
Elige una opción: """))
    except ValueError:
        print(" ERROR: Debes ingresar un número.")
        continue

    if option == 1:
        agregar()
    elif option == 2:
        consultar()
    elif option == 3:
        Actualizar()
    elif option == 4:
        eliminar()
    elif option == 5:
        Calcular()
    elif option == 6:
        print("👋 Saliendo del programa...")
        break

    else:
        print(" Opción no válida. Intenta de nuevo.")











