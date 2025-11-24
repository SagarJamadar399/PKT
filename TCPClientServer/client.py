import socket

SERVER_IP = '127.0.0.1'   # same machine as server
SERVER_PORT = 5000

# 1. Create socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to server (this triggers TCP 3-way handshake)
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")

# 3. Send data to server
message = "Hello server, this is client!"
client_socket.sendall(message.encode())

# 4. Receive reply
data = client_socket.recv(1024)
print("Received from server:", data.decode())

# 5. Close connection
client_socket.close()
print("Client closed.")
