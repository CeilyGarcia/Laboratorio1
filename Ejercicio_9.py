cantidad = int(input("Ingrese la cantidad a invertir: "))
interes = int(input("Ingrese el interes anual: "))
años = int(input("Ingrese el numero de años: "))
op1 = interes/100
op2 = op1*años
total = cantidad*op2
print("El capital total es: ",total)
