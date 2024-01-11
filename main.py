import socket
import os
import time

# Function to lock the screen (you may need to customize this based on the OS)
def lock_screen():

    os.system("gnome-screensaver-command -l")

def handle_client(client_socket, data):
    student_ids = ["1201247", "1192956","1202397"]

    if data in student_ids:
        print("Server: OS will lock screen after 10 seconds.")
        client_socket.send("Server: OS will lock screen after 10 seconds.".encode())
        time.sleep(10)
        lock_screen()
    else:
        print("Server: Error - Invalid student ID or text received.")

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9955))
    server.listen(1)

    print("Server listening on port 9955...")

    while True:
        client_socket, addr = server.accept()
        data = client_socket.recv(1024).decode()
        print(f"Server received data: {data}")

        handle_client(client_socket, data)

if __name__ == "__main__":
    start_server()
