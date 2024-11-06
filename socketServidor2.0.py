import socket
import hashlib
from time import sleep


def servidor():

    while True:
        servidor_socket = socket.socket()
        servidor_socket.bind(('0.0.0.0', 5000))
        servidor_socket.listen(1)

        cliente_socket, direccion = servidor_socket.accept()
        

        mensaje = cliente_socket.recv(1024).decode()
        mensajeHash = cliente_socket.recv(1024).decode()
        if(mensaje == ""):
            print("Mensaje vacío")
        else:
            text= hashlib.md5(mensaje.encode())
            print(f"HAsh desde el server {text}")
            if(text.hexdigest() != mensajeHash):
                print("mensaje corrupto Cerraremos el servidor")
                servidor_socket.close()
                return "";
            
        print(f"Mensaje del cliente: {mensaje}")
                
                
            

        print("Envia un mensaje al cliente")
        respuesta= input()
        cliente_socket.send(respuesta.encode())
        text= hashlib.md5(respuesta.encode())
        cliente_socket.send(text.hexdigest().encode())

        



servidor()
