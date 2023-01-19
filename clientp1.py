import socket
import time

while True:
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP address and port
    server_ip = "192.168.1.100" # Replace with the IP address of the Raspberry Pi
    server_port = 1234

    # Connect to the server
    client_socket.connect((server_ip, server_port))

    # Receive data from the server
    received_data = client_socket.recv(1024).decode()
    
    # Save the received data to a file
    with open("SW_pokerstreaming/texts/p1.txt", "w") as file:
        file.write(received_data)
        file.close()        
    # Close the socket
    client_socket.close()

    # Wait for 10 seconds before next iteration
    time.sleep(10)