iva = 0.19
def impuesto(precio, IVA):
    precio = input("Cual es el precio del producto que vas a comprar: ")
    total = precio * IVA
    print("El precio total de tu producto sin impuestos es:", precio ,"| El precio con IVA incluido es: ", total)
numeros = [1, 6, 7 , 8, 3, 2, 6, 9, 2]
if not numeros:
    print("La lista esta vacia")
promedio = sum(numeros) / len(numeros)