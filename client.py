# client.py
# This file is intended to run on your mobile device (using Pydroid, for example)

import socket

SERVER_IP = 'your_server_ip_address'  # Replace 'your_server_ip_address' with the IP address of the server
SERVER_PORT = 12345  # Replace 12345 with the actual port number used by the server

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    client_socket.sendall("Hello, server!".encode())
    
    client_socket.close()

if __name__ == "__main__":
    main()
