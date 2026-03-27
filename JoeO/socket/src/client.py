import socket

# 1. Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server's address and port
client_socket.connect(('localhost', 12345))

# 3. Send a message (must be encoded to bytes)
message = "Hello from the Client!"
client_socket.send(message.encode())

# 4. Close the socket
client_socket.close()