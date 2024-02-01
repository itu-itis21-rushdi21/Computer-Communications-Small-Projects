import socket

port = 8080

def upload(client_socket, filename):
    with open(filename, "rb") as f:
        file_data = f.read()
        print(file_data)
        client_socket.sendall(file_data)

def download(client_socket, filename):
    with open(filename, "wb") as f:
        while True:
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            print(file_data)
            f.write(file_data)

def compare(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        file1_data = f1.read()
        file2_data = f2.read()
        if file1_data == file2_data:
            return True
        else:
            return False

def result(success):
    if success:
        print("transmission was successful.")
    else:
        print("transmission was not successful.")

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", port))
    print("Uploading the file to the server...")
    upload(client_socket, "client_data.txt")
    download(client_socket, "downloaded_data.txt")
    client_socket.close()
    success = compare("downloaded_data.txt", "client_data.txt")
    result(success)
