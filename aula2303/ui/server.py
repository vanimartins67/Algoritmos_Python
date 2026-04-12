import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen()

print("Servidor rodando...")

conn, addr = server.accept()
print(f"Conectado com {addr}")

while True:
    try:
        msg = conn.recv(1024).decode()
        if msg:
            print(f"Cliente: {msg}")
    except:
        break

conn.close()
server.close()