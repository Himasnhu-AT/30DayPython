
import socket
import threading
import time

# Define port for server
PORT = 5000

# Define timeout for testing
TIMEOUT = 1

# Helper function to send data to a socket
def send_data(sock, data):
    sock.sendall(data.encode('utf-8'))

# Helper function to receive data from a socket
def receive_data(sock):
    data = sock.recv(1024).decode('utf-8')
    return data

# Test case 1: Basic server-client communication
def test_basic_communication():
    # Start server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))

    # Send message from client
    send_data(client_socket, "Hello from the client!")

    # Receive message from server
    response = receive_data(client_socket)

    # Check if response is as expected
    assert response == "Hello from the server!"

    # Close client socket
    client_socket.close()

    # Stop the server thread
    server_thread.join()

# Test case 2: Multiple clients connecting to the server
def test_multiple_clients():
    # Start server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    # Create multiple client sockets
    client_sockets = []
    for i in range(3):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', PORT))
        client_sockets.append(client_socket)

    # Send messages from clients
    for i, client_socket in enumerate(client_sockets):
        send_data(client_socket, f"Hello from client {i+1}")

    # Receive messages from server
    for i, client_socket in enumerate(client_sockets):
        response = receive_data(client_socket)
        assert response == f"Hello from server to client {i+1}"

    # Close client sockets
    for client_socket in client_sockets:
        client_socket.close()

    # Stop the server thread
    server_thread.join()

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
    data = receive_data(client_socket)
    # Send response to client
    send_data(client_socket, f"Hello from server to client {data.split()[2]}")
    # Close client connection
    client_socket.close()

# Run tests
if __name__ == "__main__":
    test_basic_communication()
    test_multiple_clients()
    print("All tests passed!")

