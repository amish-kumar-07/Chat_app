import socket
import threading

HOST = '127.0.0.1' 
PORT = 12345        

clients = {}

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(username + ": " + message)
        except:
            break

    client_socket.close()
    del clients[username]
    broadcast(username + " left the chat.")

def broadcast(message):
    for client in clients:
        client.send(bytes(message, 'utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("[SERVER] Server is running on {}:{}".format(HOST, PORT))

    while True:
        client_socket, client_address = server.accept()
        print("[SERVER] New connection from {}:{}".format(client_address[0], client_address[1]))

        client_socket.send(bytes("Enter your username: ", 'utf-8'))
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = username

        broadcast(username + " joined the chat.")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

if __name__ == "__main__":
    start_server()
