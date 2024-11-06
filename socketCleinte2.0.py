import socket
import hashlib
def ClienteScanner():



    while True:
        cliente_socket = socket.socket()
        cliente_socket.connect(('127.0.0.1', 5000))
        bandCifrado=False;
        if(bandCifrado==False):
            print("Escribe una clave para el servidor")
            mensaje = input()
            
            bandCifrado=True
            
        print("Escribe un mensaje para el servidor")
        mensaje = input()

        cliente_socket.send(mensaje.encode())
        text= hashlib.md5(mensaje.encode())
        cliente_socket.send(text.hexdigest().encode())

        serverMensaje = cliente_socket.recv(1024).decode()
        serverHash = cliente_socket.recv(1024).decode()

        hashLocalServer = hashlib.md5(serverMensaje.encode())
        
        print(f" Mensaje del servidor: {serverMensaje}")
        print(f" Mensaje del servidor: {serverHash}")
        print(f" Mensaje del servidor: {hashLocalServer.hexdigest()}")


ClienteScanner()
