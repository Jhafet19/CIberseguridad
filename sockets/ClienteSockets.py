import socket

def cliente():
    
    cliente_socket = socket.socket()
    
    
    cliente_socket.connect(('127.0.0.1', 5000))  # IP y puerto del servidor

    
    mensaje = "Hola desde el cliente!Buenas noches "
    cliente_socket.send(mensaje.encode())

    
    cliente_socket.close()

cliente()
