from os import path
from socket import *
import webbrowser
import os.path
from urllib import response

serverPort = 9966
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

def sendError(connection):
    connection.send(b"HTTP/1.1 404 Not Found \r\n")
    connection.send(b"Content-Type: text/html \r\n")
    connection.send(b"\r\n")
    print('\b\bResponse status: 404 Not Found')
    file = '<!DOCTYPE html><style>p{color: #49B7F0}h1 {font-size:  60px;}#error-message {color: red;}' \
           '* {text-align: center;font-size: 40px;font-weight: bold; }</style><main><header><title>Error</title></header><body><div ' \
           'id="error-message"><h1>The file is not found</h1><hr><div><img src="error.png" ></div></div><hr><div><p>Kareem soboh - 1201247</p><p>Mohammed ' \
           'Abo Jazar - 1192956</p><p>Basel Abu Hamed - 1202397</p></div><hr><div><p>IP Address: ' + str(ip) + \
           ', Port number: ' + str(port) + '</p></div></body></main></html> '
    connection.send(file.encode())
    connection.close()

while True:
    connection, address = serverSocket.accept()
    sentence = connection.recv(1024).decode('utf-8')
    ip = address[0]
    port = address[1]
    requestedFile = sentence.split(' ')[1]
    request = requestedFile.lstrip('/')
    print('IP: ' + str(ip) + ', Port: ' + str(port))
    print(sentence)

    if request == '' or request.endswith("en") or request=="index.html"  or request=="main_en.html":
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: text/html \r\n")
            connection.send(b"\r\n")
            mhtml = open('main_en.html', 'rb')
            connection.send(mhtml.read())
            mhtml.close()
    elif request.endswith("ar"):
            request = 'main.html'
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: text/html \r\n")
            connection.send(b"\r\n")
            mhtml = open('main_ar.html', 'rb')
            connection.send(mhtml.read())
            mhtml.close()

    elif request.endswith(".jpg"):

        file_exists = os.path.exists(str(request))
        if file_exists:
            requestType = 'image/jpg'
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: image/jpg \r\n")
            connection.send(b"\r\n")
            print('Response status: 200 OK\n\n')
            file = open(str(request), "rb")
            connection.send(file.read())
            file.close()
        else: sendError(connection)
    elif request.endswith(".png"):
        file_exists = os.path.exists(str(request))
        if file_exists:
            requestType = 'image/png'
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: image/png \r\n")
            connection.send(b"\r\n")
            print('Response status: 200 OK\n\n')
            file = open(str(request), "rb")
            connection.send(file.read())
            file.close()
        else:
            sendError(connection)
    elif request.endswith(".html"):
        file_exists = os.path.exists(str(request))
        if file_exists:
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: text/html \r\n")
            connection.send(b"\r\n")
            print('Response status: 200 OK\n\n')
            file = open(str(request), "rb")
            connection.send(file.read())
            file.close()
        else:
            sendError(connection)
    elif request.endswith(".css"):
        file_exists = os.path.exists(str(request))
        if file_exists:
            connection.send(b"HTTP/1.1 200 OK\r\n")
            connection.send(b"Content-Type: text/css \r\n")
            connection.send(b"\r\n")
            print('Response status: 200 OK\n\n')
            file = open(str(request), "rb")
            connection.send(file.read())
            file.close()
        else:
            sendError(connection)
    elif request.endswith("cr"):

            connection.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
            connection.send(bytes("Content-Type:\r\n", "UTF-8"))
            connection.send(bytes("location: https://www.cornell.edu/ \r\n" , "UTF-8"))
            print('Response status: 307 temporary Redirect\n\n')
            file = open(str(request), "rb")
            connection.send(file.read())
            file.close()
    elif request.endswith("so"):

        connection.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
        connection.send(bytes("Content-Type:\r\n", "UTF-8"))
        connection.send(bytes("location: https://stackoverflow.com/ \r\n", "UTF-8"))
        print('Response status: 307 temporary Redirect\n\n')
        file = open(str(request), "rb")
        connection.send(file.read())
        file.close()
    elif request.endswith("rt"):

        connection.send(bytes("HTTP/1.1 307 Temporary Redirect  \r\n", "UTF-8"))
        connection.send(bytes("Content-Type:\r\n", "UTF-8"))
        connection.send(bytes("location: https://ritaj.birzeit.edu/ \r\n", "UTF-8"))
        print('Response status: 307 temporary Redirect\n\n')
        file = open(str(request), "rb")
        connection.send(file.read())
        file.close()

    else:
        sendError(connection)


