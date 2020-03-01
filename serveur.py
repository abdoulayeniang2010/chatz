import socket , sys

HOST = "localhost"
PORT = 4444

# creation du socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serveur_socket.bind((HOST, PORT))

except socket.error:
    print("# WARNING: la liaison a l'adresse %s:%s a echoué" % (HOST, PORT))
    sys.exit()
while True:
    print("serveur pret en attente de connexion")
    serveur_socket.listen(5)
    connexion, adresse = serveur_socket.accept()
    print ("client IP : %s port %s"%(adresse[0], adresse[1]))
    message_serveur = "connecté sur le serveur de Wakanda"
    connexion.send(message_serveur.encode("Utf8"))
    message_client = connexion.recv(2048).decode("Utf8")

    """ Dialogue a tour de role entre le client et le serveur. Le client apres 
    la reception du premier message de bienvenue aura la main pour envoyer 
    vers le serveur et ce dernier apres reception pourra decider de repondre.
    un message exit permet d'arreter la connexion du client.
    Et de pouvoir donner la decision au serveur s'il decide de continuer ou pas.   
    """
    while True:
        print("Client >> ", message_client)
        if message_client.upper() == "EXIT":
            break
        message_serveur = input("Serveur # ")
        connexion.send(message_serveur.encode("Utf8"))
        message_client = connexion.recv(2048).decode("Utf8")
    connexion.send("exit".encode("Utf8"))
    print("connexion interrompue avec le client")
    connexion.close()
    """on demande au serveur s'il desir relancer un dialogue 
    ou bien terminer l'execution du programme.
    la variable test permet de recuperer l'entrer du serveur. 
    si test est vide ou (different de t ou r comme premier caractere)
    on ne sortira pas du boucle while 
    """
    test = "1"
    while len(test) == 0 or (test[0].upper() != "T" and test[0].upper() != "R"):
        test = input("R pour recommencer / T pour terminer [R/T] : ")

    if test[0].upper() == "T":
        sys.exit()