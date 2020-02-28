import socket , sys

host = "localhost"
port = 4441

# creation du socket
serveurSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #on associe le socket avec son adresse et un port d'ecoute
    serveurSocket.bind((host,port))
except socket.error:
    #au cas l'adresse est incorrect ou le port est deja utilisé
    print("# WARNING: %s:%s a echoué"%(host,port))
    sys.exit () #on quitte le programme

print ("serveur pret en attente de connexion")
serveurSocket.listen(3)
connexion, adresse = serveurSocket.accept()
print ("client IP : %s port %s"%(adresse[0], adresse[1]))

#envoie de mesage vers le client avec la methode send
messageServeur = "connecté sur le serveur de Wakanda"
connexion.send(messageServeur.encode("Utf8"))

#dialogue a tour de role entre le client et le serveur
messageClient = connexion.recv(2048).decode("Utf8")

while True:
    #affichage message du client
    print("Client >> ",messageClient)

    if messageClient.upper() == "EXIT":
        break
    #saisir et envoyer le message au climat
    messageServeur = input("Serveur # ")
    connexion.send(messageServeur.encode("Utf8"))
    #le serveur recoit le message du client
    messageClient = connexion.recv(2048).decode("Utf8")
#envoie du message exit suivie du fermeture de la connexion
connexion.send("exit".encode("Utf8"))
print("connexion interrompue")
connexion.close()
