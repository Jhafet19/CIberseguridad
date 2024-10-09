import socket

def servidor():
    
    servidor_socket = socket.socket()
    
    
    servidor_socket.bind(('0.0.0.0', 5000))
    
    
    servidor_socket.listen(1)
    print("Esperando una conexión...")

    while True:
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Conectado a {direccion}")

        
        mensaje = cliente_socket.recv(1024).decode()
        print(f"Mensaje del cliente: {mensaje}")
        
        
        cliente_socket.close()


servidor()
