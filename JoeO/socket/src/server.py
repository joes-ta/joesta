import socket

# 1. Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to an address and port
# 'localhost' means this computer; 12345 is an arbitrary port
server_socket.bind(('localhost', 12345))

# 3. Start listening (max 1 connection in queue)
server_socket.listen(1)
print("Server is waiting for a connection...")

# 4. Accept a connection
connection, address = server_socket.accept()
print(f"Connected to: {address}")

# 5. Receive data (up to 1024 bytes) and decode from bytes to string
data = connection.recv(1024).decode()
print(f"Client says: {data}")

# 6. Close the connection
connection.close()
server_socket.close()