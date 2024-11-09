import hashlib

def cifrar(palabra, clave):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    aux = ""
    for i in palabra:
        suma = abc.find(i) + clave

        modulo = int(suma) % len(abc)
        aux = aux + str(abc[modulo])

    print(f"palabra encriptada {aux}")
    return aux

def desifrarCesar(palabraCifrada,clave):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    aux = ""
    for i in range(len(palabraCifrada)):
        for j in range(len(abc)):
            if palabraCifrada[i].lower() == abc[j]:
                aux += abc[(j-clave)%26]
    print(f"palabra desencriptada {aux}")
    return aux

def obterHashHexdigest(mensaje):
    text = hashlib.md5(mensaje.encode())
    return text.hexdigest()


def obterHash(mensaje):
    text = hashlib.md5(mensaje.encode())
    return text