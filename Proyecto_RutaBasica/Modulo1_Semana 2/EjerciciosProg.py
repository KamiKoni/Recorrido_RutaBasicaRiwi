#Ejercicio Fizz Buzz
for i in range (1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")    
    if(i % 3 == 0):
        print("fizz")
    if(i % 5 == 0):
        print("buzz")    
    else:
        print(i)

#Clasificador de Numeros.
numeros = [1,-43,0,8,-2,-9,32,65,-34,0,-23,-12,42.1, 42.1, 32.1, 56.3,0]
num_positivos = list(filter(lambda  x : x > (0), numeros))
print(num_positivos)
num_negativos = list(filter(lambda  x : x < (0), numeros))
print(num_negativos)
num_cero = list(filter(lambda  x : x == (0), numeros))
print(num_cero)








