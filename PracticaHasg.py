import hashlib

def hashTextMD5(t):
    txtBytes = hashlib.md5(t.encode())
    return txtBytes.hexdigest()

res='SI'

while res !='NO' and 'N':
    texto = input("Ingresa un texto para calcular su hash: ")
    print("Hash MD5 del textp: ", hashTextMD5(texto))
    r = input("Desaea calcular otro hash:Si/No")
    res= r.upper();
