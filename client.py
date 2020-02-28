import socket, sys

host = "localhost"
port = 4441
#creation du socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #demande de connexion
    clientSocket.connect((host,port))
except socket.error:
    print ("connexion echoué")
    sys.exit()
#recevoir le message serveur
messageServeur = clientSocket.recv(2048).decode("Utf8")
#dialogue a tour de role entre le serveur et le client
while True:
    #si le serveur envoie exit
    if messageServeur.upper() == "EXIT":
        clientSocket.send("exit".encode("Utf8"))
        break
    # on affiche le message serveur
    print ("Serveur ## ",messageServeur)
    #saisir et envoyer son message
    messageClient = input("Client >> ")
    clientSocket.send(messageClient.encode("Utf8"))
    #recevoir le message
    messageServeur = clientSocket.recv(2048).decode("Utf8")
#fermeture de la connexion
print("connexion interrompue")
clientSocket.close()
