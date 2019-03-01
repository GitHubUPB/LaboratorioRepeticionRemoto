p=0
c=0
n=0

for x in range(0,10):
    x=int(input("Digite Un Numero"))
    if x==0:
        c=c+1

    else:
        if x<0:
            p= p+1
        else:
            n= n+1

print("La Cantidad Dee Ceros Es: ",c)
print("La Cantidad De positivos es: ", p)
print("La Cantidad De negativos es: ", n)
        
