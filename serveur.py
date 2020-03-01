import socket , sys

HOST = "localhost"
PORT = 4444

# creation du socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serveur_socket.bind((HOST, PORT))
    print("serveur pret en attente de connexion")
except socket.error:
    print("# WARNING: la liaison a l'adresse %s:%s a echoué" % (HOST, PORT))
    sys.exit()
while True:
    serveur_socket.listen(5)
    connexion, adresse = serveur_socket.accept()
    print ("client IP : %s port %s"%(adresse[0], adresse[1]))
    message_serveur = "connecté sur le serveur de Wakanda"
    connexion.send(message_serveur.encode("Utf8"))
    message_client = connexion.recv(2048).decode("Utf8")
    while True:
        print("Client >> ", message_client)
        if message_client.upper() == "EXIT":
            break
        message_serveur = input("Serveur # ")
        connexion.send(message_serveur.encode("Utf8"))
        message_client = connexion.recv(2048).decode("Utf8")

    test = input("Recommencer / Terminer [R/T] : ")
    if test[0].upper() == "T":
        break
connexion.send("exit".encode("Utf8"))
print("connexion interrompue")
connexion.close()