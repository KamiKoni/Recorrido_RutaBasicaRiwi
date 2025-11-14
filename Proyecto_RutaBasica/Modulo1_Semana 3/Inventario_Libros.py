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
    book = []
    try:
        Amount = int(input(Fore.BLUE + "¿Cuántos libros quieres agregar al sistema?: "))
    except ValueError:
        print(Fore.RED + "ERROR: Valor ingresado no válido.")
        return
    while Amount != 0:
        try:
            title = input("Cual es el titulo del libro?: ")
            price = float(input("Cual es el precio del libro?: "))
            quantity = int(input("Cual es la cantidad del libro en stock?: "))
        except ValueError:
            print(Fore.RED + ("ERROR, VALOR INGRESADO NO VALIDO"))
            return
        if(price <= 0 and quantity <= 0):
            print(Fore.RED+("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
        else:
            print(Fore.GREEN+("Libro introducido agregado al sistema exitosamente ✔"))
            Amount -= 1
        book = {"title": title, "price": price, "quantity": quantity}
        return book
def consultar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que buscas: "))
    for book in inventory:
        if book["title"].lower() == busqueda.lower():   # comparación sin mayúsc./minúsc.
            print(f"Titulo: {book['title']} | Precio: {book['price']} | Cantidad en stock: {book['quantity']}")
            return
    else:
        print(Fore.RED + ("El libro que ingresaste no esta actualmente en el inventario"))
def Actualizar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que actualizaras: "))
    encontrado = False
    for book in inventory:
        if book["title"].lower() == busqueda.lower():
            encontrado = True
            try:
                nuevo_precio = float(input(Fore.BLUE+(f"Ingresa el precio nuevo de {book['title']}: ")))
            except ValueError:
                print(Fore.RED + ("ERROR, VALOR INGRESADO NO VALIDO"))
                return
            if(nuevo_precio <= 0):
                print(Fore.RED+("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
                return
            else:
                book["price"] = nuevo_precio
                print(Fore.GREEN+("Libro actualizado exitosamente ✔"))
        if not encontrado:
            print(Fore.RED+("Libro no encontrado en el sistema (┬┬﹏┬┬)"))
def eliminar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que actualizaras: "))
    for book in inventory:
        if book["title"].lower() == busqueda.lower():
            delete = input(Fore.BLUE+(f'Estas seguro de que quieres eliminar del sistema a {book} (Y,N): ')).lower().strip()
            if(delete == "y"):
                inventory.remove(book)
def Calcular():
    total = sum(p["price"] * p["quantity"] for p in inventory)
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
        print(Fore.RED + " ERROR: Debes ingresar un número.")
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











