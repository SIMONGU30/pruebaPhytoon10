opcion=0
opcion2=0
senado=0
camara=0
consulta=0
pacto=0
centro=0
equipo=0

while(opcion!=4):
    print("*********MENU ********")
    print("1---> senado")
    print("2---> camara")
    print("3---> consulta")
    print("4---> salir")
    print("5---> mostrar votos")
    print("**********************************")

    opcion=int(input("digite una opcion "))

    if opcion==1:
        senado=senado+1
    elif opcion==2:
        camara=camara+1
    elif opcion==3:
        print("1.PACTO")
        print("2.CENTRO")
        print("3.EQUIPO")

        if opcion==1:
            pacto=pacto+1
        elif opcion==2:
            centro=centro+1
        elif opcion==3:
            equipo=equipo+1
        else:
            print("no digito numero correcto")

    elif opcion==5:
        print(f"senado : {senado}")
        print(f"camar : {camara}")
        print(f"consulta : {consulta}")
        print(f"pacto : {pacto}")
        print(f" centro : {centro}")
        print(f"equipo : {equipo}")











    



