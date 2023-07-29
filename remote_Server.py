import socket
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

SERVER = None
IP_ADDRESS = None
PORT = None
keyboard = None

def setup():
    global SERVER, IP_ADDRESS, PORT, keyboard
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_ADDRESS = 'your_ip_address'  # Replace 'your_ip_address' with your actual IP address
    PORT = 12345  # Choose a suitable port number
    
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)  # Listen to a maximum of 100 connections

def acceptConnections():
    global SERVER, IP_ADDRESS, PORT
    while True:
        client_socket, client_address = SERVER.accept()
        print(f"Connection established with {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle the client connection
        threading.Thread(target=recvMessage, args=(client_socket,)).start()

def getDeviceSize():
    monitors = get_monitors()
    if monitors:
        monitor = monitors[0]
        width = monitor.width
        height = monitor.height
        return width, height
    else:
        return None

def recvMessage(client_socket):
    global keyboard
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        # Process the message received from the client
        
        # Example: Print the message
        print(f"Received message: {message}")

def controller():
    # Define your controller logic here
    pass

# Main program
if __name__ == "__main__":
    setup()
    threading.Thread(target=acceptConnections).start()
    keyboard = pynput.keyboard.Controller()