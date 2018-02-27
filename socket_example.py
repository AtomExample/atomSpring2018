import socket

HOSTNAME = '127.0.0.1'
PORT = 2000
CONNECTION_COUNT = 1
MSG_LENGTH = 1024

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.bind((HOSTNAME, PORT))
serversocket.listen(CONNECTION_COUNT)

RESPONSE_TEMPLATE = 'HTTP/1.1 200 OK\nConnection: close\n\n<h3>{response_body}</h3>\n'

requests_counter = 0

print 'Listening on {0} port {1}'.format(HOSTNAME, PORT)
while True:
    clientsocket, address = serversocket.accept()
    print clientsocket.recv(MSG_LENGTH)
    requests_counter += 1
    clientsocket.send(
        RESPONSE_TEMPLATE.format(response_body=requests_counter)
    )
    clientsocket.shutdown(1)

    clientsocket.close()

serversocket.close()
