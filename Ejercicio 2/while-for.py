
mesesDiezAños = 120
mesesSieteAños = 84

# Valor de la casa
casa = 400000




def calcular():
    sueldo = int(input("Ingrese su sueldo: "))
    if (sueldo >= 80000):
        pie = 15 / 100
        pagarPie = pie * casa #Costo del pie
        resto = casa - pagarPie
        pagarMensual = resto / mesesDiezAños
        print("")
        print("##################################################")
        print("")
        print(f"El pie de casa sera de ${int(pagarPie)}")
        print(f"Mensualmente tendra que pagar ${int(pagarMensual)}")
        print("")
        print("##################################################")
        print("")

    else:
        pie = 30 / 100
        pagarPie = pie * casa #Costo del pie
        resto = casa - pagarPie
        pagarMensual = resto / mesesSieteAños
        print("")
        print("##################################################")
        print("")
        print(f"El pie de casa sera de ${int(pagarPie)}")
        print(f"Mensualmente tendra que pagar ${int(pagarMensual)}")
        print("")
        print("##################################################")
        print("")


counter = 0
while (counter == 0):
    calcular()
    ask = int(input("Desea volver a calcular?\n [1] - Seguir    [2] - Salir"))
    while (ask < 1 or ask > 2):
        ask = int(input("Ingrese un numero valido\n [1] - Seguir    [2] - Salir"))
    if (ask == 2):
        counter += 1
        print("Hasta luego!")        