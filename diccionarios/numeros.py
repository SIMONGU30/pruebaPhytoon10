contador=0
sumatoria=0

while(contador<6):
    numero=int(input("Ingrese un numero: "))
    if(numero<0):
        sumatoria+=1
    contador+=1
print(f"la cantidad de negativos  fue : {sumatoria}")

