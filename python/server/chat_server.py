# chat_server.py
import socket
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
SEPARATOR = "<SEP>"

client_sockets = set()

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
            break
        else:
            msg = msg.replace(SEPARATOR, ": ")
            for client_socket in client_sockets:
                client_socket.send(msg.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected")
        client_sockets.add(client_socket)
        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()