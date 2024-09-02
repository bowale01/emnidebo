import socket
import pysctp

def sctp_server(host='0.0.0.0', port=12345):
    sock = pysctp.sctpsocket_tcp(socket.AF_INET)
    sock.bind((host, port))
    sock.listen(5)
    print(f"SCTP Server listening on {host}:{port}")

    while True:
        conn, addr = sock.accept()
        print(f"Connection from {addr}")
        data = conn.recv(1024)
        if data:
            print(f"Received: {data.decode()}")
            conn.sctp_send(data)
            print(f"Sent: {data.decode()}")
        conn.close()

if __name__ == "__main__":
    sctp_server()
