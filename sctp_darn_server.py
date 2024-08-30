#!/usr/bin/env python3
import socket

def main():
    # Create an SCTP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_SEQPACKET, socket.IPPROTO_SCTP)

    # Bind the socket to an address and port
    server_socket.bind(('0.0.0.0', 5000))

    # Start listening for incoming connections
    server_socket.listen(5)
    print("SCTP server listening on port 5000...")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")

        # Send a response back to the client
        client_socket.sendall(b"Hello from SCTP server!")

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    main()
