import socket

HOST = '127.0.0.1'  # Dirección local
PORT = 65432        # Puerto no reservado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}...")

    
    conn, addr = servidor.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Cliente dice: {data.decode()}")
            conn.sendall(b"Mensaje recibido por el servidor")

