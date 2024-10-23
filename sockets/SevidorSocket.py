import socket
from time import sleep


def servidor():

    while True:
        servidor_socket = socket.socket()
        servidor_socket.bind(('0.0.0.0', 5000))
        servidor_socket.listen(1)

        cliente_socket, direccion = servidor_socket.accept()

        mensaje = cliente_socket.recv(1024).decode()
        if(mensaje == ""):
            print("Mensaje vacío")
        else:
            print(f"Mensaje del cliente: {mensaje}")


        respuesta= input()
        cliente_socket.send(respuesta.encode())

        



servidor()
