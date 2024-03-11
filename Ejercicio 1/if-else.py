#Datos estaticos

categoria1 = 35;
categoria2 = 25;
categoria3 = 10;
categoria4 = 25;
categoria5 = 35;

precioAsiento = 10000;

#Programa

edad = int(input("Ingrese la edad del individuo: "))

if(edad < 5):

    print("El individuo no puede acceder al teatro")

else:
    if (edad >= 5 and edad <= 14):
        print(f"El teatro perdería ${categoria1/100 *precioAsiento} pesos")

    if (edad >= 15 and edad <= 19):
        print(f"El teatro perdería ${categoria2/100 *precioAsiento} pesos")

    if (edad >= 20 and edad <= 45):
        print(f"El teatro perdería ${categoria3/100 *precioAsiento} pesos")

    if (edad >= 46 and edad <= 65):
        print(f"El teatro perdería ${categoria4/100 *precioAsiento} pesos")

    if (edad >=66 ):
        print(f"El teatro perdería ${categoria5/100 *precioAsiento} pesos")
