import hashlib

def cifrar(palabra, clave):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    aux = ""
    for i in palabra:
        suma = abc.find(i) + clave

        modulo = int(suma) % len(abc)
        aux = aux + str(abc[modulo])

    print(aux)
    return aux

def desifrarCesar(palabraCifrada,clave):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    aux = ""
    for i in range(len(palabraCifrada)):
        for j in range(len(abc)):
            if palabraCifrada[i].lower() == abc[j]:
                aux += abc[(j-clave)%26]

    return aux

def obterHash():

