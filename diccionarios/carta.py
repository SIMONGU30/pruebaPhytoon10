#1 Menu Opciones
opcion=100

#ciclo

print("*********MENU A LA CARTA*********")
print("1---> Calcular la Suma")
print("2---> Calcular la Resta")
print("3---> Calcular la Multiplicacion")
print("4---> Calcular la Division")
print("0---> Calcular la Division")
print("**********************************")

while(opcion!=0):
    opcion=int(input("Digita una opcion : "))
    if(opcion==1):
        numero1=int(input("Digita un numero : "))
        numero2=int(input("Digita otro numero : "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')
    elif(opcion==2):
        numero1=int(input("Digita un numero : "))
        numero2=int(input("Digita otro numero : "))
        print(f'{numero1}-{numero2}={(numero1-numero2)}')
    elif(opcion==3):
        numero1=int(input("Digita un numero : "))
        numero2=int(input("Digita otro numero : "))
        print(f'{numero1}*{numero2}={(numero1*numero2)}')
    elif(opcion==4):
        numero1=int(input("Digita un numero : "))
        numero2=int(input("Digita otro numero : "))
        print(f'{numero1}/{numero2}={(numero1/numero2)}')
    else:
        print("Digita una Opcion valida")