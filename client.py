import socket

def start_client(student_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9955))

    # Send student_id to the server
    client.send(student_id.encode())

    response = client.recv(1024).decode()

    print(f"Client received response: {response}")

    client.close()

if __name__ == "__main__":
    student_id = "1202397"
    start_client(student_id)
