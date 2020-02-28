import socket , sys

host = "localhost"
port = 2233

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
serveurSocket.listen(0)

connexion, adresse = serveurSocket.accept()
print ("client IP : %s port %s"%(adresse[0], adresse[1]))

messageServeur = "connecté sur le serveur de Wakanda"
connexion.send(messageServeur.encode("Utf8"))
