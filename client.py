import socket, sys

host = "localhost"
port = 2233

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #on demande une connexion sur l'adresse et le port renseignés
    clientSocket.connect((host,port))
except socket.error:
    print ("connexion echoué")
    sys.exit()
# le client recoit et affiche le message du serveur avec la methode recv
messageServeur = clientSocket.recv(2048).decode("Utf8")
print ("serveur >> ",messageServeur)
