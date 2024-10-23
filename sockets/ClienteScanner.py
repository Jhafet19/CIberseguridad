import socket
def ClienteScanner():



    while True:
        cliente_socket = socket.socket()
        cliente_socket.connect(('127.0.0.1', 5000))
        print("Escribe un mensaje para el servidor")
        mensaje = input()

        cliente_socket.send(mensaje.encode())

        serverMensaje = cliente_socket.recv(1024).decode()
        print(f" Mensaje del servidor: {serverMensaje}")



ClienteScanner()
