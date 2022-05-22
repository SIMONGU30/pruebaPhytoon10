# for tradicional en pyhton

#for contador  in range(10,21,5):
    #print(contador)

programadores=[]

contador=0

tamaño=int(input("digite el tamaño de la lista"))


for i in range(1,tamaño+1):

    numerosUsuario=int(input("digite el numero "))
    contador+=numerosUsuario
    
    programadores.append(contador)
print(programadores)