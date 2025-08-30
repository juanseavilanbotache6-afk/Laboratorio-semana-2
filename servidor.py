import socket #cliente-servidor

HOST = '127.0.0.1'  # Dirección local
PORT = 65432        # Puerto no reservado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen() #esperando que un cliente intente conectarse
    print(f"Servidor escuchando en {HOST}:{PORT}...")
    # socket.AF_INET-indica que se usará IPv4
    # socket.SOCK_STREAM-el socket usará TCP (conexión confiable)
    
    conn, addr = servidor.accept() #addr contiene la dirección IP y puerto del cliente que se conectó
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Cliente dice: {data.decode()}")
            conn.sendall(b"Mensaje recibido por el servidor")

