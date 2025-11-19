while True:
    # with open(f"fruits.txt","w") as file:
    #     for i in range(1,6):
    #         num = input("Ingrese una fruta: ")
    #         file.write(f'{num} \n')
    palabra = input("Ingresa la fruta que deseas buscar: ")
    with open(f"fruits.txt","r") as file:
            i = file.readlines()
            print(len(i))
            for linea in i:
                if palabra in linea:
                    print(linea, end= "")
    break
