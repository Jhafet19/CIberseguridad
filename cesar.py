def cifrar(palabra,clave):
    
    abc = 'abcdefghijklmnñopqrstuvwxyz'
    aux=""
    for i in palabra:
        suma = abc.find(i)+clave
       
        modulo = int(suma) % len(abc)
        aux = aux + str(abc[modulo])
    
    print(aux)

var = input("Ingresa una palabra")
var2 = int(input("Ingrese una clave"))

cifrar(var,var2)
