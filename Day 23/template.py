
/* DAY 23: Network Programming with Sockets
 *
 * In this challenge, you'll create a simple client-server application using sockets.
 * 
 * **Server Code:**
 * 1. Import the `socket` and `threading` modules.
 * 2. Define a port number for the server (e.g., 5000).
 * 3. Create a server socket using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
 * 4. Bind the server socket to the specified port and IP address (e.g., ('', PORT)).
 * 5. Listen for client connections with `server_socket.listen()`.
 * 6. Create a loop to accept incoming client connections using `server_socket.accept()`.
 * 7. Handle each client connection in a separate thread using `threading.Thread`.
 * 8. In the client handling thread, receive data from the client using `client_socket.recv()`.
 * 9. Send a response back to the client using `client_socket.sendall()`.
 * 10. Close the client connection using `client_socket.close()`.
 *
 * **Client Code:**
 * 1. Import the `socket` module.
 * 2. Create a client socket using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
 * 3. Connect to the server using `client_socket.connect(('localhost', PORT))`.
 * 4. Send a message to the server using `client_socket.sendall()`.
 * 5. Receive a response from the server using `client_socket.recv()`.
 * 6. Print the received message.
 * 7. Close the client connection using `client_socket.close()`.
 *
 * **Sample Interaction:**
 * 1. Client sends: "Hello from the client!"
 * 2. Server receives: "Hello from the client!"
 * 3. Server sends: "Hello from server to client client!" 
 * 4. Client receives: "Hello from server to client client!"
 * 
 * LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>
 *
 **/

import socket
import threading

# Define port for server
PORT = 5000

# Function to run the server
def run_server():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the address and port
    server_socket.bind(('', PORT))
    # Listen for incoming connections
    server_socket.listen()

    # Accept client connections
    while True:
        # Accept a client connection
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
# Connect to the server
client_socket.connect(('localhost', PORT))

# Send message from client
client_socket.sendall("Hello from the client!".encode('utf-8'))

# Receive message from server
response = client_socket.recv(1024).decode('utf-8')

# Print received message
print(f"Received from server: {response}")

# Close client socket
client_socket.close()
