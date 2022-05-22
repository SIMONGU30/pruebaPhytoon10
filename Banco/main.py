from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta


opcion=1

print("********* BANCOLOMBIA *********")
print("1---> Reagistrar Cliente")
print("2---> salir ")
print("**********************************")


while(opcion!=0):
    opcion=int(input("digita una opcion: "))

    if(opcion==1):
        nombre=input("Digite el nombre del usuaroi")
        apellido=input("Digite el apellido del usuaroi")
        cedula=input("Digite el cedula del usuaroi")
        saldoInicial=0
        numeroCuenta=input("Digite el numero: ")


        cuenta=Cuenta(numeroCuenta,saldoInicial)
        cliente=Cliente(nombre,apellido,cedula,cuenta)