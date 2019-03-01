p=0

for m in range(0,99999999999999999999999999999999999999999999999999999999999999999):
    m=int(input("ingrese un numero"))

    if m%2==0:
        p = p + 1
    else:
        break

    print("El CMD Se Detuvp PorQue Ingreso Un Numero Impar \n y La Cantidad De Pares Fueron: ",p)
