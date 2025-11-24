import socket

HOST = '127.0.0.1'   # loopback (local machine)
PORT = 5000          # any free port > 1024

# 1. Create socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind socket to address and port
server_socket.bind((HOST, PORT))

# 3. Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT} ...")

# 4. Accept a connection (blocks until client connects)
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

# 5. Receive data from client
data = conn.recv(1024)  # up to 1024 bytes
print("Received from client:", data.decode())

# 6. Send reply to client
reply = "Hello client, message received!"
conn.sendall(reply.encode())

# 7. Close connection
conn.close()
server_socket.close()
print("Server closed.")
