import socket
import hashlib
import  seguridad as sg


def ClienteScanner():
    bandCifrado = False
    clave = 0
    while True:
        cliente_socket = socket.socket()
        cliente_socket.connect(('127.0.0.1', 5000))


        if(bandCifrado==False):
            print("Escribe una clave para el servidor")
            clave =  input()

        print("Escribe un mensaje para el servidor")
        mensaje = input()
        claveInt = int(clave)
        mensaje = sg.cifrar(mensaje,claveInt)
        if(bandCifrado==False):
            cliente_socket.send(clave.encode())
            bandCifrado = True
        cliente_socket.send(mensaje.encode())
        text = sg.obterHashHexdigest(mensaje)
        cliente_socket.send(text.encode())

        serverMensaje = cliente_socket.recv(1024).decode()
        serverHash = cliente_socket.recv(1024).decode()

        hashLocalServer = sg.obterHashHexdigest(serverMensaje)

        print(f" Mensaje del servidor: {serverMensaje}")
        print(f" MensajeHash local del servidor: {hashLocalServer}")
        print(f" Mensaje hash enviado por servidor: {serverHash}")


ClienteScanner()
