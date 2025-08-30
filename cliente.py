import socket

HOST = '127.0.0.1'  # Dirección del servidor
PORT = 65432        # Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    cliente.sendall(b"Hola servidor, soy el cliente!")
    data = cliente.recv(1024)

print(f"Servidor responde: {data.decode()}")
