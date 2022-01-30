from tokenize import Double


peso = int(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))
op1 = estatura**2
masa = peso/op1
n = round(masa,2)
print("Tu indice de masa corporal es: ", n)
