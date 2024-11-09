import socket
import hashlib
import  seguridad as sg
from time import sleep

def servidor():
    bandCifrado = False
    clave = ""
    claveInt =0
    while True:
        servidor_socket = socket.socket()
        servidor_socket.bind(('0.0.0.0', 5000))
        servidor_socket.listen(1)

        cliente_socket, direccion = servidor_socket.accept()

        if (bandCifrado == False):
            clave = cliente_socket.recv(1024).decode()
            bandCifrado = True
            claveInt = int(clave)
        mensaje = cliente_socket.recv(1024).decode()
        mensajeHash = cliente_socket.recv(1024).decode()
        if(mensaje == ""):
            print("Mensaje vacío")
        else:
            text =sg.obterHash(mensaje)
            print(f"Se ha establecido la clave {clave} para el cifrado")
            print(f"HAsh creado desde el local {text.hexdigest()}")
            print(f"Hash enviado por el cliente {mensajeHash}")
            if(text.hexdigest() != mensajeHash):
                print("mensaje corrupto Cerraremos el servidor")
                servidor_socket.close()
                return ""

        mensaje= sg.desifrarCesar(mensaje,claveInt)
        print(f"Mensaje del cliente: {mensaje}")
                
        print("Envia un mensaje al cliente")
        respuesta= input()
        cliente_socket.send(respuesta.encode())
        text = sg.obterHashHexdigest(respuesta)

        cliente_socket.send(text.encode())

servidor()
