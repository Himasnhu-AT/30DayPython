
import socket
import threading

# Define port for server
PORT = 5000

# Function to run the server
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen()

    # Accept client connections
    while True:
        client_socket, address = server_socket.accept()
        # Handle client connection in a new thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# Function to handle a client connection
def handle_client(client_socket, address):
    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    # Send response to client
    client_socket.sendall(f"Hello from server to client {data.split()[2]}".encode('utf-8'))
    # Close client connection
    client_socket.close()

# Create a thread to run the server
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', PORT))

# Send message from client
client_socket.sendall("Hello from the client!".encode('utf-8'))

# Receive message from server
response = client_socket.recv(1024).decode('utf-8')

# Print received message
print(f"Received from server: {response}")

# Close client socket
client_socket.close()

