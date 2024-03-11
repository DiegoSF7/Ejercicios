#Datos estaticos

categoria1 = 35;
categoria2 = 25;
categoria3 = 10;
categoria4 = 25;
categoria5 = 35;

precioAsiento = 20000;
counter = 0;


#Logica
def calcularPerdida():
    perdidaDinero = 0;
    ask = int(input("Ingrese la cantidad de individuos: "))
    while(ask < 0 ):
        ask = int(input("Ingrese una cantidad coherente por favor: "))
    print(f"Se ingresarán {ask} individuos...")
    for i in range(1,ask + 1):
        print("")
        print("-"*40)
        edad = int(input(f"Ingrese la edad del individuo {i}: "))
        while (edad < 0):
            edad = int(input("Ingrese una edad valida "))

        if(edad < 5):
            print("El individuo no puede acceder al teatro")
        else:
            if (edad >= 5 and edad <= 14):
                lost = categoria1/100 *precioAsiento
                print(f"El teatro perdería ${lost} pesos")
                perdidaDinero += lost

            elif (edad >= 15 and edad <= 19):
                lost = categoria2/100 *precioAsiento
                print(f"El teatro perdería ${lost} pesos")
                perdidaDinero += lost

            elif (edad >= 20 and edad <= 45):
                lost = categoria3/100 *precioAsiento
                print(f"El teatro perdería ${lost} pesos")
                perdidaDinero += lost

            elif (edad >= 46 and edad <= 65):
                lost = categoria4/100 *precioAsiento
                print(f"El teatro perdería ${lost} pesos")
                perdidaDinero += lost

            elif (edad >=66 ):
                lost = categoria5/100 *precioAsiento
                print(f"El teatro perdería ${lost} pesos")
                perdidaDinero += lost
    print("")
    print(f"-"*60)
    print(f"- El teatro perdio un total de: ${perdidaDinero} pesos")
    print(f"-"*60)

#Loop
while (counter == 0):
    calcularPerdida()
    op = int(input("Desea seguir con la operacion? \n [1] - Seguir   [0] - Salir \n"))
    while(op < 0 or op > 1):
        op = int(input("Ingrese un numero valido \n [1] - Seguir    [0] - Salir \n"))
    if(int(op) == 0):
        counter += 1
        print("Hasta luego!")

        