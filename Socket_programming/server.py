import socket
import signal

student_id = 1
server_socket = None
port = 8080

def recive(client_socket, filename):
    with open(filename, "wb") as f:
        file_data = client_socket.recv(1024)
        f.write(file_data)

def send(client_socket, filename):
    with open(filename, "rb") as f:
        file_data = f.read()
        client_socket.sendall(file_data)
        client_socket.close()

def interrupt():
    if server_socket:
        server_socket.close()
        print("Exiting...")
        print("socket closed.")
        print("\nServer closed.")
        exit(0)

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    signal.signal(signal.SIGINT, interrupt)

    while True:
        server_socket.listen()
        print("Waiting for a connection from a client...")
        client_socket, client_address = server_socket.accept()
        print("Connection established with a client at {}".format(client_address))
        recive(client_socket, "server_data.txt")
        print("Uploading the text file to the client application...")
        send(client_socket, "server_data.txt")
