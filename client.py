import socket
import sys

HOST = "localhost"
PORT = 4444
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
except socket.error:
    print ("connexion echoué avec le serveur ")
    sys.exit()

message_serveur = client_socket.recv(2048).decode("Utf8")
while True:
    if message_serveur.upper() == "EXIT":
        client_socket.send("exit".encode("Utf8"))
        break
    print ("Serveur ## ", message_serveur)
    message_client = input("Client >> ")
    client_socket.send(message_client.encode("Utf8"))
    message_serveur = client_socket.recv(2048).decode("Utf8")
print("**** Connexion Interrompue ...... ***** ")
client_socket.close()