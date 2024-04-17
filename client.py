import socket
import threading

HOST = '127.0.0.1'  
PORT = 12345        

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            break

def send_message():
    while True:
        message = input()
        client_socket.send(bytes(message, 'utf-8'))

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    username_prompt = client_socket.recv(1024).decode('utf-8')
    print(username_prompt, end="")
    username = input()

    client_socket.send(bytes(username, 'utf-8'))

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_message)
    send_thread.start()

if __name__ == "__main__":
    start_client()
