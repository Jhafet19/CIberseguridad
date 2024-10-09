import socket
def ClienteScanner():
    cliente_socket=socket.socket();

    cliente_socket.connect(('127.0.0.1',5000))
    print("Escribe un mensaje para el servidor")
    mensaje = input()

    cliente_socket.send(mensaje.encode())

    cliente_socket.close()

ClienteScanner();
