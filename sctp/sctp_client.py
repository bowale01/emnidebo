import socket
import pysctp
import time

def sctp_client(server_ip='localhost', server_port=12345):
    sock = pysctp.sctpsocket_tcp(socket.AF_INET)
    sock.connect((server_ip, server_port))

    message = "Hello from SCTP client"
    print(f"Sending: {message}")
    sock.sctp_send(message.encode())

    data = sock.recv(1024)
    print(f"Received: {data.decode()}")

    sock.close()

if __name__ == "__main__":
    # Connect to the SCTP server
    sctp_client(server_ip='sctp-server.default.svc.cluster.local', server_port=12345)
