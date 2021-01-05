"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s está online." % client_address)
        client.send(bytes("Digite o seu nome:", "utf8"))
        addresses[client] = client_address
        Thread(target=connect_client, args=(client,)).start()


def server_broadcast(msg, prefix=""):  # prefix is for name identification.
    """Server broadcast a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


def connect_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFF_SIZE).decode("utf8")

    welcome = "Bem vindo "
    client.send(bytes(welcome + name + "!", "utf8"))
    client.send(bytes("O envio de mensagens foi ativado!", "utf8"))
    msg = "%s entrou no chat!" % name
    server_broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFF_SIZE)
        if msg != bytes("{quit}", "utf8"):
            server_broadcast(msg, name + "")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()

            del clients[client]
            server_broadcast(bytes("%s saiu do chat" % name, "utf8"))
            break


clients = {}
addresses = {}

HOST = "localhost"
PORT = 33000
BUFF_SIZE = 1024
ADDRESS = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Aguardando conexão...")
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
