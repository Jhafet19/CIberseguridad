conta="hola"
conta2 = input("Escribe la contraseña")
if conta.lower()==conta2.lower():
    print("La contraseña si coincide")
else:
    print("La contraseña no coincide")

frase= input("Escribe una frase")

letra= input("Escribe una letra para buscar en esa frase")

cont=0
for i in frase:
    if(letra.lower()==i.lower()):
        cont+=1
print(f"la letra aparece {cont} veces")

pin="contra"
for i in range(3):
    var= input("Escribe el pin")
    if(var==pin):
        print("login correcto")
        break
    elif(i == 2):
        print("llamando al policía")
    
