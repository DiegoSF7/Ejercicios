sueldo = int(input("Ingrese su sueldo: "))
casa = 400000
mesesDiezAños = 120
mesesSieteAños = 84

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